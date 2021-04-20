from fastapi import FastAPI 
import hashlib

app = FastAPI()

@app.get('/')
def root():
    return {"message": "Hello world!"}

@app.get('/method',status_code = 200)
def method_get():
    return{"method": "GET"}

@app.post('/method',status_code = 201)
def method_post():
    return{"method": "POST"}

@app.delete('/method',status_code = 200)
def method_delete():
    return {"method": "DELETE"}

@app.options('/method', status_code = 200)
def method_options():
    return {"method": "OPTIONS"}


@app.get('/auth')
def auth_func(password = '', password_hash = ''):
    if hashlib.sha512(password.encode()).hexdigest() == password_hash:
        status_code = 204
    else:
        status_code = 401



