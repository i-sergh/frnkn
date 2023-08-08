from fastapi import FastAPI
from fastapi.responses import JSONResponse
from kafka_utils import get_one, kafka_reconnect

app = FastAPI()



@app.get("/")
def pong():
    return {"ping": "pong"}

@app.get("/one")
def get_one_q():
    return JSONResponse(content=get_one())

@app.get("/reconnect")
def reconect():
    kafka_reconnect()
    return {'Result': 'Success'}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8668)