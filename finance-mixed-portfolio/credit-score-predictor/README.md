# Credit Score Predictor (CLI)

## Run
```bash
cd credit-score-predictor
python app.py
```
Follow terminal prompts to get probability & advice.

신용 점수 예측 및 관리 서비스

ML 모델: scikit-learn (RandomForest, Logistic Regression)

입력: 소득, 지출, 대출 여부, 신용카드 사용 내역(가상 데이터 생성)

출력: 신용 점수 + 개선 전략 리포트

내용: 사용자의 거래 기록, 소비 패턴(가상 데이터 기반)을 입력하면 머신러닝으로 신용 점수를 예측하고, 개선 전략(카드 사용 줄이기, 대출 상환 등)을 제안.

기술: Python (scikit-learn), Flask, SQLite

포인트: 실제 금융권에서 많이 활용되는 "신용 리스크 관리"를 체험형으로 구현.
