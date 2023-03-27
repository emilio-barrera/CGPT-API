import os
from dotenv import load_dotenv

class env_reader():
    def __init__(self) -> None:
        load_dotenv()

    def get_var(self, name: str)->str:
        try:
            return os.getenv(name)
        except:
            return ""