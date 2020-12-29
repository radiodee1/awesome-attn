#!/usr/bin/env python3.6

import argparse
import os
import datetime
import random

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
    sp1 = ' '
    sp2 = ' '
    if len(ans_prefix) == 0: sp1 = ''
    if len(ans_suffix) <= 1: sp2 = ''
    z = str(str(ans_prefix) + sp1 + str(ans_word) + sp2 + str(ans_suffix))
    #print(z, "z")
    x = ques, z
    return x
    
def output_from_list(out_list, ans_list, q, a_prefix, a_suffix):
    for i in ans_list:
        #print(i)
        z =  [ pairs_from_strings(q, a_prefix, i, a_suffix) ]
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
    parser = argparse.ArgumentParser(description='Make training file.')
    parser.add_argument('--length', help='Base file from movie corpus for db output', default=0)
    parser.add_argument('--test-on-screen', help='print some values to the screen.', action='store_true')
    parser.add_argument('--file-pairs', help='shift and repeat movie data', action='store_true')
    parser.add_argument('--tab-file',  help='Base file from movie corpus for db output', action='store_true')
    
    args = parser.parse_args()
    arg_length = 500
    arg_to_screen = False
    arg_tab = True
    arg_filename = 'data/extra'

    if args.length > 0:
        arg_length = args.length

    if args.file_pairs:
        arg_tab = False

    if args.tab_file:
        arg_tab = True

    if args.tab_file == args.file_pairs:
        print("only one kind of output allowed.")
        exit()


    now = datetime.datetime.now()
    time = now.strftime("%I:%M %p")
    date = now.strftime("%B %d, %Y")
    if arg_to_screen:
        print(time+ ", " + date )

    #print(string_from_date_info(2020, 10, 12))

    for i in [2012, 2020, 2021]: # year
        for j in range(1, 12): # month
            for k in range(0, 31): # day
                for l in [0,12, 15]: # hour
                    for m in [0, 30, 45, 61]: # minutes
                        times += [string_from_date_info(i, j, k, h=l, m=m)]

    if arg_to_screen:
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
        out = []
        output_from_list(out, i[0], i[1], i[2], i[3]  )
        out_list.append(out)

    out_random = []
    num_list = 0
    while len(out_random) <= 500:
        
        n = num_list % (len(txt_list) + 0)
        #print( n )
        out_random += [random.choice(out_list[n])]
        num_list += 1
    
    if arg_to_screen:
        print (out_random)
    
    if arg_tab:
        arg_filename = arg_filename + '.tab.txt'
        z = open(arg_filename, 'w')
        for i in out_random:
            z.write(i[0] + '\t' + i[1] + '\n')
        z.close()
        pass
    else:
        y = open(arg_filename + '.src','w')
        z = open(arg_filename + '.tgt', 'w')
        for i in out_random:
            y.write(i[0] + '\n')
            z.write(i[1] + '\n')
        y.close()
        z.close()
        pass

