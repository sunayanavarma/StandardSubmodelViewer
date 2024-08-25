'''
Created on 27 May 2024

@author: pakala
'''


import os
from dotenv import load_dotenv
from flask import Flask, render_template_string
from flask_sock import Sock
from time import sleep
from restapi.routing import pages

load_dotenv()
template_dir = os.path.abspath('../client')

def create_app():
    app = Flask(__name__,template_folder=template_dir,static_folder=template_dir)
    sock = Sock(app)
    app.register_blueprint(pages.bp)
    
    @sock.route('/ws')
    def websocket(ws):
        print(f'DEBUG: websocket endpoint called')

        while True:
    
            for i in range(1000):
    
                data = 2*i+7
    
                ws.send(data)
    
                sleep(2)

    
    return app