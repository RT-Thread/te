import os

list = os.listdir(os.path.dirname(__file__))
testcases = []

# filter testcases
for item in list:
    if item.startswith('testcase_') and item.endswith('.py'):
        m = item.replace('.py', '')
        testcases.append(m)

__all__ = testcases
