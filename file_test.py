# _*_coding:utf-8_*_

import os

print(os.getcwd())

# with open('test1.txt', 'w') as f1:
#     for i in range(6):
#         f1.write('hello world ' + str(i) + '\n')
#
# with open('test2.txt', 'w') as f2:
#     for i in range(6, 10):
#         f2.write('hello world ' + str(i) + '\n')

with open('test2.txt', 'r') as f2:
    while 1:
        line = f2.readline()
        print(line)
        if line:
            # print(line)
            with open('test1.txt', 'r+') as f1:
                """the mode for test1.txt is r+"""
                content = f1.read()
                f1.seek(0, 0)
                f1.write(line + '\n' + content)
                f1.close()
        else:
            break
