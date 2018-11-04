from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def function(name=None):
    return render_template('profile.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)