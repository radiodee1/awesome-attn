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

foods = [
            'ice cream',
            'chili',
            'ham',
            'candy',
            'chocolate'
        ]

colors = [
            'red',
            'green',
            'blue',
            'yellow'
        ]

numbers = [
            '0',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            'zero',
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine'
        ]

def pairs_from_strings(ques, ans_prefix, ans_word, ans_suffix):

    z = str(str(ans_prefix) + ' ' + str(ans_word) + ' ' + str(ans_suffix))
    #print(z, "z")
    x = ques, z
    return z
    
def output_from_list(out_list, ans_list, q, a_prefix, a_suffix):
    for i in ans_list:
        print(i)
        z =  [pairs_from_strings(q, a_prefix, i, a_suffix) ]
        out_list += z
    pass

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
        #print(num)
        num -= 1
        break
    time = now.strftime("%I:%M %p")
    date = now.strftime("%B %d, %Y")
    return time + ", " + date 

if __name__  == '__main__' :
    #print(food)
    now = datetime.datetime.now()
    time = now.strftime("%I:%M %p")
    date = now.strftime("%B %d, %Y")
    print(time+ ", " + date )

    #print(string_from_date_info(2020, 10, 12))

    for i in [2012, 2020, 2021]: # year
        for j in range(1, 12): # month
            for k in range(0, 31): # day
                for l in [0,12, 15]: # hour
                    for m in [0, 30, 45, 61]: # minutes
                        times += [string_from_date_info(i, j, k, h=l, m=m)]

    print("times generated", len(times))
    #print(times)

    txt_list = [
                [names, 'what is your name?', 'my name is', '.'],
                [places, 'where are you?', 'i am in', '.'],
                [times, 'what time is it?', 'it is','.'],
                [foods, 'what is your favorite food?', 'i like','.'],
                [colors,'what is your favorite color?', '', 'is my favorite color.'],
                [numbers, 'what is your favorite number?', 'my favorite number is', '.' ]
            ]

    out_list = []
    for i in txt_list:
        output_from_list(out_list, i[0], i[1], i[2], i[3]  )
    print(out_list)
