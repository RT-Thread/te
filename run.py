#!/usr/bin/env python
# encoding: utf-8

import qemubox
import time

from testcase import *
from testcase.filesystem import *
from testcase.kernel import *
from testcase.example import *

def RunTestCase(box):
    tc = globals()

    for item in tc:
        if item.startswith('testcase'):
            testcase = tc[item]

            if testcase.__name__.rfind('.'):
                name = testcase.__name__[testcase.__name__.rfind('.') + 1:]
            else:
                name = testcase.__name__

            # print(testcase.__name__),
            if testcase.__doc__:
                print(testcase.__doc__),
            if not testcase.run(box):
                print("[%s] failed." % name)
                return
            else:
                print("[%s] passed!" % name)

    return

if __name__ == '__main__':
    box = qemubox.BoxStartup()

    if qemubox.BoxReady(box):

        if not qemubox.BoxFileSystemReady(box):
            if qemubox.BoxFileSystemFormat(box):
                box = qemubox.BoxReload(box)
                if not qemubox.BoxFileSystemReady(box):
                    print('file system failed! Please check manually!')
                    qemubox.BoxClose(box)
                    exit(-1)

        RunTestCase(box)

        time.sleep(0.5)
        qemubox.BoxClose(box)
