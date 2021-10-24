import os, datetime, io, requests


from telebot.types import Message
from telebot import TeleBot
from PIL import Image


def download_image(tgbot: TeleBot, message: Message, photos: list, user_data: dict):
    filepath = f"media/name1.jpg"
    for img in photos:


        file_info = tgbot.get_file(img.file_id)
        downloaded_file = tgbot.download_file(file_info.file_path)
        fp = io.BytesIO(downloaded_file)
        img = Image.open(fp)
        
        img.save(filepath)
        img.close()

    send_request(user_data, filepath)
    os.remove(filepath)

def send_request(user_data: dict, filepath: str):
    file = {"images": open(filepath,'rb')}

    url = "http://localhost:8000/api/v1/add-point/"
    data = {
        "description": user_data["problem"],
        "latitude": user_data["latitude"],
        "longitude": user_data["longitude"],
    }

    requests.post(
        url=url,
        data=data,
        files=file
    )
