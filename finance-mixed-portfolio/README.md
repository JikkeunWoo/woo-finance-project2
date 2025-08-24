# 💰 Finance Mixed Portfolio

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)](https://www.python.org/)
[![Framework: Flask](https://img.shields.io/badge/Framework-Flask-lightgrey)](https://flask.palletsprojects.com/)

Mix of Flask web apps and CLI tools. See each folder for usage.
1. 가계부 기반 금융 목표 관리 앱

내용: 사용자가 매일 지출을 기록하면, 예산 대비 지출 상태와 절약 목표 달성률을 알려줌.

기술: Flask, SQLite, Chart.js 시각화

포인트: 취업 자기소개서에서 “생활 밀착형 금융 서비스 기획 경험” 강조 가능.

2. 신용 점수 예측 및 관리 서비스

내용: 사용자의 거래 기록, 소비 패턴(가상 데이터 기반)을 입력하면 머신러닝으로 신용 점수를 예측하고, 개선 전략(카드 사용 줄이기, 대출 상환 등)을 제안.

기술: Python (scikit-learn), Flask, SQLite

포인트: 실제 금융권에서 많이 활용되는 "신용 리스크 관리"를 체험형으로 구현.

3. 환율 알리미 & 해외 송금 수수료 비교기

내용: 한국은행/외환 API를 사용해 실시간 환율을 제공하고, 송금 서비스별 수수료 비교.

기술: Flask + 외부 API 연동

포인트: 글로벌 금융 서비스와 연결 → 은행/핀테크 서비스 연계성 강조 가능.

4. 금융 사기(스팸) 메시지 탐지기

내용: 은행 사칭 스팸 문자/메일 데이터를 학습해 의심 메시지를 걸러주는 서비스.

기술: Python (sklearn, NLP), Flask

포인트: 실제 금융권 보안 분야(피싱/스미싱 탐지)와 직결되는 주제.

5. 주식 종목 감성 분석 대시보드

내용: 네이버/구글 뉴스 API에서 주식 종목 관련 뉴스 수집 후, HuggingFace 감성 분석 모델로 긍정/부정 비율을 시각화.

기술: Flask + Plotly/Dash, Transformers

포인트: 금융 데이터와 AI NLP 접목 → 투자 의사결정 보조 도구.


