from fastapi import FastAPI
app = FastAPI()
@app.get("/hello")
def hello(name: str):
    if name is None:
        print("hello!")
    else:
        print("Hello" + name)
