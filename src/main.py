from typing import IO
from logging.config import dictConfig
import logging
import pathlib
import json
from typing import List, Union
import databases
import sqlalchemy
import pandas as pd
import io
import re
from fastapi import FastAPI, File, Header, Depends, UploadFile, HTTPException, status, BackgroundTasks, Query, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, Required
import os
import urllib
from db import database as db
from db import services
import uvicorn
import pymysql
from api.const.constants import *
from api.models import models
from api.validation import FileValidation
import datetime
from api.models import services as _service
import xlrd
# *** ------------------------------------- *** #


# swaggerUI default route, create instance
# global vars
app = FastAPI(docs_url='/swagger', redoc_url=None)

conn = db.engine.connect()

# enable Cross origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


# post method decorator
@app.post('/UploadData/POST',
          description='FILE_SIZE must not exceed = 5MB\nFILE_EXTENSION must be either .xlxs or .xls')
async def upload(file: UploadFile = File(...)):
    # async funtion for file uploads

    if await FileValidation(file).validation():  # direct class method call for type and size validation
        file_path = os.path.abspath(os.path.join(os.getcwd(), f'../uploaded_files/{file.filename}'))

        file_name_str = str(file.filename).split('.')[0]

        # d['file_name'] = file_name_str
        # with open(file_path, 'wb+') as out_pt:
        #     content = await file.read()
        #
        #     out_pt.write(content)
        #     out_pt.close() # close file pointer
        #
        #
        # df = pd.DataFrame()

        content = await file.read()

        df = pd.read_excel(content)  # created dataframe object

        # FIXME check if empty, do not add to sql

        if not df.empty:
            df.to_sql("data", db.engine, if_exists='replace', index_label='ID')
        else:
            logging.warning("Your Excel data is empty, please try another file ")

        # create empty xls/xlsx metadata file (not just binary)

        # df = pd.read_sql(f"SELECT * FROM {d['file_name']};", conn)

        data_to_return = {'data': {
            'is_valid': True,
            'is_empty': df.empty,
            'file_name': file.filename,
            'mime_type': file.content_type
        }}

        logging.info(data_to_return)


        return data_to_return


@app.get('/SendReport/GET')
async def get_method(_type: models.ModelGET, start_date: datetime.date, end_date: datetime.date,
                     acceptor_email: Union[List] = Query(default=Required,
                                                                    description='Must have @code.edu.az extension, otherwise emails will fail validation')):

#regex='^[A-Za-z0-9._%+-]+@code.edu.az$'

    garbage_mails = [email for email in acceptor_email if not re.match('^[A-Za-z0-9._%+-]+@code.edu.az$', email)]

    for garbage in garbage_mails:
        acceptor_email.remove(garbage)

    if not acceptor_email:
        raise HTTPException(status_code=400, detail='Valid emails are empty, Please try again')

    if start_date >= end_date:
        raise HTTPException(status_code=400, detail='End date must be greater or equal to start date')

    try:
        df = pd.read_sql("""SELECT * FROM "data"; """, conn)
        # print(df)

        # a = conn.execute("SELECT * FROM DATA;")

    except:
        raise HTTPException(status_code=400,
                            detail="Table doesn't exist. Please upload .xls or .xlsx file in the POST method")

    res: sqlalchemy = services.queries(start_date=start_date,
                                       end_date=end_date,
                                       option=_type)



    data_to_return = {'data':
                    {'type': _type,
                     'start_date': start_date,
                     'end_date': end_date,
                     'successful validated emails': acceptor_email
                     },
                'query res': res.fetchall(),
                'email responses': [None]}


    HTML_table_for_email = _service.HTMLGenerator().generate_html(list_of_tuples= data_to_return['query res'])

    # print(HTML_table_for_email)

    sg_instance = models.SendMail(acceptor_email)


    if acceptor_email:
        data_to_return['email responses'] = sg_instance.send_mail(subject=EMAIL_SUBJECTS[_type], _content=HTML_table_for_email, is_all=True)

        logging.info("Message to these emails have been sent successfully ", acceptor_email)

    else:
        raise HTTPException(status_code=400, detail="Email error. Either emails are empty or not @code.edu.az extensioned")


    # for tup in data_to_return['query res']:
    #     for index, data in enumerate(tup):
    #         print(index, data, '\n', f'Data type: {type(data)}')
    #     print()




    logging.info(data_to_return)


    return data_to_return







if __name__ == '__main__':
    cwd = pathlib.Path(__file__).parent.resolve()

    # print(cwd)

    logging.basicConfig(filename="./src/api/log/logfile.log", level=logging.INFO)

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        reload=True,
        port=8000,
        log_config=f"{cwd}/log.ini",  # initialize log config from log.ini
        log_level="info"  # log level
    )

    #Mail grid api key = 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

# ID  |     Segment      |         Country          |  Product  | Discount Band | Units Sold | Manufacturing Price | Sale Price | Gross Sales |     Discounts      |        Sales       |  COGS   |       Profit       |        Date
