# from fastapi import APIRouter
# text_api = APIRouter(prefix = "/texts",
#                       tags = ["Текст"])
# @text_api.post("/add-text")
# async def add_text(username: str,
#                    text: str):
#     text_in_project = open(f"database/photos/texts.txt", "at")
#     user_text = f"{username}: {text}\n"
#     text_in_project.write(user_text)