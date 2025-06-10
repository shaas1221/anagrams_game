from flask import Flask, render_template, request
import json, random

app = Flask(__name__)

# تحميل بيانات الآيات
with open('sentences.json', 'r', encoding='utf-8') as f:
    data = json.load(f)['sentences']

@app.route('/')
def index():
    entry = random.choice(data)
    reference = entry['reference']
    phrase = entry['phrase']
    # خلط أحرف العبارة
    scrambled_list = random.sample(list(phrase), len(phrase))
    return render_template('index.html',
                           reference=reference,
                           scrambled_list=scrambled_list,
                           phrase=phrase)

@app.route('/check', methods=['POST'])
def check():
    user_answer = request.form['answer'].strip()
    original = request.form['original']
    correct = (user_answer == original)
    reference = request.form['reference']
    return render_template('result.html',
                           correct=correct,
                           original=original,
                           reference=reference)

if __name__ == '__main__':
    app.run(debug=True)
