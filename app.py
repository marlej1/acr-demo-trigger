from fastapi import FastAPI

app = FastAPI();

@app.get("/")
def home():
    return {
        "message": "Hello 4",
        "status": "success"
    }

