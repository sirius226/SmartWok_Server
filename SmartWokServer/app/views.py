from flask import render_template, flash, redirect, request
from app import app
from forms import LoginForm
from forms import ButtonForm
import os
import socket

if os.name != "nt":
    import fcntl
    import struct

    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip


cookingIdx = 1
mealtype = 0
user = { 'nickname': 'Diaosi' }
mealname = 'BwB'
meal = 'Beef with Broccoli'

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    form = ButtonForm()
    global cookingIdx
    global mealtype
    global mealname
    global meal
    server_ip = get_lan_ip()
    if request.method == 'GET':
        return render_template('menu.html',
            user = user,
            server_ip = server_ip)
    elif request.method == 'POST':
        print ("mealname: %s" % (str(request.form['mealname'])))
        mealname = str(request.form['mealname'])
        if mealname == 'BwB':
            mealtype = 1
            meal = 'Beef with Broccoli'
        elif mealname == 'HC-PC':
            mealtype = 2
            meal = 'HC-Pineapple Chicken'
        elif mealname == 'PSwO':
            mealtype = 3
            meal = 'Pepper Steak with Onion'
        return render_template('cooking.html',
            user = user,
            server_ip = server_ip,
            mealname = mealname,
            meal = meal,
            cookingIdx = cookingIdx)

@app.route('/cooking',methods = ['GET', 'POST'])
def cooking():
    global cookingIdx
    server_ip = get_lan_ip()
    if request.method == 'GET':
        return render_template('cooking.html',
            user = user,
            server_ip = server_ip,
            mealname = mealname,
            meal = meal,
            cookingIdx = cookingIdx)
    elif request.method == 'POST':
        command = str(request.form['command'])
        if command == 'preheating':
            cookingIdx = 2
        elif command == 'cooking':
            cookingIdx = 3
        else:
            print ("do not know the command")
        return render_template('cooking.html',
            user = user,
            server_ip = server_ip,
            mealname = mealname,
            meal = meal,
            cookingIdx = cookingIdx)

# @app.route('/')
# @app.route('/login', methods = ['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
#         return redirect('/index')
#     return render_template('login.html', 
#         title = 'Sign In',
#         form = form,
#         providers = app.config['OPENID_PROVIDERS'])


@app.route('/recipie/01')
def recipie():
    if cookingIdx == 2 and mealtype ==1:
        return "b"
    elif cookingIdx == 3 and mealtype ==1:
        return "c"
    elif cookingIdx == 2 and mealtype ==2:
        return "d"
    elif cookingIdx == 3 and mealtype ==2:
        return "e"
    else:
        return "a"

@app.route('/')
def rootpage():
    return redirect('/login')

@app.route('/login',methods = ['GET', 'POST'])
def login():
    global user
    server_ip = get_lan_ip()
    if request.method == 'GET':
        return render_template('index.html',
            server_ip = server_ip)
    elif request.method == 'POST':
        print ("%s Logined" % (str(request.form['username'])))
        user = { 'nickname': str(request.form['username']) }
        return render_template('account.html',
            user = user,
            server_ip = server_ip)

@app.route('/account',methods = ['GET', 'POST'])
def account():
    server_ip = get_lan_ip()
    if request.method == 'GET':
        user = { 'nickname': 'Diaosi'}
        return render_template('account.html',
            user = user,
            server_ip = server_ip)

@app.route('/favorite',methods = ['GET', 'POST'])
def favorite():
    server_ip = get_lan_ip()
    if request.method == 'GET':
        user = { 'nickname': 'Diaosi'}
        return render_template('favorite.html',
            user = user,
            server_ip = server_ip)

@app.route('/shopping',methods = ['GET', 'POST'])
def shopping():
    server_ip = get_lan_ip()
    if request.method == 'GET':
        user = { 'nickname': 'Diaosi'}
        return render_template('shopping.html',
            user = user,
            server_ip = server_ip)

@app.route('/uploading',methods = ['GET', 'POST'])
def uploading():
    server_ip = get_lan_ip()
    if request.method == 'GET':
        user = { 'nickname': 'Diaosi'}
        return render_template('uploading.html',
            user = user,
            server_ip = server_ip)






