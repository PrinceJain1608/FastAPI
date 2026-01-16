from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def getData():
  return "Welcome to Home..."