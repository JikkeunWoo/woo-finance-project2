# Fraud/Spam Message Detector (CLI)

Run:
```bash
cd fraud-detection-app
python app.py
```
Type a message (e.g., '긴급 로그인 링크 클릭'), see prediction & confidence. `quit` to exit.

금융 사기(스팸) 메시지 탐지기

데이터: SMS 스팸 데이터셋 (UCI ML Repository 활용)

모델: Naive Bayes / SVM 텍스트 분류

출력: 입력 문장이 "정상" / "사기" 판별

내용: 은행 사칭 스팸 문자/메일 데이터를 학습해 의심 메시지를 걸러주는 서비스.

기술: Python (sklearn, NLP), Flask

포인트: 실제 금융권 보안 분야(피싱/스미싱 탐지)와 직결되는 주제. 데이터를 쌓고, 정보를 추가하며 개선 및 발전 가능.

