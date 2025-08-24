def predict(text: str):
    text = text.lower()
    spam = ["긴급","제한","로그인","클릭","쿠폰","당첨","업데이트","취소","인증","비밀번호","http","link","은행"]
    score = sum(k.lower() in text for k in spam)
    label = "SPAM" if score >= 2 else "HAM"
    conf = min(0.95, 0.5 + score*0.1)
    return label, conf

def main():
    print("=== Fraud/Spam Detector (CLI) ===")
    print("Type message and press Enter. Type 'quit' to exit.")
    while True:
        s = input("Message> ").strip()
        if not s: 
            continue
        if s.lower() in ("quit","exit","q"):
            break
        lab, conf = predict(s)
        print(f"Prediction: {lab} (confidence {conf*100:.1f}%)\n")

if __name__=='__main__':
    main()
