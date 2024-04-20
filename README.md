# LLVM Spam Detector

```bash
docker build -t spam-ai:latest .
docker run --rm -p 8000:80 spam-ai:latest
```

```bash
curl http://127.0.0.1:8000/analyze -H "Content-Type: application/json" -d '{"payload": "hello"}'
{"score":0.999976396560669,"type":"Not Spam"}

curl http://127.0.0.1:8000/analyze -H "Content-Type: application/json" -d '{"payload": "Thank you for paying last month’s bill. We’re rewarding our very best customers with a gift for their loyalty. Click here!"}'
{"score":0.9999904632568359,"type":"Spam"}
```