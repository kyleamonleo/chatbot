
from flask import Flask, jsonify, request,send_file, render_template, make_response, redirect, url_for
import bot


app = Flask(__name__)


@app.route('/bot', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        txt = request.form['nm']

        bot_said =bot.ApiChat(txt)
        return render_template('bot.html', name=bot_said)

    else:
        return render_template('bot.html')

@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/home')
def Home():
    return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


