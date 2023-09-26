from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")

def index():
    name = "zoba"
    return render_template('zoba.html', zoba=name)

if __name__ == '__main__':
    app.run(debug=True)
