import sys
import requests
from typing import Dict
from .response import JobResponse, BuildResponse
from .settings import *

def http_get(url: str) -> requests.Response:
    _timeout = HTTP_TIMEOUT
    return requests.get(url, auth=(JINKENS_USER, JINKENS_PASS), timeout=_timeout)

def get_job() -> JobResponse:
    url = '{}/job/{}/job/master/api/json'.format(JINKENS_URL, JINKENS_JOB)
    res  = http_get(url)
    return JobResponse(res)

def get_build(url: str) -> BuildResponse:
    res = http_get(url)
    return BuildResponse(res)

