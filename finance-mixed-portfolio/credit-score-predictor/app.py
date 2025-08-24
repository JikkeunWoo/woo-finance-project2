# CLI Credit Score Predictor
def ask_float(prompt, default=None):
    while True:
        try:
            raw = input(f"{prompt}" + (f" [{default}]" if default is not None else "") + ": ").strip()
            if not raw and default is not None:
                return float(default)
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("=== Credit Score Predictor (CLI) ===")
    income = ask_float("Monthly income (KRW)", 3500000)
    expense = ask_float("Monthly expense (KRW)", 2200000)
    loans = ask_float("Active loans count", 1)
    late = ask_float("Late payments (12m)", 0)
    cards = ask_float("Credit cards count", 2)

    util = expense / (income + 1.0)
    score = 0.65 + (income - expense)/10_000_000 - loans*0.05 - late*0.08 - max(0, util-0.6)*0.4 - max(0, cards-4)*0.02
    prob = max(0.0, min(1.0, score))
    print(f"Predicted Good Credit Probability: {prob*100:.1f}%")

    tips = []
    if util > 0.6: tips.append("Reduce expenses to keep utilization ≤ 60%.")
    if loans >= 1: tips.append("Repay/refinance to lower DSR.")
    if late >= 1: tips.append("Enable auto-pay to prevent delinquencies.")
    if cards >= 4: tips.append("Close unused cards to simplify credit lines.")
    if income - expense < 500000: tips.append("Increase savings buffer.")
    print("Advice:", "; ".join(tips) if tips else "You're in good shape.")

if __name__ == "__main__":
    main()
