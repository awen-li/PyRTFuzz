#!/usr/bin/python


import re
import os
import sys, getopt
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as mpl
import matplotlib.font_manager as font_manager
from matplotlib.ticker import FuncFormatter


class TpNode ():
    def __init__ (self, Time, Cov, AppNum):
        self.Time  = Time
        self.Cov = Cov
        self.AppNum = AppNum


def LoadInput (File='PRTFuzz_perf.log'):
    TpNodeList = []
    with open (File, 'r') as F:
        AllLines = F.readlines()
        BaseTime = None
        for Line in AllLines:
            Items = ' '.join(Line.split ()).split()
            if not Items[0].isnumeric ():
                BaseTime = None
                continue
            if BaseTime == None:
                BaseTime = int(Items[0])
            Items = [(int(Items[0])-BaseTime)/3600, int (Items[1]), int (Items[2])]
            TpNodeList.append (TpNode (Items[0], Items[1], Items[2]))
    return TpNodeList

def GetAllLogs (DirName):
    LogFiles = []

    DirList = []
    DirList.append (DirName)

    while len (DirList) != 0:
        DirName = DirList.pop (0)
        FileList = os.listdir (DirName)
        for file in FileList:
            Path = os.path.join (DirName, file)
            if os.path.isdir (Path):
                DirList.append (Path)
                continue

            if Path.find ("PRTFuzz_perf.log") != -1:
                LogFiles.append (Path)

    return LogFiles

def GetCovByTimeLine (TpNodeList, TimeLine):
    CovList = {}
    for TN in TpNodeList:
        Time = int (TN.Time)
        if Time in TimeLine:
            CovList[Time] = TN.Cov

    CovList = list(CovList.values())
    while len (CovList) < len (TimeLine):
        CovList.append (CovList[-1])
    return CovList


def GetAppNumByTimeLine (TpNodeList, TimeLine):
    AnList = {}
    for TN in TpNodeList:
        Time = int (TN.Time)
        if Time in TimeLine:
            AnList[Time] = TN.AppNum
    AnList = list(AnList.values())
    while len (AnList) < len (TimeLine):
        AnList.append (AnList[-1])
    return AnList

def DrawRQ1 (Dir):
    print ("### RQ1: drawing Cov/AppNum over time line....")
    File = GetAllLogs (Dir)[0]
    TpNodeList = LoadInput (File)

    TimeLine = [v*4 for v in range (0, 19)]
    fig, (axCov, axApp) = plt.subplots(1, 2)

    # Cov over time
    X = TimeLine
    Y = GetCovByTimeLine (TpNodeList, TimeLine)
    axCov.plot(X, Y, linewidth=2.0, color='black')
    #axCov.set_title('Block coverage over time', fontsize=10)
    axCov.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    axCov.set(ylabel="#Block-coverage")
    axCov.set(xlabel="Time (hour)")

    # AppNum over time
    Y = GetAppNumByTimeLine (TpNodeList, TimeLine)
    axApp.plot(X, Y, linewidth=2.0, color='black')
    #axApp.set_title('Application number over time', fontsize=10)
    axApp.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    axApp.set(ylabel="#Application")
    axApp.set(xlabel="Time (hour)")
    
    fig.set_figwidth(12)
    fig.set_figheight(4)
    
    plt.savefig(Dir+'/PIC_RQ1')
    plt.close()
    return

def LoadRQ2Data (File):
    DList = {}
    with open (File, 'r') as F:
        AllLines = F.readlines()
        for Line in AllLines:
            Items = ' '.join(Line.split ()).split()
            if not Items[0].isnumeric ():
                continue
            DList[Items[0]] = Items
    return DList

def GetOverComplexity (DList, Index):
    Data = []
    for compl, item in DList.items ():
        Data.append (item[Index])
    return Data

