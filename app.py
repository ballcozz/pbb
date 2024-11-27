from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Fungsi untuk menghitung PBB
def pbb(a, b):
    return math.gcd(a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = pbb(num1, num2)
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
