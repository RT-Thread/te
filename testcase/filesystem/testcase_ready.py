"""
testcase: file system ready
"""

import qemubox

def run(box):
    ret = qemubox.BoxRunCmd(box, 'ls', ['No such directory', 'Directory /:'])

    if ret == 0:
        print('file system not ready!')
        return False
    else:
        print('file system ready!')

    return True
