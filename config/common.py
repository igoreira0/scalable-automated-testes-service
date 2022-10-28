from enum import Enum


class TestsOptions(Enum):
    OPEN_GOOGLE = 1
    GENERIC_TEST = 2
    GENERIC_TEST_ERROR = 3


class TestResult(Enum):
    SUCCESS = 'SUCCESS'
    ERROR = 'ERROR'
