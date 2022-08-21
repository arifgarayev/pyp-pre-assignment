from typing import Union
from pydantic import BaseModel
from enum import Enum, IntEnum
import sendgrid
import os
from sendgrid.helpers.mail import *
from api.const import constants
from fastapi import FastAPI, HTTPException, status
import json

class ModelGET(IntEnum, Enum):
    one = 1
    two = 2
    three = 3
    four = 4


class UserPOST(BaseModel):
    file_name: str

class SendMail():
    def __init__(self, list_of_mails):
        self.sg = sendgrid.SendGridAPIClient(api_key=constants.SENDGRRID_API_KEY)
        self.list_of_mails = list_of_mails
        self.from_email = Email(constants.FROM_EMAIL)

    def send_mail(self, subject, _content, is_all=None):

        if is_all:
            for to_email in self.list_of_mails:
                to_mail = To(to_email)
                content = Content("text/html", _content)

                mm = Mail(self.from_email, to_mail, subject, content)

                response = self.sg.client.mail.send.post(request_body=mm.get())


        if response:


            return {'SendGrid response':
                        {
                            'list of emails successfully sent': self.list_of_mails,
                            'status code': response.status_code,
                            'response body': response.body,
                            'response headers': response.headers
                        }}

        else:
            raise HTTPException(status_code=400,
                            detail="Email issue")

