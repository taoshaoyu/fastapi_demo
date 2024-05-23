uvicorn app0:app --host 0.0.0.0 --port 5000

curl http://localhost:5002/items/

curl -X "POST" "http://127.0.0.1:5002/items/" \
     -H "accept: application/json" \
     -H "Content-Type: application/json" \
     -d "{\"name\": \"123\", \"price\":123}"