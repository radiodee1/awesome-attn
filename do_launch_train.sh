echo $#

if [[ "$#" == "1" && -f "$1"  ]] ; then
    echo "train_from $1"
    onmt_train --config yaml/train_config.yaml --train_from $1

    exit
fi


onmt_train --config yaml/train_config.yaml



