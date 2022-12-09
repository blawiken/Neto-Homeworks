import pytest
from task_1 import filter_geo_logs
from task_2 import get_uniqs
from task_3 import quaries


def test_task_1():
    res = filter_geo_logs()
    assert type(res) == list


@pytest.mark.parametrize(
    'ids, etalon',
    [(
        {
            'user1': [10, 10, 20],
            'user2': [20, 30]
        },
        [10, 20, 30]
    ),
    (
        {
            'user1': [100, 2000, 1],
            'user2': [1, 100]
        },
        [100, 2000, 1]
    )]
)
def test_task_2(ids, etalon):
    res = get_uniqs(ids)
    assert res == etalon


def test_task_3():
    res = quaries()
    assert res['percent'] > 0