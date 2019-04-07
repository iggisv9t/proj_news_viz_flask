#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pandas as pd
import altair as alt
import json
from datamanager import DataManager


data_manager = DataManager()
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/hook', methods=["GET", "POST", 'OPTIONS'])
def change_plot():
    if request.method == 'POST':
        chart = data_manager.change_plot(request)
        # print(chart)

        return json.dumps(chart)

@app.route('/initial', methods=["GET", "POST", 'OPTIONS'])
def get_data():
    if request.method == 'POST':
        data_dict = data_manager.get_initial_data()
        # data_dict = {'rubrics_dict': rubrics_dict, 'topics_dict': topics_dict}
        return json.dumps(data_dict)

if __name__ == "__main__":
    app.run(debug=True)
