#!/usr/bin/env python3.6

import argparse
import os
import datetime
import random

print("python3.6")

prefix_q = "question: "
prefix_a = 'answer: '

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

ages = [
    '10',
    '22',
    '52',
    '44',
    '5',
    '1'
        ]

def pairs_from_strings(ques, ans_prefix, ans_word, ans_suffix):
    sp1 = ' '
    sp2 = ' '
    if len(ans_prefix) == 0: sp1 = ''
    if len(ans_suffix) <= 1: sp2 = ''
    z = str(str(ans_prefix) + sp1 + str(ans_word) + sp2 + str(ans_suffix))
    #print(z, "z")
    x = [ques, z]
    return x
    
def output_from_list(out_list, ans_list, q, a_prefix, a_suffix, pad_text=None):
    for i in ans_list:
        #print(i)
        z =  [ pairs_from_strings(q, a_prefix, i, a_suffix) ]
        if pad_text is not None: # and isinstance(pad_text, str):
            if len(pad_text) == 1: pad_text = [pad_text]
            z[0][1] = random.choice(pad_text) + \
                      " " + z[0][0] + ' ' + z[0][1] + ' ' + prefix_q + z[0][0] + " " + prefix_a + z[0][1]
        out_list += z
    pass

def string_from_date_info(y, month, day, h = 0, m = 0, current_time=False):
    num = 100
    now = datetime.datetime.now()
    while num > 0 and current_time == False:
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

def make_single_context():

    input_dict = {
        'name': "jane",
        'place': "new york",
        'time': "dummy_time",
        'food': 'chocolate',
        'color': "blue",
        'number': "7",
        'age': '52'
    }

    input_dict['time'] = string_from_date_info(None,None,None, current_time=True)

    txt_list = [
        [[input_dict['name']], 'what is your name?', 'my name is', '.', 'names'],
        [[input_dict['place']], 'where are you?', 'i am in', '.', 'places'],
        [[input_dict['time']], 'what time is it?', 'it is', '.', 'times'],
        [[input_dict['food']], 'what is your favorite food?', 'i like', '.', 'foods'],
        [[input_dict['color']], 'what is your favorite color?', '', 'is my favorite color.', 'colors'],
        [[input_dict['number']], 'what is your favorite number?', 'my favorite number is', '.', 'numbers'],
        [[input_dict['age']], "how old are you?", "i am",".", 'ages']
    ]
    ctx_list = []
    ctx_list_long = None
    for i in txt_list:
        output_from_list(ctx_list, i[0], i[1], i[2], i[3] , ctx_list_long )
    ctx_list = [' '.join(i) for i in ctx_list]
    ctx_list = ' '.join(ctx_list)
    return  ctx_list



if __name__  == '__main__' :
    #print(food)
    parser = argparse.ArgumentParser(description='Make training file.')
    parser.add_argument('--length', help='Base file from movie corpus for db output', default=0)
    parser.add_argument('--test-on-screen', help='print some values to the screen.', action='store_true')
    parser.add_argument('--file-pairs', help='shift and repeat movie data', action='store_true')
    parser.add_argument('--tab-file',  help='Base file from movie corpus for db output', action='store_true')
    parser.add_argument('--random', help='Randomize saved values.', action='store_true')
    parser.add_argument('--large-context', help='Set large context', action='store_true')
    parser.add_argument('--no-prefix', help='Remove Q and A on data.', action='store_true')

    args = parser.parse_args()
    arg_length = 500
    arg_to_screen = False
    arg_tab = True
    arg_filename = 'data/extra'
    arg_random = False
    arg_ctx = False
    arg_no_prefix = False

    if args.random:
        arg_random = True

    if args.test_on_screen:
        arg_to_screen = True

    if int(args.length) > 0:
        arg_length = int(args.length)

    if args.file_pairs:
        arg_tab = False

    if args.tab_file:
        arg_tab = True

    if args.large_context:
        arg_ctx = True

    if args.tab_file == args.file_pairs:
        print("only one kind of output allowed.")
        exit()

    if args.no_prefix:
        arg_no_prefix = True
        prefix_a = ''
        prefix_q = ''

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
                [names, 'what is your name?', 'my name is', '.', 'names'],
                [places, 'where are you?', 'i am in', '.', 'places'],
                [times, 'what time is it?', 'it is','.', 'times'],
                [foods, 'what is your favorite food?', 'i like','.', 'foods'],
                [colors,'what is your favorite color?', '', 'is my favorite color.', 'colors'],
                [numbers, 'what is your favorite number?', 'my favorite number is', '.','numbers' ],
                [ages, "how old are you?", "i am", ".", 'ages']
            ]

    out_list = []
    for i in txt_list:
        out = []
        ctx_list = None
        ctx_list_long = None
        if arg_ctx:
            ctx_list_long = []
            for _ in i[0]:
                l = [ ii[4] for ii in txt_list if ii[4] is not i[4]]
                ctx_list = []
                for ll in l:
                    ll = [ii for ii in txt_list if ii[4] == ll ][0]
                    #print(ll[1:], 'll')
                    output_from_list(ctx_list, [random.choice(ll[0])], ll[1], ll[2], ll[3]  )
                    #print(ctx_list, 'ctx')
                ctx_list = [' '.join(i) for i in ctx_list]
                ctx_list = ' '.join(ctx_list)
                ctx_list_long += [ctx_list]
                #ctx_list = " ".join(ctx_list)
            #print(ctx_list_long)
            pass

        #print("---")
        #print(ctx_list)
        output_from_list(out, i[0], i[1], i[2], i[3] , ctx_list_long )
        out_list.append(out)
        #print(out_list[0], 'with context')

    out_random = []
    num_list = 0
    while len(out_random) < arg_length:
        
        n = num_list % (len(txt_list) + 0)

        if arg_random:
            n = random.randint(0, len(txt_list) - 1)

        z = [random.choice(out_list[n])]
        if arg_to_screen: print(z, 'z list')
        out_random += z
        num_list += 1

    for i in range(len(out_random)):
        if arg_to_screen:
            print(len(out_random[i][1]))
        pass

    if arg_to_screen:
        print()
        print (out_random, 'out_random')
    
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

    l = make_single_context()
    print("\n", l)