import uvicorn

if __name__ == "__main__":
    uvicorn.run("load:app", host="0.0.0.0", port=8070, reload=True)
