from flask import Flask, render_template,request



'''def GetTemp():
    temp=0
    dht_device = adafruit_dht.DHT11(board.D4)
    temp = dht_device.temperature
    return temp;
def GetHum():
    hum=0
    dht_device = adafruit_dht.DHT11(board.D4)
    hum = dht_device.humidity
    return hum;'''
app = Flask(__name__)
@app.route('/' ,methods=['GET', 'POST'])
@app.route('/index.html' ,methods=['GET', 'POST'])
def main():
    daynight=["sun","moon"]
    homerseklet=0
    para=0
    kapcsolok=""
    templist=
    humlist=
    if request.method == 'POST':
        kapcsolok=request.get_data(as_text=True)
    else: pass
    kapcsolok=kapcsolok.split(",")
    print(kapcsolok)
    return render_template('index.html', daytime=daynight[0], gauge_temp=homerseklet, gauge_hum=para)
if __name__ == '__main__':
    app.run(host="0.0.0.0")

