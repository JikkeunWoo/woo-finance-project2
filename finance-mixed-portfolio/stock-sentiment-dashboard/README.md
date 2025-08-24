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

포인트: 금융 데이터와 AI NLP 접목 → 투자 의사결정 보조 도구로 활용. 추후 실시간으로 변하는 개별 주식 종목에 관한 뉴스들에 빠르게 대응할 수 있도록 발전시키면 실효성 있음. 종목 관련 이슈를 일일이 확인하기 어렵거나, 투자에 대해 무지한 사용자들이 시간을 단축하고 번거로움을 줄일 수 있음. 
