# awesome-attn
workspace for attention experiments

## starting scripts

* `./do_make_nmt_init.sh` - init submodule.
* `./do_make_movie_download.sh` - run this to download movie subtitles database.
* `./do_make_db_tab_from_cornel_movie.py` - run this to get individual question/answers.
* `./do_make_split.py --filename data/movie_lines.txt.tab.txt  --length -1 --pairs --mode train` - this moves q/a into diffrent files. 
