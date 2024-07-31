import redis
import cv2
import json
import base64
import os

redis_client = redis.Redis(host="34.42.25.221",port=6379)
channel = "MNIST IMAGES"

user = ""

image_path = "inputs"

image_name = input("digite um numero desejado: ")
while image_name != "exit":
    image = cv2.imread(f"{image_path}/{image_name}")
    image = cv2.imencode('.jpg', image)[1].tobytes()
    image = base64.b64encode(image).decode('utf-8')

    message = json.dumps({"image_name": image_name, "image": image, "user": user, "Prediction": None})
    redis_client.publish(channel, message)
    
    image_name = input("digite um numero desejado: ")
    