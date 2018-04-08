import os
import pytest
from typing import Any
import ardeployer.config as config

def test_config_load() -> None:
    example = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'env.example')
    config.config_load(example)
    assert 'myjob' == config.config_get('JENKINS_JOB')

def test_config_set() -> None:
    config.config_set('JENKINS_JOB', 'hello')
    assert 'hello' == config.config_get('JENKINS_JOB')

def test_config_get() -> None:
    config.config_set('JENKINS_JOB', '')
    assert '' == config.config_get('JENKINS_JOB')
    assert None == config.config_get('JENKINS_NONE')

