import uvicorn # type: ignore

from fastapi import FastAPI # type: ignore

from api import api_router
from service import Base, engine
from models import Base

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        print("Startup Migration App ...")
        # drop table
        await conn.run_sync(Base.metadata.drop_all)
        
        await conn.run_sync(Base.metadata.create_all)
        print("Migrastion Finished ...")
    


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0',  port=9999)