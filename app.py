
import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/teste')
def index():
    return render_template('testejson.html')


@app.route('/teste2')
def index2():
    return render_template('testejson2.html')


@app.route('/api/say_name2', methods=['POST'])
def say_name2():
    first = request.form['first_name']
    email = request.form['email']
    print(first)
    print(email)    
    return jsonify(first_name=first)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

