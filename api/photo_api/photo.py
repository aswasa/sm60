from fastapi import APIRouter, UploadFile, File
import random
from typing import Union, Optional

photo_api = APIRouter(prefix="/file",
                      tags=["Работа с файлами"])


ALLOWED_EXTENSIONS= ["jpg", "jpeg", "heic", "png"]



@photo_api.post("/add-photo")
async def add_photo(post_id: int | None = None,
                    user_id: int | None = None,
                    photo_file: UploadFile = File(...)):
    file_id = random.randint(1, 1000000000000000)
    info_id = post_id if post_id else user_id
    if photo_file:
        extension = photo_file.filename.split(".")[-1]
        if extension in ALLOWED_EXTENSIONS:
            photo_in_project = open(f"database/photos/photo_{file_id}_{info_id}.{extension}",
                                    "xb")
            try:
                users_photo = await photo_file.read()
                photo_in_project.write(users_photo)
            except Exception as error:
                return {"status": 0, "message": "try again" + f"\n {error}"}
            finally:
                photo_in_project.close()
                return {"status": 1, "message": "ok"}

# @photo_api.post("/add-text")
# async def add_text(name: str,text: str):
#     chat = open("database/file.txt", "at")
#     chat.write(f"{name}: {text}\n")
#     chat.close()