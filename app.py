from flask import Flask, render_template,request
import mysql.connector as mariadb
kapdef = ["","","","",""]
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
    datalist=""
    templist=""
    humlist=""
    mariadb_connection = mariadb.connect(user='raspberry', password='pi', database='data')
    cursor = mariadb_connection.cursor()
    cursor.execute("SELECT HOUR(Idopont),MINUTE(IDOPONT),SECOND(IDOPONT),Hofok,Para FROM Hopara WHERE IDOPONT>DATE_SUB(LOCALTIME(), INTERVAL 10 MINUTE) AND SECOND(IDOPONT)=0")
    for Idopont,Idopont2,Idopont3, Hofok, Para in cursor:
        datalist=datalist+"'"+str(Idopont)+":"+str(Idopont2)+"',"
        templist=templist+str(Hofok) + ","
        humlist=humlist+str(Para) + ","
    cursor.close()
    mariadb_connection.close()
    if request.method == 'POST':
        kapcsolok=request.get_data(as_text=True)
    else: pass
    kapcsolok=kapcsolok.split(",")
    print(kapcsolok)
    for i, x in enumerate(kapcsolok):
        if x=="false":
            kapdef[i]=""
        elif x=="true":
            kapdef[i]="checked"
    print(kapdef)
    return render_template('index.html',futauto_default=kapdef[0],futon_default=kapdef[1],riaszt_default=kapdef[2],lampa1_default=kapdef[3],lampa2_default=kapdef[4], daytime=daynight[0], gauge_temp=homerseklet, gauge_hum=para,d_list=datalist, temp_list=templist, hum_list=humlist)
'''if __name__ == '__main__':
    app.run(host="0.0.0.0")'''