from flask import Flask, request, jsonify
import sqlite3
import time
from datetime import datetime


app = Flask(__name__)

# POST endpoint
@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.get_json()
    text = data['text']

    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute("INSERT INTO data (text) VALUES (?)", (text,))

    conn.commit()
    conn.close()

    return jsonify(success=True)


# GET endpoint
@app.route('/get_data', methods=['GET'])
def get_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    c.execute("SELECT * FROM data")
    rows = c.fetchall()

    conn.close()

    data = []
    for row in rows:
        id = row[0]
        text = row[1]
        date = row[2]
        data.append({'id': id, 'text': text, 'date': date})

    return jsonify(data=data)


if __name__ == '__main__':
    app.run()