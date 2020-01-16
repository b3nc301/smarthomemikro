
#!/bin/bash
echo Installer
sudo apt install -y mariadb-server python3
pip3 install flask
pip3 install adafruit-circuitpython-dht
pip3 install mysql-connector
pip3 install gunicor
sudo install mariadb-server