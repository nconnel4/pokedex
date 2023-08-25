from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def ping() -> dict[str, str]:
    return {"message": "pong!"}
