from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Hector"}


@app.get("/inversiones/{inversion}")
def read_item(inversion: int, q: Union[str, None] = None):
    return {"inversion": inversion, "q": q}