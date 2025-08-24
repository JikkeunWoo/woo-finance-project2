# Stock Sentiment Dashboard (Flask)
Run:
```bash
cd stock-sentiment-dashboard
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000, paste headlines, click Analyze.

주식 종목 감성 분석 대시보드

데이터: 주식 관련 뉴스 (샘플 크롤링 or API 모듈)

모델: HuggingFace distilbert-base-uncased-finetuned-sst-2-english

출력: 긍/부정 비율 차트 시각화

내용: 네이버/구글 뉴스 API에서 주식 종목 관련 뉴스 수집 후, HuggingFace 감성 분석 모델로 긍정/부정 비율을 시각화.

기술: Flask + Plotly/Dash, Transformers

포인트: 금융 데이터와 AI NLP 접목 → 투자 의사결정 보조 도구.
