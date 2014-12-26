import inspect
import os
import pytest

rootdir = os.path.dirname(__file__)


def pytest_pycollect_makeitem(collector, name, obj):
    if (inspect.isclass(obj) and obj.__name__ == 'Solution' and
            hasattr(obj, 'tests')):
        # The solution will be the only defined method on the class
        attrname, _ = inspect.getmembers(obj, inspect.ismethod)[0]

        @pytest.mark.parametrize(['input', 'expected'], obj.tests)
        def test(input, expected):
            assert getattr(obj(), attrname)(input) == expected

        return list(collector._genfunctions('test_' + obj.__module__, test))

