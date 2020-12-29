# awesome-attn
workspace for attention experiments

## starting scripts

* `. ./do_make_source_virtualenv.sh` - setup virtual environment. (Note leading dot!)
* `./do_make_nmt_init.sh` - init submodule.
* `./do_make_movie_download.sh` - run this to download movie subtitles database.
* `./do_make_db_tab_from_cornell_movie.py data/movie_lines.txt --text-file ` - run this to get individual question/answers.
* `./do_make_split.py --filename data/movie_lines.txt.tab.txt  --length -1 --pairs --mode train --force` - this moves q/a into diffrent files. 
* `./do_make_split.py --filename data/movie_lines.txt.tab.txt  --length 500 --pairs --mode valid --force` - simple `valid.from` and `.to` files. These are not truly 'holdout sets'. The data is repeated.
* `./do_make_split.py --filename data/movie_lines.txt.tab.txt  --length 500 --pairs --mode test --force` - simple `test.from` and `.to` files. These are not truly 'holdout sets'. The data is repeated.

Then:

* `./do_launch_prep.sh` - this sets up bpe files.
* `./do_launch_train.sh` - this trains a model.
