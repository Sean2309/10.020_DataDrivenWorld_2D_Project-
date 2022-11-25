from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField, IntegerField, HiddenField, SelectField
from wtforms.validators import DataRequired, ValidationError, EqualTo

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
	var_x = SelectField("Choose the x variable", validators=[DataRequired()]) # X Variable
	var_hue = SelectField("Choose the hue variable", validators=[DataRequired()]) # Hue Variable
	var_y = SelectField("Choose the y variable", validators=[DataRequired()]) # Y Variable for bivariate
	var_year = SelectField("Choose the year variable", validators=[DataRequired()])
	submit = SubmitField('Display')





	
