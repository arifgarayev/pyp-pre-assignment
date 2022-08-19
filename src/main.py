from typing import IO
from logging.config import dictConfig
import logging
import pathlib
from typing import List
import databases
import sqlalchemy
import pandas as pd
import openpyxl
import io
import psycopg2
from fastapi import FastAPI, File, Header, Depends, UploadFile, HTTPException, status, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import urllib
from db.database import *
import uvicorn
import pymysql
from api.const.constants import *
from
from api.validation import FileValidation

# *** ------------------------------------- *** #



#swaggerUI default route, create instance
#global vars
app = FastAPI(docs_url='/swagger', redoc_url=None)

conn = engine.connect()

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

        file_name_str = str(file.filename).split('.')[0]

        d['file_name'] = file_name_str
        # with open(file_path, 'wb+') as out_pt:
        #     content = await file.read()
        #
        #     out_pt.write(content)
        #     out_pt.close() # close file pointer
        #
        #
        # df = pd.DataFrame()

        content = await file.read()

        df = pd.read_excel(content) # created dataframe object

        # FIXME check if empty, do not add to sql

        if not df.empty:
            df.to_sql(file_name_str, engine, if_exists='replace', index_label='ID')




        # create empty xls/xlsx metadata file (not just binary)

        # df = pd.read_sql(f"SELECT * FROM {file_name_str};", conn)


        return {'data': {
            'is_valid': True,
            'is_empty': df.empty,
            'file_name': file.filename,
            'mime_type': file.content_type
        }}


@app.get('/SendReport/GET/{Type}')
async def get_method(type: ModelGET, start_date, end_date, acceptor_email):
    return {'data':
                {'type': type,
                 'start_date': start_date
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



#ID  |     Segment      |         Country          |  Product  | Discount Band | Units Sold | Manufacturing Price | Sale Price | Gross Sales |     Discounts      |        Sales       |  COGS   |       Profit       |        Date

