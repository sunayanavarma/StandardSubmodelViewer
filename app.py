'''

Created on 7 Aug 2024

 

@author: pakala

'''

#!/usr/bin/env python3

 

# Pre-requisites

# pip install "Wekzeug>-2.0.0rc3"

# pip install flask-sock

 

# Run with flask development server:

# FLASK_APP=FlaskSock.py flask run

 

# Or run under gunicorn:

# pip install gunicorn

# gunicorn -b :5000 --workers 4 --threads 100 THISFILE:app

 

################################################################################

# HTML/Javascript part - just wanted to avoid a whole bunch of files/directories

################################################################################

HTML = """

<!DOCTYPE html>

<html>

  <head>

  <title>Websocket Demo</title>

  <!-- Pull in jQuery from Google-->

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js"></script>

 

  </head>

  <body>

    <h2>WebSocket Demo</h2>

 

<canvas id="myChart" style="width:100%;max-width:600px"></canvas>

 

<script>

const xValues = [];

const yValues = [];

i = 0

generateData("x * 2 + 7", 0, 1, 0.5);

 

chart = new Chart("myChart", {

  type: "line",

  data: {

    labels: xValues,

    datasets: [{

      fill: false,

      pointRadius: 1,

      borderColor: "rgba(255,0,0,0.5)",

      data: yValues

    }]

  },   

  options: {

    legend: {display: false},

    title: {

      display: true,

      text: "y = x * 2 + 7",

      fontSize: 16

    }

  }

});

function generateData(value, i1, i2, step = 1) {

  for (let x = i1; x <= i2; x += step) {

    xValues.push(x);

    yValues.push(eval(value));

  }

  i = i +1

}

      // Create websocket

      var ws = new WebSocket('ws://127.0.0.1:{{port}}/ws');

 

      // Whenever new message received, update display

      ws.onmessage = function(event) {

 

        console.log('DEBUG: Received ' + event.data);

 

        var HTML = "<li>" + event.data + "</li>";

        $("#culist").append(HTML);

        xValues.push(i);

        yValues.push(parseInt(event.data));

        i = i + 1;

            chart.update();

 

      }

 

      // Send first message to get server to start sending updates

      ws.send('GO!');

 

</script>

       <div>

          <h2>Another continuously updated list:</h2>

       <ul id="culist">

       </ul>

    </div>

  </body>

</html>

"""

 

################################################################################

# Python part

################################################################################

from flask import Flask, render_template_string

from flask_sock import Sock

from time import sleep

 

port = 5000

app = Flask(__name__)

sock = Sock(app)

 

@sock.route('/ws')

def anything(ws):

    print(f'DEBUG: websocket endpoint called')

    while True:

        for i in range(1000):

            data = 2*i+7

            ws.send(data)

            sleep(2)

 

@app.route('/')

def main():

    print(f'DEBUG: Sending main page')

    return render_template_string(HTML, port=port)

 

app.run(host="localhost",port = 5000)