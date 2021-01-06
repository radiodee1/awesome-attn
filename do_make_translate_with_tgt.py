#!/bin/bash

echo $@

cat $0

bin/translate.py $@

#bin/translate.py --src test.txt --model data/transformer_movie_chat_step_5000.pt --tgt_prefix --tgt "what time is it? the time is 3:45 PM January 5, 2021"


