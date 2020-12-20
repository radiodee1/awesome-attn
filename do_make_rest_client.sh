export HOST="127.0.0.1"
export PORT=5000
export URL_ROOT="/OpenNMT-py"

curl -i -X POST -H "Content-Type: application/json" \
    -d '[{"src": "this is a test for model 0", "id": 100}]' \
    http://$HOST:$PORT$URL_ROOT/translate | Tokenizer/cli/detokenize
 


