export HOST="127.0.0.1"
export PORT=5000
export URL_ROOT="/"
export CONFIG="../json/conf.json"

curl -i -X POST -H "Content-Type: application/json" \
    -d '[{"src": "this is a test for model 0", "id": 0}]' \
    http://$HOST:$PORT$URL_ROOT/translate
