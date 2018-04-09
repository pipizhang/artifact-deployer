import os
import sys
import requests
from typing import Dict, Tuple
from .response import JobResponse, BuildResponse
from .config import *

def http_get(url: str) -> requests.Response:
    return requests.get(url, auth=(config_get('JENKINS_USER'), config_get('JENKINS_PASS')), timeout=config_get('HTTP_TIMEOUT'))

def http_download(url: str) -> requests.Response:
    return requests.get(url, auth=(config_get('JENKINS_USER'), config_get('JENKINS_PASS')), timeout=config_get('HTTP_TIMEOUT'), stream=True)

def get_job() -> JobResponse:
    url = '{}/job/{}/job/master/api/json'.format(config_get('JENKINS_URL'), config_get('JENKINS_JOB'))
    res  = http_get(url)
    return JobResponse(res)

def get_build(url: str) -> BuildResponse:
    res = http_get(url)
    return BuildResponse(res)

def download_artifact(url: str, local_file: str) -> Tuple[bool, str]:
    if os.path.isfile(local_file):
        try:
            os.remove(local_file)
        except OSError as e:
            return False, str(e)

    r = http_download(url)
    with open(local_file, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

    if os.path.isfile(local_file):
        return True, ""
    else:
        return False, 'Failed to download file {}'.format(url)

