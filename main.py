from flask import Flask, render_template, request
from count_frequency import count_frequency


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods = ['POST', 'GET']) 
def result(): 
    if request.method == 'POST':
        result = request.form
        answer = count_frequency(result['word'])
        return render_template("result.html", answer = answer)


if __name__ == '__main__':
    app.run(debug=True)