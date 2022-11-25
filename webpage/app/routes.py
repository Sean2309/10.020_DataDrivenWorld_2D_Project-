from app import application
from flask import render_template, flash, redirect, url_for
from app.forms import * 
from werkzeug.urls import url_parse
from .constants import *
from flask import request 
from app.serverlibrary import * 

@application.route('/')
@application.route('/index', methods=['GET', 'POST'])
def index():
	form = DropdownForm()
	form.var_type.choices = options.get("var_types")
	form.graph.choices = options.get("graphs")
	form.var_hue.choices = options.get("vars")
	form.var_x.choices = options.get("vars")
	form.var_y.choices = options.get("vars")
	form.var_year.choices = options.get("years")

	if form.validate_on_submit():
		print(form)
		generate_univariate_graph(form)
		return render_template('graph.html')
	
	return render_template('index.html', title='Home')
