import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
# gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
