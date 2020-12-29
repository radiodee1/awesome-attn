echo $#

CONFIG="yaml/train_config.yaml"
CONFIG_EXTRA="yaml/train_config_extra.yaml"
CORPUS_EXTRA="data/bpe/extra.src"

if [[ -f "$CORPUS_EXTRA" ]] ; then
    CONFIG=$CONFIG_EXTRA
fi

if [[ "$#" == "1" && -f "$1"  ]] ; then
    echo "train_from $1"
    #onmt_train --config yaml/train_config.yaml --train_from $1
    onmt_train --config $CONFIG --train_from $1
    exit
fi

if [[ "$#" == "1" && ! -f "$1" ]] ; then
    echo "$1 is not a file."
    exit
fi


#onmt_train --config yaml/train_config.yaml
onmt_train --config $CONFIG


