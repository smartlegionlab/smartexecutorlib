# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright (c) 2018-2024, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
import os
import subprocess


class SubExecutor:

    @classmethod
    def execute(cls, command: str):
        p = subprocess.Popen(command, shell=True, stderr=subprocess.DEVNULL)
        status = p.wait()
        return not bool(status)


class OsExecutor:
    @classmethod
    def execute(cls, command: str):
        status = os.system(command)
        return not bool(status)


class SmartExecutor:
    os = OsExecutor()
    sub = SubExecutor()


class ExecutorsFactory:
    @classmethod
    def get_os_executor(cls):
        return OsExecutor()

    @classmethod
    def get_sub_executor(cls):
        return SubExecutor()

    @classmethod
    def get_executor(cls):
        return SmartExecutor()
