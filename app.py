from flask import Flask, render_template,request
from jinja2 import Template


app = Flask(__name__)


@app.route('/' ,methods=['GET', 'POST'])
@app.route('/index.html' ,methods=['GET', 'POST'])
def main():
    lampa1="checked"
    lampa2=""
    daynight=["sun","moon"]
    a=""
    '''if request.method == 'POST':
            if request.form['submit_button'] == 'Do Something':
                a=request.form['szam']'''
    if request.method == 'POST':
        a=request.get_data(as_text=True)
    else: pass
    print(a.split(","))
    return render_template('index.html', lampa1_default=lampa1, lampa2_default=lampa2, daytime=daynight[0])
if __name__ == '__main__':
    app.run(host="0.0.0.0")
