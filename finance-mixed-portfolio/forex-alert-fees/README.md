# Forex Converter & Fees Comparator (Flask)

Run:
```bash
cd forex-alert-fees
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000 → select pair and amount → Convert.

환율 알리미 & 해외 송금 수수료 비교기

API: 한국은행 환율 API (또는 샘플 데이터)

기능: 실시간 환율 조회, 송금 서비스별 수수료 계산

시각화: Flask + Bootstrap UI

내용: 한국은행/외환 API를 사용해 실시간 환율을 제공하고, 송금 서비스별 수수료 비교.

기술: Flask + 외부 API 연동

포인트: 글로벌 금융 서비스와 연결 → 은행/핀테크 서비스 연계성 강조 가능
