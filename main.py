# -*- coding: utf-8 -*-
from flask import Flask,render_template,request,jsonify
from Rxclaim_ChatBot_Test import RxClaim_chatbot


app = Flask(__name__)

r = RxClaim_chatbot()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process') 
def process():
    NewMessage = request.args.get('a', 'default', type=str) 
    NewMessage = r.bot_reply(NewMessage)
    return jsonify(result = NewMessage)
      

if __name__ == '__main__':
    app.run(debug = True)