def DrawRQ2 (Dir):
    print ("### RQ2: drawing line of SSGEN.")
    DList = LoadRQ2Data (Dir+'/data.txt')

    XLabels = list (DList.keys())
    fig, (axTimes, axMems, axCodeSize) = plt.subplots(1, 3)

    # SS-gen
    SSTimes = GetOverComplexity (DList, 1)
    SSMems  = GetOverComplexity (DList, 2)

    # PY-gen
    PYTimes = GetOverComplexity (DList, 3)
    PYMems  = GetOverComplexity (DList, 4)
    PYSize  = GetOverComplexity (DList, 5)

    # Times
    X = XLabels
    axTimes.plot(X, SSTimes, linewidth=2.0, color='b', label='SS-gen')
    axTimes.plot(X, PYTimes, linewidth=2.0, color='g', label='PY-gen')
    axTimes.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    axTimes.set(ylabel="Time (s)")
    #axTimes.set(xlabel="The number of complexity")
    axTimes.set_xticklabels(X, rotation=45)
    axTimes.legend(loc="upper left", prop={"size": 8})

    # Memories
    X = XLabels
    axMems.plot(X, SSMems, linewidth=2.0, color='b', label='SS-gen')
    axMems.plot(X, PYMems, linewidth=2.0, color='g', label='PY-gen')
    axMems.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    axMems.set(ylabel="Memory (MB)")
    axMems.set(xlabel="The number of complexity")
    axMems.set_xticklabels(X, rotation=45)
    axMems.legend(loc="upper left", prop={"size": 8})

    # Code size
    X = XLabels
    axCodeSize.plot(X, PYSize, linewidth=2.0, color='c')
    axCodeSize.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    axCodeSize.set(ylabel="Code size (KLoC)")
    #axCodeSize.set(xlabel="The number of complexity")
    axCodeSize.set_xticklabels(X, rotation=45)


    fig.set_figwidth(20)
    fig.set_figheight(6)
    
    plt.savefig(Dir+'/PIC_RQ2')
    plt.close()
    return

def DrawRQ3_1 (Dir):
    print ("### RQ3.1: drawing Cov/AppNum over time line with diff APP complexity....")

    TimeLine = [v*4 for v in range (0, 19)]
    fig, (axCov, axApp) = plt.subplots(1, 2)

    LineType = {'1':'-', '4':'-', '16':'-', '64':'-', '128':':', '256':':', '512':':', '1024':':'}
    ColorType = {'1':'k', '4':'g', '16':'r', '64':'b', '128':'k', '256':'g', '512':'r', '1024':'b'}

    AllLogs = GetAllLogs (Dir)
    AllLogs.sort ()
    for Log in AllLogs:
        Complexity = re.findall(r"-complex-(\d+?)/", Log)[0]
        LT = LineType[Complexity]
        CL = ColorType[Complexity]

        TpNodeList = LoadInput (Log)
        
        # Cov over time
        X = TimeLine
        Y = GetCovByTimeLine (TpNodeList, TimeLine)
        axCov.plot(X, Y, linewidth=2.0, color=CL, linestyle=LT, label='complexity-' + str(Complexity))
        #axCov.set_title('Block coverage over time', fontsize=10)
        axCov.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
        axCov.set(ylabel="#Block-coverage")
        axCov.set(xlabel="Time (hour)")
        axCov.legend(loc="upper left", prop={"size": 8})

        # AppNum over time
        Y = GetAppNumByTimeLine (TpNodeList, TimeLine)
        axApp.plot(X, Y, linewidth=2.0, color=CL, linestyle=LT, label='complexity-' + str(Complexity))
        #axApp.set_title('Application number over time', fontsize=10)
        axApp.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
        axApp.set(ylabel="#Application")
        axApp.set(xlabel="Time (hour)")
        axApp.legend(loc="upper left", prop={"size": 8})

    fig.set_figwidth(12)
    fig.set_figheight(4)
    
    
    plt.savefig(Dir+'/PIC_RQ3-1_Complexity')
    plt.close()

