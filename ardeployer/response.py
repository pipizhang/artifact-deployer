import datetime
import json
import pprint
import requests
from typing import Any, Dict, List

class JsonResponse(object):
    def __init__(self, response: requests.Response) -> None:
        self.response = response
        self.json = response.json()

    def __str__(self) -> str:
        content =  json.dumps(self.json)
        return pprint.pformat(content, width=160)

    def is_200(self) -> bool:
        return self.response.status_code == 200

class JobResponse(JsonResponse):
    def has_builds(self) -> bool:
        if len(self.json) and 'builds' in self.json and len(self.json['builds']):
            return True
        else:
            return False

    def get_last_builds(self, n: int) -> List[Dict]:
        arr = self.json['builds'][:n]
        for build in arr:
            build['api'] = '{}api/json'.format(build['url'])
        return arr

    def get_last_builds_api(self, n: int) -> List[str]:
        return list(map(lambda v: v['api'],  self.get_last_builds(n)))

class BuildResponse(JsonResponse):
    def is_success(self) -> bool:
        return self.json['result'].upper() == 'SUCCESS'

    def id(self) -> int:
        return self.json['id']

    def time(self) -> str:
        tstamp = self.json['timestamp'] / 1000
        return datetime.datetime.fromtimestamp(tstamp).strftime('%Y-%m-%d %H:%M:%S')

    def commit_id(self) -> str:
        return self.json['changeSets'][0]['items'][0]['commitId'][:9]

    def commit_msg(self) -> str:
        return self.json['changeSets'][0]['items'][0]['msg']


