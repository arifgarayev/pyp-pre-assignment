from typing import IO
from logging.config import dictConfig
import logging
import pathlib
from typing import List
import databases
import sqlalchemy
import pandas as pd
import openpyxl
import xlrd, openpyxl, pyxlsb
import psycopg2
from fastapi import FastAPI, File, Header, Depends, UploadFile, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import urllib

import uvicorn

from api.const.constants import *

from api.validation import FileValidation

# *** ------------------------------------- *** #



#swaggerUI default route, create instance
app = FastAPI(docs_url='/swagger', redoc_url=None)

#enable Cross origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

#post method decorator
@app.post('/UploadData/POST', description='FILE_SIZE must not exceed = 5MB\nFILE_EXTENSION must be either .xlxs or .xls')
async def upload(file: UploadFile = File(...)):
    #async funtion for file uploads

    if await FileValidation(file).validation(): #direct class method call for type and size validation
        file_path = os.path.abspath(os.path.join(os.getcwd(), f'../uploaded_files/{file.filename}'))

        with open(file_path, 'w+') as out_pt:
            content = await file.read()
            out_pt.write(content.decode('utf-8'))
            out_pt.close() # close file pointer




        # create empty xls/xlsx metadata file (not just binary)


        df = pd.read_excel(file_path, engine='openpyxl')

        print(df)


        return {'data': {
            'is_valid': True,
            # 'is_empty': df.empty,
            'file_name': file.filename,
            'mime_type': file.content_type
        }}



if __name__ == '__main__':

    cwd = pathlib.Path(__file__).parent.resolve()

    # print(cwd)

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        reload=True,
        port=8000,
        log_config=f"{cwd}/log.ini", #initialize log config from log.ini
        log_level="info" #log level
    )


