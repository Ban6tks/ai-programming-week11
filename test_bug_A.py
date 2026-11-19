import pytest

from bug3_logic import find_max


@pytest.mark.parametrize(
    ("scores", "expected"),
    [
        ([9, 3, 5], 9),       # 최댓값이 첫 번째
        ([1, 10, 3], 10),     # 최댓값이 중간
        ([1, 3, 10], 10),     # 최댓값이 마지막
        ([7], 7),             # 원소 하나
        ([-8, -2, -5], -2),   # 음수 점수
        ([2, 5], 5),          # 원소 두 개
    ],
)
def test_find_max(scores, expected):
    assert find_max(scores) == expected