#!/usr/bin/env python
# encoding: utf-8

import sys
import pexpect

qemu_cmd = 'qemu-system-arm -M vexpress-a9 -kernel rt-thread/bsp/qemu-vexpress-a9/rtthread.elf -nographic -sd sd.bin'

def BoxStartup():
    child = pexpect.spawn(qemu_cmd)
    child.logfile_read = file('log.txt', 'w')

    child.expect_exact(' \ | /')
    qemu_output = child.before

    print child.after,
    child.expect('msh')
    print child.before

    return child

def BoxReady(box):
    box.send('\n')
    box.expect('msh')

    box.send('\n')
    box.expect('msh')

    return True

def BoxFileSystemReady(box):
    box.send('ls /\n')
    result = box.expect(['No such directory', 'Directory /:'])

    if result == 0:
        return False

    return True

def BoxFileSystemFormat(box):
    print('do file system format...')

    box.sendline('mkfs sd0')
    ret = box.expect(['mkfs failed', pexpect.TIMEOUT], timeout = 1)

    if ret == 0:
        print('Format file system failed!')
        return False

    return True

def BoxReload(box):
    BoxClose(box)
    return BoxStartup()

def BoxRunCmd(box, cmd, expect = None):
    box.sendline(cmd)

    if expect:
        result = box.expect(expect)
        return result

    return 0

def BoxLogClear(box):
    before = box.before
    after  = box.after

def BoxDelay(box, second):
    import time
    time.sleep(second)

def BoxClose(box):
    box.sendcontrol('a')
    box.send('c')
    try:
        box.close(force=True)
    except:
        print "done"
