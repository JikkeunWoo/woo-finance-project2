from flask import Flask, render_template_string, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

samples = ["어닝 서프라이즈로 주가 급등","신제품 흥행 매출 확대","대규모 수주 성공",
           "원가 상승과 수요 둔화로 실적 악화","규제 강화 우려로 투자심리 위축","리콜 이슈 발생"]
labels = [1,1,1,0,0,0]
vec = TfidfVectorizer(max_features=500, ngram_range=(1,2))
X = vec.fit_transform(samples)
clf = LogisticRegression(max_iter=300).fit(X, labels)

TPL = """
<h2>📈 Stock Sentiment Dashboard</h2>
<form method='POST'>
  <textarea name='lines' rows='8' cols='80'>어닝 서프라이즈로 주가 급등
원가 상승과 수요 둔화로 실적 악화</textarea><br><br>
  <button type='submit'>Analyze</button>
</form>
{% if stats %}
  <p>Total {{stats.total}} / Positive {{stats.pos}} / Negative {{stats.neg}}</p>
  <ul>{% for line,lab in items %}<li>[{{"긍정" if lab else "부정"}}] {{line}}</li>{% endfor %}</ul>
{% endif %}
"""

@app.route("/", methods=["GET","POST"])
def index():
    stats=None; items=[]
    if request.method=="POST":
        lines = [l.strip() for l in request.form.get("lines","").split("\n") if l.strip()]
        if lines:
            Xq = vec.transform(lines)
            pred = clf.predict(Xq)
            pos = int((pred==1).sum()); neg = len(pred)-pos
            stats={"total":len(lines),"pos":pos,"neg":neg}
            items = list(zip(lines, pred.tolist()))
    return render_template_string(TPL, stats=stats, items=items)

if __name__=="__main__":
    app.run(debug=True)
