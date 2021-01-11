# awesome-attn
workspace for attention experiments

## starting scripts

* `source ./do_make_source_virtualenv.sh ` - setup virtual environment. 
* `./do_make_nmt_init.sh ` - init submodule.
* `./do_make_movie_download.sh ` - run this to download movie subtitles database.
* `./do_make_db_tab_from_cornell_movie.py data/movie_lines.txt --text-file --repeat ` - run this to get individual question/answers.

The next few scripts split up the input file from the movie dialog corpus.

* `./do_make_split.py --filename data/movie_lines.txt.tab.txt  --length -1 --start 500 --pairs --mode train --force ` - this moves q/a into diffrent files. 
* `./do_make_split.py --filename data/movie_lines.txt.tab.txt  --length 500 --start 0 --pairs --mode valid --force ` - simple `valid.from` and `.to` files. These are not truly 'holdout sets'. The data is repeated.
* `./do_make_split.py --filename data/movie_lines.txt.tab.txt  --length 500 --start 0 --pairs --mode test --force ` - simple `test.from` and `.to` files. These are not truly 'holdout sets'. The data is repeated.

This script generates the 'extra' files for the transformer training. It is not required. This is a sort of 'dummy' corpus.

* `./do_make_corpus_tab.py --file-pairs  --test-on-screen --length 150000 --large-context --encoder-context ` - run this if you want the 'extra' corpus.

Then:

* `./do_launch_prep.sh ` - this sets up bpe files.
* `./do_launch_train.sh ` - this trains a model. As a first parameter you can use the name of a checkpoint that you want to start with.
