export FLASK_APP=serv.py
echo "pensez bien à lancer Jack !"
chromium-browser 127.0.0.1:5000 &
flask run