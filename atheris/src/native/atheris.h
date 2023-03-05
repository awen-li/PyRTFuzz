/*
 * Copyright 2020 Google LLC
 * Copyright 2021 Fraunhofer FKIE
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// Compatible fuzzing engines must implement the functions specified in this
// header, and exactly one of them must be linked. See atheris.cc for
// documentation on the behavior of these functions.

#ifndef ATHERIS_ATHERIS_H_
#define ATHERIS_ATHERIS_H_

#include <functional>
#include <string>
#include <vector>

#include "pybind11/functional.h"
#include "pybind11/pybind11.h"
#include "pybind11/stl.h"

namespace atheris {

namespace py = pybind11;

std::vector<std::string> Setup(
    const std::vector<std::string>& args,
    const std::function<void(py::bytes data)>& test_one_input,
    py::kwargs kwargs);

std::vector<std::string> SetupCore(
    const std::vector<std::string>& args,
    const std::function<void(std::string script_name)>& test_one_script,
    const std::function<std::string(std::string dir)>& get_random_script,
    const std::function<std::string(std::string seed)>& get_specified_script,
    py::kwargs kwargs);


void Fuzz();
void FuzzLv1();
void FuzzLv2();

py::handle _trace_cmp(py::handle left, py::handle right, int opid, uint64_t idx,
                      bool left_is_const);
int _reserve_counter();
void _trace_branch(uint64_t idx);

}  // namespace atheris

#endif  // ATHERIS_ATHERIS_H_
