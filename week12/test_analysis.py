import pandas as pd

from analysis import 정제, 반별평균


scores_df = pd.read_csv("scores_2026.csv")
mini_df = pd.read_csv("mini.csv")

cleaned_scores = 정제(scores_df)
cleaned_mini = 정제(mini_df)


def test_scores_2026_has_100_cleaned_rows():
    assert len(cleaned_scores) == 100


def test_cleaned_scores_have_only_two_classes():
    assert set(cleaned_scores["반"].unique()) == {"1반", "2반"}


def test_class_score_totals_equal_overall_total():
    class_totals = cleaned_scores.groupby("반")["점수"].sum()
    assert class_totals.sum() == cleaned_scores["점수"].sum()


def test_mini_first_class_average_is_80():
    assert 반별평균(cleaned_mini)["1반"] == 80.0