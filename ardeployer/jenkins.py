import sys
import requests
from typing import Dict
from .response import JobResponse, BuildResponse
from .config import *

def http_get(url: str) -> requests.Response:
    return requests.get(url, auth=(config_get('JENKINS_USER'), config_get('JENKINS_PASS')), timeout=config_get('HTTP_TIMEOUT'))

def get_job() -> JobResponse:
    url = '{}/job/{}/job/master/api/json'.format(config_get('JENKINS_URL'), config_get('JENKINS_JOB'))
    res  = http_get(url)
    return JobResponse(res)

def get_build(url: str) -> BuildResponse:
    res = http_get(url)
    return BuildResponse(res)

