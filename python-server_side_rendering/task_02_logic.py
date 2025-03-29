from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    
    with open('items.json', 'r') as file:
        data = json.load(file)

   
    return render_template('items.html', items=data['items'])

if __name__ == '__main__':
    app.run(debug=True)
