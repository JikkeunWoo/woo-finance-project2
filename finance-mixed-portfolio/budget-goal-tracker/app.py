from flask import Flask, render_template_string, request
import sqlite3

DB="budget.db"
app = Flask(__name__)

def init_db():
    con = sqlite3.connect(DB); c=con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS budget (month TEXT PRIMARY KEY, limit_amt REAL)")
    c.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, category TEXT, amount REAL)")
    con.commit(); con.close()

TPL = """
<h2>💸 Budget Goal Tracker</h2>
<form method='POST'>
  <input type='hidden' name='form' value='budget'>
  Month (YYYY-MM): <input name='month' value='2025-08'>
  Limit (KRW): <input name='limit_amt' value='1500000'>
  <button>Save Budget</button>
</form><br>
<form method='POST'>
  <input type='hidden' name='form' value='expense'>
  Date: <input type='date' name='date'>
  Category: <input name='category'>
  Amount: <input name='amount' type='number' step='0.01'>
  <button>Add Expense</button>
</form>
{% if msg %}<p><b>{{msg}}</b></p>{% endif %}
{% if prog %}
  <p>{{prog.month}} – Spent {{prog.spent}} / Limit {{prog.limit}} ({{prog.rate}}%)</p>
{% endif %}
<ul>{% for cat,amt in bycat %}<li>{{cat}}: {{amt}}</li>{% endfor %}</ul>
"""

@app.route("/", methods=["GET","POST"])
def index():
    init_db(); msg=None
    if request.method=="POST":
        f = request.form.get("form")
        con = sqlite3.connect(DB); c=con.cursor()
        if f=="budget":
            c.execute("REPLACE INTO budget (month, limit_amt) VALUES (?,?)",
                      (request.form["month"], float(request.form["limit_amt"])))
            msg="Budget saved."
        elif f=="expense":
            c.execute("INSERT INTO expenses (date, category, amount) VALUES (?,?,?)",
                      (request.form["date"], request.form["category"], float(request.form["amount"])))
            msg="Expense added."
        con.commit(); con.close()
    con = sqlite3.connect(DB); c=con.cursor()
    c.execute("SELECT month, limit_amt FROM budget"); bud=c.fetchone()
    c.execute("SELECT SUM(amount) FROM expenses"); total=c.fetchone()[0] or 0
    c.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category"); bycat=c.fetchall()
    con.close()
    prog=None
    if bud:
        m, lim = bud; rate = round(total/lim*100,1) if lim else 0
        prog={"month":m,"limit":lim,"spent":total,"rate":rate}
    return render_template_string(TPL, msg=msg, prog=prog, bycat=bycat)

if __name__=="__main__":
    app.run(debug=True)
