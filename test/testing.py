from src.main import app
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests

from fastapi.testclient import TestClient


client = TestClient(app)


def post_xlsx():



    r = requests.post("127.0.0.1:8000/swagger/UploadData/POST", files={"file": ("filename", open('/Users/arifgarayev/Documents/git repos/pyp-pre-assignment/files/example_data.xlsx', "rb"), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')})

    response = client.post(
        "/UploadData/POST", files={"file": ("filename", open('/Users/arifgarayev/Documents/git repos/pyp-pre-assignment/files/example_data.xlsx', "rb"), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
    )

    print(response)


post_xlsx()