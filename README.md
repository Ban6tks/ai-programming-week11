# 성적 CSV 검증기

## ① 무엇을 하나요 (What · 현재 상태)

성적 CSV 파일을 읽어 유효한 점수 목록과 제외한 행의 기록을 돌려줍니다. 빈 점수, 정수가 아닌 점수, 0~100 범위를 벗어난 점수, 열 개수가 잘못된 행을 제외합니다. 평균과 학점 계산 기능은 아직 포함하지 않습니다.

## ② 왜 만들었나요 (Why)

실제 성적 CSV 파일에는 빈 칸, 범위를 벗어난 점수, 글자로 입력된 점수 등이 섞여 있을 수 있습니다. 이러한 데이터를 그대로 읽으면 프로그램이 중단되거나 잘못된 값이 처리될 수 있으므로, 유효한 값과 제외할 값을 구분하기 위해 만들었습니다.

## ③ 어떻게 쓰나요 (How)

저장소 폴더에서 터미널을 열고 다음 명령을 순서대로 실행합니다.

python --version
python -m pip install --user -U pytest~=7.0 pytest-cov
set PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
python load_scores.py scores.csv

set PYTEST_DISABLE_PLUGIN_AUTOLOAD=1은 옛 Anaconda가 설치된 PC에서 pytest 플러그인 오류를 방지하기 위한 명령입니다. 새 명령 프롬프트를 열 때마다 pytest 실행 전에 한 번 입력합니다.

예상 결과:

- 읽은 줄: 5개
- 건너뛴 줄: 5개

## ④ 어떻게 테스트하나요

다음 명령으로 기본 기능을 테스트합니다.

python -m pytest test_load_scores.py -q

실제 결과:

- 12 passed

AI 비교 실험 파일의 실제 결과:

- test_bug_A.py: 2 failed, 4 passed
- test_bug_B.py: 1 failed, 3 passed

test_bug_A.py와 test_bug_B.py는 find_max 함수의 버그를 확인하기 위한 비교용 원본입니다. find_max 함수가 목록의 마지막 원소를 검사하지 않기 때문에 최댓값이 마지막에 있는 테스트가 실패합니다.

## ⑤ 파일 구성

| 파일 | 하는 일 |
| --- | --- |
| load_scores.py | CSV 파일을 읽어 유효한 점수 목록과 제외한 행의 기록인 (kept, skipped)를 돌려줍니다. |
| scores.csv · empty.csv · weird.csv | 일반 데이터, 빈 파일, 특이한 데이터를 확인하기 위한 예제 CSV 파일입니다. |
| test_load_scores.py | CSV 읽기와 데이터 검증 기능을 확인하는 pytest 테스트입니다. |
| bug3_logic.py · test_bug_A.py · test_bug_B.py | find_max의 버그와 코드·명세 기반 AI 테스트 결과를 비교하는 실험 파일입니다. |
| prompts.txt | AI 실험에 사용하는 프롬프트가 기록된 파일입니다. |

## ⑥ 만든 사람과 AI 사용

- 만든 사람: Ban6tks
- 사용한 AI 도구·모델: GitHub Copilot Chat / 실제 사용한 모델명
- AI에게 도움받은 부분: find_max 함수의 코드와 명세를 바탕으로 pytest 테스트 초안을 작성하는 데 도움을 받았습니다.
- 내가 직접 판단·확인한 부분: AI가 만든 테스트를 직접 저장하고 실행하여 기대값과 실제 반환값을 비교했습니다. 이를 통해 find_max가 목록의 마지막 원소를 검사하지 않는 버그를 확인했습니다.

## 라이선스

MIT License (LICENSE 파일 참고)