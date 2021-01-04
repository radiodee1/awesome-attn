export IP="127.0.0.1"
export PORT=5000
export URL_ROOT="/OpenNMT-py"
export CONFIG="json/server_conf_best.json"

echo $#
echo "Enter number for 'best' saved checkpoint step."

if [[ "1" -eq "$#" && "$1" != "best" ]] ; then
    echo 'one input'
    echo $1

    if [[ -f data/transformer_movie_chat_step_$1.pt ]] ; then
        rm data/transformer_movie_chat_step_best.pt
        cp data/transformer_movie_chat_step_$1.pt data/transformer_movie_chat_step_best.pt
    fi

fi

if [[ "1" -eq "$#" && -f $1 ]] ; then
    echo 'one input'
    echo $1
    
    echo "last 3 chars ${1: -3}"
    

    if [[  ${1: -3} == ".pt" ]] ; then
        rm data/transformer_movie_chat_step_best.pt
        cp $1 data/transformer_movie_chat_step_best.pt
    fi

fi

onmt_server --ip $IP --port $PORT --url_root $URL_ROOT --config $CONFIG 
