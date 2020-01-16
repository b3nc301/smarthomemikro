from flask import Flask, render_template,request
import mysql.connector as mariadb
import board
import adafruit_dht
import RPi.GPIO as GPIO
from time import sleep
from threading import Thread
import smtplib, ssl

'''E-mail küldés'''
port = 465
password = "'''password'''"
smtp_server = "smtp.gmail.com"
sender_email = "'''sender mail'''"
receiver_email = ["'''receiver1'''","'''receiver2'''"]
message = """\
Subject: RIASZTAS!

Figyelem! Aktiv riasztas mellett tevekenyseget eszlelt a rendszer!."""


kapdef = ["","","","",""]
tempset=25

'''GPIO set'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
'''Lámpakezelő függvények'''
def Lampa1On():
    GPIO.output(18, GPIO.HIGH)
def Lampa2On():
    GPIO.output(23, GPIO.HIGH)
def Lampa1Off():
    GPIO.output(18, GPIO.LOW)
def Lampa2Off():
    GPIO.output(23, GPIO.LOW)
'''Mérő függvény'''
def meres():
    global temp
    global hum
    dht_device = adafruit_dht.DHT11(board.D4)
    mariadb_connection = mariadb.connect(user='raspberry', password='pi', database='data')
    cursor = mariadb_connection.cursor()

    while True:
        temp = dht_device.temperature
        hum = dht_device.humidity
        cursor.execute("INSERT INTO `Hopara`(`Hofok`, `Para`) VALUES (%s,%s)", (temp, hum))
        cursor.execute("DELETE FROM Hopara WHERE IDOPONT<DATE_SUB(LOCALTIME(), INTERVAL 3 HOUR)")
        mariadb_connection.commit()
        sleep(10)
'''Hőszabályozó függvény'''
def heat():
    while(temp<tempset and kapdef[0]=="checked"):
        GPIO.output(22, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)
'''Riasztó függvény'''
def riaszt():
    while(kapdef[2]=="checked"):
        if(GPIO.input(17)==GPIO.HIGH):
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            break

'''Mérőszál indítása'''
Thread(target=meres).start()


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def main():
    '''Változók inicializálása'''
    global tempset
    global kapdef
    datalist=""
    templist=""
    humlist=""
    kapcsolok=""
    '''Hőmérsékletelőzmények lekérdezése az adatbázisból'''
    mariadb_connection = mariadb.connect(user='raspberry', password='pi', database='data')
    cursor = mariadb_connection.cursor()
    cursor.execute("SELECT HOUR(Idopont),MINUTE(IDOPONT),Hofok,Para FROM Hopara WHERE IDOPONT>DATE_SUB(LOCALTIME(), INTERVAL 60 MINUTE)")
    '''Hőmérsékletelézmények átalakítása JS-nek érthetően'''
    for Idopont,Idopont2, Hofok, Para in cursor:
        datalist=datalist+"'"+str(Idopont)+":"+str(Idopont2)+"',"
        templist=templist+str(Hofok) + ","
        humlist=humlist+str(Para) + ","
        '''SQL zár'''
    cursor.close()
    mariadb_connection.close()
    '''gombnyomás/számadat beírás érzékelése és tárolása'''
    if request.method == 'POST':
        kapcsolok=request.get_data(as_text=True)
    else: pass
    kapcsolok=kapcsolok.split(",")
    '''Gombok oldaltöltéskori értékének beállítása'''
    for i, x in enumerate(kapcsolok):
        if x=="false":
            kapdef[i]=""
        elif x=="true":
            kapdef[i]="checked"
        elif x.isdigit():
            tempset=int(x)
    '''Lámpa fel és lekapcsolás'''
    if(kapdef[3]=="checked"):
        Lampa1On()
    else: Lampa1Off()
    if(kapdef[4]=="checked"):
        Lampa2On()
    else: Lampa2Off()
    '''Fűtés kapcsolása'''
    if(kapdef[0]=="checked"):
        Thread(target=heat).start()
    elif(kapdef[1]=="checked"):
        GPIO.output(22, GPIO.HIGH)
    else:GPIO.output(22, GPIO.LOW)
    '''riasztó élesítés'''
    if(kapdef[2]=="checked"):
        Thread(target=riaszt).start()
    '''Oldal Render'''
    return render_template('index.html', futauto_default=kapdef[0], futon_default=kapdef[1],
                               riaszt_default=kapdef[2], lampa1_default=kapdef[3], lampa2_default=kapdef[4],
                               temp_value=tempset, gauge_temp=temp, gauge_hum=hum, d_list=datalist,
                               temp_list=templist, hum_list=humlist)
