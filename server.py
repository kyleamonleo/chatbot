
from fastapi import FastAPI
from flask import Flask, jsonify, request,send_file, render_template, make_response, redirect, url_for
import bot

# app = FastAPI()
# @app.get("/myBotApi")
# def hello(text=None ):
#     if text is None:
#         text = "hello"

#     return jsonify({"message": ApiChat(text)})


app = Flask(__name__)


# @app.route('/botApi/',  methods=['GET', 'POST'])
# def botChat():
#     # if request.method=='POST':
#     #     dataFromJs = request.form['mydata']
#     #     resp = make_response(json({"response":ApiChat(dataFromJs)}))
#     #     resp.headers['Content-Type'] = "application/json"
#     #     return resp,render_template('index.html', message='')
#     # else:
#     name = request.args.get('name')
#     text = bot.ApiChat(name)
#     return jsonify({"message": text})

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
    app.run(host='127.0.0.1', debug=True, port=5050)
    # chat()
    # ApiChat("hello")

