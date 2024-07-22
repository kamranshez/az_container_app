from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World1", "World2": "This is pakistan"}

@app.get("about/")
def about_page():
    return {"Institute": "World1", "World2": "Pakistan zinda bad 1234567 80"}

