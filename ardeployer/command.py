import os
import sys
import zipfile
from texttable import Texttable
from typing import List, Optional
from .jenkins import *
from .config import config_load

class RunCommand(object):
    @classmethod
    def execute(cls) -> None:
        cls().process()

    def __init__(self) -> None:
        print('Run ...')

    def download(self, url: str, local_file: str) -> None:
        ok, error = download_artifact(url, local_file)
        if ok == False:
            print('Error: {}'.format(error))
            sys.exit(1)

        the_zip = zipfile.ZipFile(local_file)
        ret = the_zip.testzip()
        if ret is not None:
            print('Error: Invlid zip file')
            sys.exit(1)

    def process(self) -> None:
        resJob = get_job()
        builds = [] # type: List[BuildResponse]
        for build in resJob.get_last_builds(5):
            builds.append(get_build(build['api']))

        ids = [] # type: List[int]
        t = Texttable()
        rows = [['Build', 'Time', 'Status', 'Commit Id', 'Commit Message']]
        for b in builds:
            _status = 'success' if b.is_success() else 'failed'
            rows.append([str(b.id()), b.time(), _status, b.commit_id(), b.commit_msg()])
            ids.append(b.id())
        t.add_rows(rows)

        print('The latest build list')
        print(t.draw())

        build_id = input("Please input build_id: ")
        tmp = list(filter(lambda x: x.id() == build_id, builds))
        if len(tmp) < 1:
            print('Error: Unknow build_id {}'.format(build_id))
            sys.exit(2)
        selected = tmp[0]

        artifact_url = selected.artifact_url('artifact/dist/*zip*/dist.zip')
        print('Fetch {} ...'.format(artifact_url))
        self.download(artifact_url, '/tmp/dist.zip')


class ListCommand(object):
    @classmethod
    def execute(cls) -> None:
        cls().process()

    def __init__(self) -> None:
        pass

    def process(self) -> None:
        resJob = get_job()
        builds = [] # type: List[BuildResponse]
        for build in resJob.get_last_builds(5):
            builds.append(get_build(build['api']))

        ids = [] # type: List[int]
        t = Texttable()
        rows = [['Build', 'Time', 'Status', 'Commit Id', 'Commit Message']]
        for b in builds:
            _status = 'success' if b.is_success() else 'failed'
            rows.append([str(b.id()), b.time(), _status, b.commit_id(), b.commit_msg()])
            ids.append(b.id())
        t.add_rows(rows)

        print('The latest build list')
        print(t.draw())


