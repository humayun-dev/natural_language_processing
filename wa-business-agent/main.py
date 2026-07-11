from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "alive"}

@app.get("/webhook")
def webhook_placeholder():
    return {"status": "webhook not configured yet"}