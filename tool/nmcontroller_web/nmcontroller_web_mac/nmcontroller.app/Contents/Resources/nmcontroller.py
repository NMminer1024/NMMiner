# -*- coding: utf-8 -*-
"""

@file: nmcontroller.py

@author: NM

@copyright  Copyright (c) 2024, NMTech. All rights reserved

"""

from flask import Flask, request, render_template
import waitress
import socket, sys, os
import json
import threading
import time



if hasattr(sys, '_MEIPASS'):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
else:
    template_folder = 'templates'


# Receive UDP from the NMMiner
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 12345))
sock.settimeout(5)
is_running = True
nmminer_map = {}

def receive_data():
    while is_running:
        try:
            data, addr = sock.recvfrom(1024)
            try:
                json_data = json.loads(data)
                nmminer_map[json_data['ip']] = json_data
                nmminer_map[json_data['ip']]['UpdateTime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            except json.JSONDecodeError:
                print("Decode Json Wrong: ", data)
        except socket.timeout:
            print("recving timeout")

udpThread = threading.Thread(target=receive_data)
udpThread.start()

app = Flask(__name__, template_folder=template_folder)

@app.route('/', methods=['GET', 'POST'])
@app.route('/web_monitor', methods=['GET', 'POST'])
def web_monitor():
    nmminer_list = []
    for key in nmminer_map:
        nmminer_list.append([nmminer_map[key]['ip'], nmminer_map[key]["BoardType"], 
                             nmminer_map[key]['HashRate'], nmminer_map[key]["Share"],
                             nmminer_map[key]['NetDiff'], nmminer_map[key]['BestDiff'], 
                             nmminer_map[key]['Valid'], round(nmminer_map[key]['Temp'], 1), 
                             nmminer_map[key]['RSSI'], round(nmminer_map[key]['FreeHeap'], 2), 
                             nmminer_map[key]['Version'], nmminer_map[key]['Uptime'],
                             nmminer_map[key]['UpdateTime']])
    return render_template('web_monitor.html', result=nmminer_list)

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # 连接到一个外部地址以获取本机IP地址
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


def logo_print():
    print("            ___          ___         ")
    print("           /\\__\\        /\\__\\    ")
    print("          /::|  |      /::|  |       ")
    print("         /:|:|  |     /:|:|  |       ")
    print("        /:/|:|  |__  /:/|:|__|__     ")
    print("       /:/ |:| /\\__\\/:/ |::::\\__\\")
    print("       \\/__|:|/:/  /\\/__/~~/:/  /  ")
    print("           |:/:/  /       /:/  /     ")
    print("           |::/  /       /:/  /      ")
    print("           /:/  /       /:/  /       ")
    print("           \\/__/        \\/__/      ")

if __name__ == "__main__":
    local_ip = get_local_ip()
    port = 7877
    logo_print()
    print("NM centralize monitor server running...")
    print("NMMiner firmware version v0.3.01 or later is required.")
    print(f"Access it in your LAN at http://{local_ip}:{port} or http://localhost:{port}")
    cwd = os.getcwd()
    if '.app/Contents/Resources' in cwd:
        print('running on macOS')
        os.system('open "http://127.0.0.1:7877"')
    waitress.serve(app, host='0.0.0.0', port=port)
    is_running = False
    print("Web monitor is closed.")
    