#-*-coding:utf-8 -*-
#coding=utf-8
print("你好，python")


print("九九乘法表（第一种）")
for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print ("%s * %s = %s " % (j, i, j * i)),
    print ""

print('倒置')
for j in range(1, 10):
    for i in range(1, 10):
        if i >= j:
            print ("%s * %s = %s " % (j, i, j * i)),
    print "\t\n"

print('九九乘法表（第二种）')
for m in range(1,10):
    for n in range (1,m+1):
        print m,'*',n,'=',m*n,'\t',
    print ''
