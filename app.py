from flask import Flask, render_template,request
from jinja2 import Template


app = Flask(__name__)


@app.route('/' ,methods=['GET', 'POST'])
def hello_world():
    '''if request.method == 'POST':
            if request.form['submit_button'] == 'Do Something':
                a=request.form['szam']'''
    return render_template('index.html')
if __name__ == '__main__':
    app.run()
