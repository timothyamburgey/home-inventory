from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/delete/<int:id>')
def delete(id):
    return "DETETE"

@app.route('/update/<int:id>')
def update(id):
    return "UPDATE"

if __name__ == '__main__':
    app.run(debug=True)