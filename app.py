from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

items = []

@app.route('/')
def home():
    today = datetime.now()
    day = today.strftime("%A, %B %d %Y")
    return render_template('list.html', newListItem=items, day=day)

@app.route('/', methods=['POST'])
def add_item():
    item = request.form['newItem']
    items.append(item)
    return redirect('/')

if __name__ == 'main':
    app.run(port=3000)