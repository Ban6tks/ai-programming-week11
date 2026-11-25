import pandas as pd


def 정제(df):
    # 원본을 보존하기 위해 복사본으로 작업한다.
    df = df.copy()
    print(f"시작 행 수: {len(df)}")

    # 점수가 비어 있는 행을 삭제한다.
    df = df.dropna(subset=["점수"])
    print(f"점수 결측 행 삭제 후: {len(df)}")

    # 모든 열의 값이 같은 중복 행을 제거한다.
    df = df.drop_duplicates()
    print(f"중복 행 제거 후: {len(df)}")

    # 반과 과목 값의 앞뒤 공백을 제거한다.
    df["반"] = df["반"].str.strip()
    df["과목"] = df["과목"].str.strip()
    print(f"공백 제거 후: {len(df)}")

    # 점수가 0 미만이거나 100 초과인 행을 삭제한다.
    df = df[df["점수"].between(0, 100)]
    print(f"점수 범위 정제 후: {len(df)}")

    return df


df = 정제(pd.read_csv("scores_2026.csv"))

수학_df = df[df["과목"] == "수학"]
print(len(수학_df))

응용_df = df[(df["반"] == "1반") & (df["점수"] >= 90)]



반별_점수평균 = df.groupby("반")["점수"].mean()
print("반별 점수 평균:")
print(반별_점수평균)

과목_반별_점수평균 = df.groupby(["과목", "반"])["점수"].mean()
print("과목·반별 점수 평균:")
print(과목_반별_점수평균)





def 반별평균(df):
    표 = (
        df.groupby("반")["점수"]
        .agg(["count", "mean", "median", "max"])
        .rename(columns={
            "count": "개수",
            "mean": "평균",
            "median": "중앙값",
            "max": "최댓값",
        })
        .round(2)
    )

    print(표)
    return 표["평균"]


반별평균(df)


# 그룹별 점수 합계의 합과 전체 점수 합계 비교
print(df.groupby("반")["점수"].sum().sum())
print(df["점수"].sum())

# 그룹별 개수의 합과 전체 행 수 비교
print(df.groupby("반")["점수"].count().sum())
print(len(df))

# 1반 수학 점수 스팟 체크
print(df[(df["반"] == "1반") & (df["과목"] == "수학")]["점수"])

미니 = 정제(pd.read_csv("mini.csv"))
print(반별평균(미니))