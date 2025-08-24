from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Receipt Fraud Detection API Running"}
