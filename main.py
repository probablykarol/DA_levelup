from fastapi import FastAPI 
import hashlib

app = FastAPI()

@app.get('/')
def root():
    return {"message": "Hello world!"}

@app.get('/method')
def method_func():
    return{"method": "GET"}


@app.get('/auth')
def auth_func(password = '', password_hash = ''):
    if hashlib.sha512(password.encode()).hexdigest() == password_hash:
        status_code = 204
    else:
        status_code = 401



