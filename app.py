from flask import Flask, render_template, request, redirect

from game_of_life import GameOfLife


app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def index():
    if request.method == 'POST':
        client_message = str(request.get_data())
        try:
            height = int(client_message[client_message.find('height=') + 7: client_message.find('&')])
            width = int(client_message[client_message.find('width=') + 6:][:-1])
            GameOfLife(height, width)
            return redirect('live')
        except:
            GameOfLife(25, 25)
            return redirect('live')
    return render_template('index.html')


@app.route('/live/')
def live():
    game = GameOfLife()
    if game.counter > 0:
        game.form_new_generation()
        return render_template('live.html', world=game.world, counter=game.counter, old_world=game.old_world)
    else:
        game.counter += 1
        return render_template('live.html', world=game.world, counter=game.counter, old_world=game.old_world)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
