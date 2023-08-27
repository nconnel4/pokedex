from fastapi import FastAPI

from app.core.config import Settings

app = FastAPI()

settings = Settings()


@app.get("/")
async def ping() -> dict[str, str]:
    print(settings.database_url)
    return {"message": "pong!"}
