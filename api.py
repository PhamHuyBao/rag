from typing import Union


from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from main import main

app = FastAPI()


@app.get("/querry/{querryString}")
def get_querry_rag(querryString: str):
    return main(querryString)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}