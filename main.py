from fastapi import  FastAPI
from api.photo_api.photo import photo_api
from texts import text_api

app=FastAPI(docs_url='/')

app.include_router(photo_api)
app.include_router(text_api)
