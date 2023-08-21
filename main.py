from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data':'list of blogs'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'list of unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data':{'blog':id}}

@app.get('/blog/{id}/comments')
def comment(id:int):
    return {'data':{'comment1','comment2'}}

@app.get('/about')
def index():
    return {'data':'about page'}