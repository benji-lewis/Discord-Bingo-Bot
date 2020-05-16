#!/usr/bin/env python3

import random as rn
import discord as ds


def NumGen():
    used=[]
    while len(used) != 100:
        num = rn.randint(0,100)
        if num in used:
            print(used)
            continue
        
        else:
            used.append(num)
            return (num)
        

while True:
    print(NumGen())
        
