from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return "welcome!"
























if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        'api:app',
        port=8000,
        reload=True,
        host='192.168.0.25'
    )