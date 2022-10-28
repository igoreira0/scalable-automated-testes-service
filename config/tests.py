from config.common import TestsOptions
from tests.generic_test_error import GenericTestError
from tests.open_google import OpenGoogle
from tests.generic_test import GenericTest

TESTS = {
    TestsOptions.OPEN_GOOGLE.value: OpenGoogle,
    TestsOptions.GENERIC_TEST.value: GenericTest,
    TestsOptions.GENERIC_TEST_ERROR.value: GenericTestError
}