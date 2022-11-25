from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField, IntegerField, HiddenField, SelectField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from app.models import User

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Repeat Password', 
							   validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')

class DropdownForm(FlaskForm):
	var_type = SelectField("Choose variable type", validators=[DataRequired()])
	graph = SelectField("Choose graph type", validators=[DataRequired()])
	var1 = SelectField("Choose the 1st variable", validators=[DataRequired()])
	var2 = SelectField("Choose the 2nd variable", validators=[DataRequired()])
	submit = SubmitField('Display')





	
