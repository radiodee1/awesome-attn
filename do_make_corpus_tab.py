#!/usr/bin/env python3.6

import argparse
import os
import datetime

print("python3.6")

names = [
            'david',
            'edward',
            'bob',
            'jane',
            'kate',
            'mary',
            'john',
            'paul',
            'george'
        ]

places = [
            'california',
            'new york',
            'washington',
            'georgia',
            'nevada',
            'mississippi',
            'florida'
        ]

times = []

food = [
            'ice cream',
            'chili',
            'ham',
            'candy',
            'chocolate'
        ]

color = [
            'red',
            'green',
            'blue',
            'yellow'
        ]

def string_from_date_info(y, month, day, h = 0, m = 0):
    num = 100
    now = datetime.datetime.now()
    while num > 0:
        try:
            now = datetime.datetime(y, month, day, hour=h, minute=m)
        except:
            day -= 1
            num -= 1
            continue
        print(num)
        num -= 1
        break
    time = now.strftime("%I:%M %p")
    date = now.strftime("%B %d, %Y")
    return time + ", " + date 

if __name__  == '__main__' :
    print(food)
    now = datetime.datetime.now()
    time = now.strftime("%I:%M %p")
    date = now.strftime("%B %d, %Y")
    print(time+ ", " + date )

    print(string_from_date_info(2020, 10, 12))

    for i in [2012, 2020, 2021]: # year
        for j in range(1, 12):
            for k in range(0, 31):
                for l in [0,12, 15]: # hour
                    for m in [0, 30, 45, 61]: # minutes
                        times += [string_from_date_info(i, j, k, h=l, m=m)]

    print("times generated", len(times))




