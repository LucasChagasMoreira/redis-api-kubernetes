import redis
from utils.pubsub_utils import get_module_logger
import os

def main():    
    redis_host = os.getenv("REDIS_HOST")
    redis_port = int(os.getenv("REDIS_PORT", 6379))  # A porta deve ser um inteiro

    redis_client = redis.Redis(host=redis_host, port=redis_port)
    channel = 'Prediction'

    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)

    logger = get_module_logger()

    logger.info(f"Subscribed in {channel} Channel")

    for message in pubsub.listen():
        if message['type'] == 'message':
            prediction = message['data']
            logger.info(f"{prediction}\n")


if __name__ == "__main__":
    main()
