//===- FuzzerInternal.h - Internal header for the Fuzzer --------*- C++ -* ===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//
// Define the main class fuzzer::Fuzzer and most functions.
//===----------------------------------------------------------------------===//

#ifndef LLVM_FUZZER_INTERNAL_H
#define LLVM_FUZZER_INTERNAL_H

#include "FuzzerDataFlowTrace.h"
#include "FuzzerDefs.h"
#include "FuzzerExtFunctions.h"
#include "FuzzerInterface.h"
#include "FuzzerOptions.h"
#include "FuzzerSHA1.h"
#include "FuzzerValueBitMap.h"
#include <algorithm>
#include <atomic>
#include <chrono>
#include <climits>
#include <cstdlib>
#include <string.h>

namespace fuzzer {

using namespace std::chrono;

class Fuzzer {
public:

  Fuzzer(UserCallback CB, InputCorpus *Corpus, MutationDispatcher &MD,
            FuzzingOptions Options);
  Fuzzer(UserCallbackCore CBCore, InputCorpus *Corpus, MutationDispatcher &MD,
            FuzzingOptions Options);
  ~Fuzzer();
  void Loop(Vector<SizedFile> &CorporaFiles);

  void ReadAndExecuteSeedCorpora(Vector<SizedFile> &CorporaFiles);
  void MinimizeCrashLoop(const Unit &U);
  void RereadOutputCorpus(size_t MaxSize);

  void LoopPyCore(Vector<SizedFile> &CorporaFiles, GetSpecifiedSeed CbSpecified);
  int RunOneScript(const char *Script);
  void ExecuteCBCore(const char *Script);
  void PrintPulseAndReportSlowInput(const char *Script);
  void SetFuzzer (UserCallback CB, InputCorpus *Corpus);
  
  size_t secondsSinceProcessStartUp() {
    return duration_cast<seconds>(system_clock::now() - ProcessStartTime)
        .count();
  }

  inline size_t SecondsDuration() {
    return duration_cast<seconds>(system_clock::now() - LastUpdateTime).count();
  }

  inline void SetLastUpdateTime () {
    size_t Last = SecondsDuration();
    LastUpdateTime = system_clock::now();

    printf ("####[SetLastUpdateTime] duration = %u\r\n", Last);
  }

  bool TimedOut() {
    if (Options.MaxTotalTimeSec <= 0) {
      return false;
    }
    else {
      size_t LastUpdateTime = SecondsDuration();
      if (LastUpdateTime > static_cast<size_t>(Options.MaxTotalTimeSec)) {
          return true;
      }
      else {
        return false;
      }
    }
  }

  size_t execPerSec() {
    size_t Seconds = secondsSinceProcessStartUp();
    return Seconds ? TotalNumberOfRuns / Seconds : 0;
  }

  size_t getTotalNumberOfRuns() { return TotalNumberOfRuns; }

  static void StaticAlarmCallback();
  static void StaticCrashSignalCallback();
  static void StaticExitCallback();
  static void StaticInterruptCallback();
  static void StaticFileSizeExceedCallback();
  static void StaticGracefulExitCallback();

  void ExecuteCallback(const uint8_t *Data, size_t Size);
  bool RunOne(const uint8_t *Data, size_t Size, bool MayDeleteFile = false,
              InputInfo *II = nullptr, bool *FoundUniqFeatures = nullptr);

  // Merge Corpora[1:] into Corpora[0].
  void Merge(const Vector<std::string> &Corpora);
  void CrashResistantMergeInternalStep(const std::string &ControlFilePath);
  MutationDispatcher &GetMD() { return MD; }
  void PrintFinalStats();
  void SetMaxInputLen(size_t MaxInputLen);
  void SetMaxMutationLen(size_t MaxMutationLen);
  void RssLimitCallback();

  bool InFuzzingThread() const { return IsMyThread; }
  size_t GetCurrentUnitInFuzzingThead(const uint8_t **Data) const;
  void TryDetectingAMemoryLeak(const uint8_t *Data, size_t Size,
                               bool DuringInitialCorpusExecution);

  void HandleMalloc(size_t Size);
  static void MaybeExitGracefully();
  std::string WriteToOutputCorpus(const Unit &U, bool IsLv2=true);

private:
  void InitFuzzer ();
  void MutatePyAndTest(const char* Script, GetSpecifiedSeed CbSpecified);
  
  void AlarmCallback();
  void CrashCallback();
  void ExitCallback();
  void CrashOnOverwrittenData();
  void InterruptCallback();
  void MutateAndTestOne();
  void PurgeAllocator();
  void ReportNewCoverage(InputInfo *II, const Unit &U, bool IsLv2=true);
  void PrintPulseAndReportSlowInput(const uint8_t *Data, size_t Size);
  void WriteUnitToFileWithPrefix(const Unit &U, const char *Prefix);
  void PrintStats(const char *Where, const char *End = "\n", size_t Units = 0,
                  size_t Features = 0);
  void PrintStatusForNewUnit(const Unit &U, const char *Text);
  void CheckExitOnSrcPosOrItem();

  static void StaticDeathCallback();
  void DumpCurrentUnit(const char *Prefix);
  void DeathCallback();

  void AllocateCurrentUnitData();
  uint8_t *CurrentUnitData = nullptr;
  std::atomic<size_t> CurrentUnitSize;
  uint8_t BaseSha1[kSHA1NumBytes];  // Checksum of the base unit.

  bool GracefulExitRequested = false;

  size_t TotalNumberOfRuns = 0;
  size_t NumberOfNewUnitsAdded = 0;

  size_t LastCorpusUpdateRun = 0;

  bool HasMoreMallocsThanFrees = false;
  size_t NumberOfLeakDetectionAttempts = 0;

  system_clock::time_point LastAllocatorPurgeAttemptTime = system_clock::now();

  UserCallback CB;
  InputCorpus *Corpus;
  MutationDispatcher &MD;
  FuzzingOptions Options;
  DataFlowTrace DFT;

  UserCallbackCore CBCore;
  InputCorpus *PyCorpus;

  system_clock::time_point ProcessStartTime = system_clock::now();
  system_clock::time_point LastUpdateTime = system_clock::now();

  system_clock::time_point UnitStartTime, UnitStopTime;
  long TimeOfLongestUnitInSeconds = 0;
  long EpochOfLastReadOfOutputCorpus = 0;

  size_t MaxInputLen = 0;
  size_t MaxMutationLen = 0;
  size_t TmpMaxMutationLen = 0;

  Vector<uint32_t> UniqFeatureSetTmp;

  // Need to know our own thread.
  static thread_local bool IsMyThread;

  const char* PyCurScript;
};


Fuzzer* GetFuzzer ();

struct ScopedEnableMsanInterceptorChecks {
  ScopedEnableMsanInterceptorChecks() {
    if (EF->__msan_scoped_enable_interceptor_checks)
      EF->__msan_scoped_enable_interceptor_checks();
  }
  ~ScopedEnableMsanInterceptorChecks() {
    if (EF->__msan_scoped_disable_interceptor_checks)
      EF->__msan_scoped_disable_interceptor_checks();
  }
};

struct ScopedDisableMsanInterceptorChecks {
  ScopedDisableMsanInterceptorChecks() {
    if (EF->__msan_scoped_disable_interceptor_checks)
      EF->__msan_scoped_disable_interceptor_checks();
  }
  ~ScopedDisableMsanInterceptorChecks() {
    if (EF->__msan_scoped_enable_interceptor_checks)
      EF->__msan_scoped_enable_interceptor_checks();
  }
};

} // namespace fuzzer

#endif // LLVM_FUZZER_INTERNAL_H
