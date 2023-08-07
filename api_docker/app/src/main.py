from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from random import randint
from time import asctime
import kafka_requests as kreq

app = FastAPI(
    title = 'NIFI'
    )



@app.get('/')
async def start_page():
    return {'ping': 'omnom'}


@app.get('/number')
async def secret_number():
    return  {
        'time': asctime(),
        'number':  randint(0, 1000)
        }

@app.get('/watch')
async def watch():
    response = await kreq.request() 
    return response

@app.get("/reconnect")
async def reconnect():
    result = await kreq.reconnect() 
    if result == 'success':
        return {'Result': 'Successful reconected'}
    else:
        return {'Result': 'Smth go wrong'}

#@app.get("/items/{item_id}")
#def read_root(item_id: str, request: Request):
#    client_host = request.client.host
#    return {"client_host": client_host, "item_id": item_id}


#    
#@app.get('/redirect')
#async def redirect_test(ip, port):    
#    return RedirectResponse('http://' + ip + ':' + port + '/nifi', status_code=303) #/nifi-api/flow/about
 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