def DrawRQ3_2 (Dir):
    print ("### RQ3.2: drawing Cov/AppNum over time line with diff Lv2Budget....")

    TimeLine = [v*4 for v in range (0, 19)]
    fig, (axCov, axApp) = plt.subplots(1, 2)

    LineType = {'10':'-', '30':'-', '60':'-', '90':':', '180':':', '360':':'}
    ColorType = {'10':'k', '30':'g', '60':'b', '90':'k', '180':'g', '360':'b'}

    AllLogs = GetAllLogs (Dir)
    AllLogs.sort()
    for Log in AllLogs:
        Budget = re.findall(r"-Budget-(\d+?)/", Log)[0]
        LT = LineType[Budget]
        CL = ColorType[Budget]

        TpNodeList = LoadInput (Log)
        
        # Cov over time
        X = TimeLine
        Y = GetCovByTimeLine (TpNodeList, TimeLine)
        axCov.plot(X, Y, linewidth=2.0, color=CL, linestyle=LT, label='budget-' + str(Budget))
        #axCov.set_title('Block coverage over time', fontsize=10)
        axCov.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
        axCov.set(ylabel="#Block-coverage")
        axCov.set(xlabel="Time (hour)")
        axCov.legend(loc="upper left", prop={"size": 8})

        # AppNum over time
        Y = GetAppNumByTimeLine (TpNodeList, TimeLine)
        axApp.plot(X, Y, linewidth=2.0, color=CL, linestyle=LT, label='budget-' + str(Budget))
        #axApp.set_title('Application number over time', fontsize=10)
        axApp.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
        axApp.set(ylabel="#Application")
        axApp.set(xlabel="Time (hour)")
        axApp.legend(loc="upper left", prop={"size": 8})

    fig.set_figwidth(12)
    fig.set_figheight(4)
    
    plt.savefig(Dir+'/PIC_RQ3-2_Lv2Budget')
    plt.close()

def DrawRQ3_3 (Dir):
    print ("### RQ3.3: drawing Cov/AppNum over time line with typed/untyped....")

    TimeLine = [v*4 for v in range (0, 19)]
    fig, (axCov, axApp) = plt.subplots(1, 2)

    LineType = {'typed':'-', 'untyped':'-'}
    ColorType = {'typed':'k', 'untyped':'g'}

    AllLogs = GetAllLogs (Dir)
    for Log in AllLogs:
        Type = 'typed'
        if Log.find ("untyped") != -1:
            Type = 'untyped'
        
        LT = LineType[Type]
        CL = ColorType[Type]

        TpNodeList = LoadInput (Log)
        
        # Cov over time
        X = TimeLine
        Y = GetCovByTimeLine (TpNodeList, TimeLine)
        axCov.plot(X, Y, linewidth=2.0, color=CL, linestyle=LT, label=Type)
        #axCov.set_title('Block coverage over time', fontsize=10)
        axCov.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
        axCov.set(ylabel="#Block-coverage")
        axCov.set(xlabel="Time (hour)")
        axCov.legend(loc="upper left", prop={"size": 8})

        # AppNum over time
        Y = GetAppNumByTimeLine (TpNodeList, TimeLine)
        axApp.plot(X, Y, linewidth=2.0, color=CL, linestyle=LT, label=Type)
        #axApp.set_title('Application number over time', fontsize=10)
        axApp.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
        axApp.set(ylabel="#Application")
        axApp.set(xlabel="Time (hour)")
        axApp.legend(loc="upper left", prop={"size": 8})

    fig.set_figwidth(12)
    fig.set_figheight(4)
    
    plt.savefig(Dir+'/PIC_RQ3-3_Typed')
    plt.close()

def main(argv):
    Rq = ''

    try:
        opts, args = getopt.getopt(argv,"q:",["question="])
    except getopt.GetoptError:
        print ("picDraw.py -q <rq>")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-q", "--question"):
            Rq = arg

    if Rq == '':
        print ("Rq = ", Rq, ", input invalid!!!!")
        return
    
    if Rq == 'rq1' or Rq == 'all':    
        DrawRQ1 ('RQ1')

    if Rq == 'rq2' or Rq == 'all':    
        DrawRQ2 ('RQ2')

    if Rq == 'rq3.1' or Rq == 'all':    
        DrawRQ3_1 ('RQ3.1')

    if Rq == 'rq3.2' or Rq == 'all':    
        DrawRQ3_2 ('RQ3.2')

    if Rq == 'rq3.3' or Rq == 'all':    
        DrawRQ3_3 ('RQ3.3')

if __name__ == "__main__":
    main(sys.argv[1:])
    
