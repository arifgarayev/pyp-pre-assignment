from fastapi import FastAPI
from typing import Union
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI(docs_url='/swagger', redoc_url=None)


@app.get('/')
def index():
    return {'data': {'name': 'Arif'}}


@app.get('/blog')
def unpb(id: int, email: Union[str]):
    print(type(email))
    return {'data': {'id': id, 'email': email}}

@app.get('/blog/{id}')
def about(id: int):
    pass
    #fetch with id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):

    return {'data': ['1', '2']}


@app.get('/welcome')
def salam(id: int, limit: Optional[int] = None):

    if limit:
        return {'data': {'id': id, 'limited': limit}}

    return {'data': {'id': id}}


class Create(BaseModel):
    title: str
    body: str
    is_published: Optional[bool] = False


@app.post('/create')
def create_sm(request: Create):
    return {'data': f'title is {request.title}'}


if __name__ == "__main__":
    import uvicorn

    pass