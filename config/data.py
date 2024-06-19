import os

from dotenv import load_dotenv

load_dotenv()


class Data:

    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    LOGIN = os.environ["LOGIN"]
    PASSWORD = os.environ["PASSWORD"]

    files = [
        "cat.jpg",
        "dog.png"
    ]
