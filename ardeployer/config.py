import os
from typing import Any
from dotenv import load_dotenv

settings = {
        'JINKENS_URL': '',
        'JINKENS_JOB': '',
        'JINKENS_USER': '',
        'JINKENS_PASS': '',
        'HTTP_TIMEOUT': 15
}

def config_load(file_path: str=None) -> None:
    if file_path != None:
        load_dotenv(dotenv_path=file_path)
    else:
        load_dotenv()
    key = '' # type: str
    for key in settings.keys():
        if os.getenv(key) != None:
            settings[key] = os.getenv(key)

def config_set(key: str, val: Any) -> None:
    if key in settings.keys():
        settings[key] = val

def config_get(key: str) -> Any:
    if key in settings.keys():
        return settings[key]
    else:
        return None


