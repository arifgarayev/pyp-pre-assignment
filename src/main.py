from typing import IO
from logging.config import dictConfig
from src.config import log_config

from tempfile import NamedTemporaryFile
import shutil

from fastapi import FastAPI, File, Header, Depends, UploadFile, HTTPException
from starlette import status

import pydantic

import uvicorn

from api.const.constants import *

from api.validation import FileValidation

# *** ------------------------------------- *** #



#swaggerUI default route, create instance
app = FastAPI(docs_url='/swagger', redoc_url=None)


#post method decorator
@app.post('/UploadData/POST', description='FILE_SIZE must not exceed = 5MB\nFILE_EXTENSION must be either .xlxs or .xls')
async def upload(file: UploadFile = File(...)):
    #async funtion for file uploads

    if await FileValidation(file).validation(): #direct class method call for type and size validation

        pass


        return {'data': {
            'is_valid': True,
            'file_name': file.filename,
            'mime_type': file.content_type
        }}



if __name__ == '__main__':

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        reload=True,
        port=8000

    )
