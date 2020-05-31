from flask import Flask, render_template, request
from bing_detect import detect_bing
from PIL import Image
import io
import numpy as np
import os


app = Flask(__name__, static_folder="images")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(APP_ROOT, 'images/')
full_path = target + 'result.png'

@app.route('/bing_search', methods = ['GET','POST'])
def Bing_detection():
	'''
	Routing Bing search detection APP
	Methods permitted  : GET, POST
	'''
	if request.method == 'GET':
	    return render_template('index_bing.html')

	if request.method == 'POST':
		X = request.form['xname']
		if not X or X == '':
			return render_template('error_bing.html', message='EMPTY_URL_ERROR : please enter something !')

		model_path = APP_ROOT + '/model.pkl'
		print(X)
		print(model_path)
		prediction = detect_bing(X, model_path)
		print(prediction)
		prediction_list = [X, prediction]
		return render_template('result_bing.html', prediction_list=prediction_list)
