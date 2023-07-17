from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from random import randint
from time import asctime

app = FastAPI(
    title = 'NIFI'
    )



@app.get('/')
async def start_page():
    return {'ping': 'pong'}


@app.get('/number')
async def secret_number():
    return  {
        'time': asctime(),
        'number':  randint(0, 1000)
        }
    
@app.get('/redirect')
async def redirect_test(ip, port):
    
    return RedirectResponse('http://' + ip + ':' + port + '/nifi', status_code=303) #/nifi-api/flow/about
 