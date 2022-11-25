from app import application
from flask import render_template, flash, redirect, url_for
from app.forms import * 
from app.models import User 
from werkzeug.urls import url_parse
from constants import *
from app import db
from flask import request 
from app.serverlibrary import * 

@application.route('/')
@application.route('/index', methods=['GET', 'POST'])
def index():
	form = DropdownForm()
	form.var_type.choices = options.var_types
	form.graph.choices = options.graphs
	form.var1.choices = options.vars
	form.var2.choices = options.vars

	if form.validate_on_submit():
		print(form)
		generate_univariate_graph(form)
		return render_template('graph.html')
	
	return render_template('index.html', title='Home')
