import uvicorn # type: ignore

from fastapi import FastAPI # type: ignore
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.docs import get_redoc_html

from api import api_router
from service import Base, engine
# from models import Base

app = FastAPI(
    title="ISI_API"
)

app.include_router(api_router, prefix="/api/v1")

app.mount("/api", StaticFiles(directory="static"), name="api")

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_favicon_url=app.swagger_ui_favicon_url,
        swagger_js_url=app.swagger_ui_js_url,
        swagger_css_url=app.swagger_ui_css_url,
    )

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        print("Startup Migration App ...")
        # drop table
        # await conn.run_sync(Base.metadata.drop_all)
        
        await conn.run_sync(Base.metadata.create_all)
        print("Migrastion Finished ...")
  


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0',  port=9999, reload=True)