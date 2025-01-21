#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import random
num=random.randint(1,100)
i=1
print(num)
a=int(input("请输入数字"))
while a!=num:
    if a<num:
        print("小了请继续")
    elif a>num:
        print("大了请继续")
    a=int(input("请输入数字"))
    i+=1
print(f"恭喜你猜了{i}次猜中了")
