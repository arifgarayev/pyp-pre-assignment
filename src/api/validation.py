from src.api.const.constants import *
from fastapi import FastAPI, File, Header, Depends, UploadFile, HTTPException


class FileValidation:
    def __init__(self, file_object):
        self.max_file_size: int = MAX_FILE_SIZE
        self.mime_types: tuple = MIME_TYPES
        self.file_object: UploadFile = file_object


    async def validation(self):

        if self.file_object.content_type not in self.mime_types:
            raise HTTPException(
                status_code=400,
                detail='please upload .xlsx or .xls'
            )

        if MAX_FILE_SIZE:
            size = await self.file_object.read()

            if len(size) > self.max_file_size:
                raise HTTPException(
                    status_code=413,
                    detail='file size exceeds 5MB'
                )

        await self.file_object.seek(0)

        return self.file_object