from flask import Flask, render_template_string, request
import pandas as pd

app = Flask(__name__)
SERVICES = {"BankA":{"fee_pct":0.5,"flat":3000},"BankB":{"fee_pct":0.3,"flat":5000},"FintechX":{"fee_pct":0.2,"flat":2000}}

TPL = """
<h2>🌍 Forex Converter & Fees Comparator</h2>
<form method='POST'>
  Amount: <input type='number' name='amount' value='1000' step='0.01'>
  From: <select name='base'><option>USD</option><option>KRW</option><option>EUR</option></select>
  To: <select name='quote'><option>KRW</option><option>USD</option><option>EUR</option></select>
  <button>Convert</button>
</form>
{% if res %}
<p>{{res.amount}} {{res.base}} → rate {{res.rate}} {{res.quote}} ⇒ {{res.exchanged}} {{res.quote}}</p>
<ul>{% for r in comp %}<li>{{r.service}} – Receive {{r.received}} (fee {{r.est_fee}})</li>{% endfor %}</ul>
{% endif %}
"""

def get_rate(base, quote):
    df = pd.read_csv("rates_sample.csv")
    row = df[(df.base==base) & (df.quote==quote)]
    if row.empty: return None
    return float(row.iloc[0]["rate"])

@app.route("/", methods=["GET","POST"])
def index():
    res=None; comp=[]
    if request.method=="POST":
        amount=float(request.form["amount"] or 0)
        base=request.form["base"]; quote=request.form["quote"]
        rate = get_rate(base, quote)
        if rate:
            exchanged = amount*rate
            for name,fee in SERVICES.items():
                fee_amt = exchanged*(fee["fee_pct"]/100.0) + fee["flat"]
                comp.append({"service":name,"received":round(exchanged-fee_amt,2),"est_fee":round(fee_amt,2)})
            comp = sorted(comp, key=lambda x: x["received"], reverse=True)
            res={"base":base,"quote":quote,"rate":rate,"amount":amount,"exchanged":round(exchanged,2)}
    return render_template_string(TPL, res=res, comp=comp)

if __name__=="__main__":
    app.run(debug=True)
