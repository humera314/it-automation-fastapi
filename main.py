from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello! The system is healthy ✅"}

@app.get("/status")
def check_status():
    return {"status": "OK", "uptime": "Running smoothly since boot 🚀"}
