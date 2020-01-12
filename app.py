from flask import Flask, render_template,request


'''def GetTemp():
    temp=0
    dht_device = adafruit_dht.DHT11()
    temp = dht_device.temperature
    return temp;'''
'''def GetHum():
    hum=0
    dht_device = adafruit_dht.DHT11()
    hum = dht_device.humidity
    return hum;'''

app = Flask(__name__)


@app.route('/' ,methods=['GET', 'POST'])
@app.route('/index.html' ,methods=['GET', 'POST'])
def main():
    lampa1="checked"
    lampa2=""
    daynight=["sun","moon"]
    homerseklet=30
    para=55
    a=""
    if request.method == 'POST':
        a=request.get_data(as_text=True)
    else: pass
    print(a.split(","))
    return render_template('index.html',lampa1_default=lampa1, lampa2_default=lampa2, daytime=daynight[0], gauge_temp=homerseklet, gauge_hum=para)
if __name__ == '__main__':
    app.run(host="0.0.0.0")
