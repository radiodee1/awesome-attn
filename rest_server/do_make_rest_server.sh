export IP="127.0.0.1"
export PORT=5000
export URL_ROOT="../OpenNMT-py"
export CONFIG="../json/conf.json"

# NOTE that these parameters are optionnal
# here, we explicitely set to default values
onmt_server --ip $IP --port $PORT --url_root $URL_ROOT --config $CONFIG
