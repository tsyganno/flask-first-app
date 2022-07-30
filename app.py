from flask import Flask, render_template

from game_of_life import GameOfLife


app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife(25, 25)
    return render_template('index.html')


@app.route('/live/')
def live():
    y = GameOfLife()
    y.form_new_generation()
    return render_template('live.html', x=y.world, counter=y.counter)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
