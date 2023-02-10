from uvicorn.main import run

if __name__ == "__main__":
    run('main:app', port=8000, reload=True)
