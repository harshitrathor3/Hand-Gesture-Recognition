from flask import Flask, render_template

from file import run

app = Flask(__name__, static_folder='templates')


@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/new')
def AppLaunch():
    run()
    return render_template('index.html')

    # return render_template('new.html')


if __name__=='__main__':
    app.run(debug=True)
