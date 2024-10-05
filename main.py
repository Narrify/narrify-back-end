from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.post('/generate/story')
async def generate_story(request: Request):
    return JSONResponse(content={'story': 'esta sería la respuesta del LLM'})


@app.post('/generate/dialog')
async def generate_dialog(request: Request):
    return JSONResponse(content={'story':'esta sería la respuesta del LLM'})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1")

