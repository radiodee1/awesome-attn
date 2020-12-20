export IP="127.0.0.1"
export PORT=5000
export URL_ROOT="/OpenNMT-py"
export CONFIG="json/server_conf.json"

# NOTE that these parameters are optionnal
# here, we explicitely set to default values
onmt_server --ip $IP --port $PORT --url_root $URL_ROOT --config $CONFIG
