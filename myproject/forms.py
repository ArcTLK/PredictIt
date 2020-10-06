from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, RadioField, Form
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[
                       DataRequired('Enter Your Name Please!')])
    email = StringField('Email', validators=[DataRequired(
        'Enter A Valid Email Please!'), Email()])
    password = PasswordField('Password', validators=[DataRequired('Enter Password Please!'), EqualTo(
        'pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField(
        'Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')


class InfoForm(FlaskForm):
    name = StringField('Name:', validators=[
                       DataRequired('Kindly Enter Your Name!')])
    submit = SubmitField('Get Started')


class SymptomForm(FlaskForm):
    symptom1 = StringField('Enter Your Symptom:', validators=[
                           DataRequired('Kindly Enter Your Symptom!')])
    num_days = IntegerField('Enter The Number Of Days You Are Experiencing This Symptom For:', validators=[
                            DataRequired('Kindly Input!')])
    submit = SubmitField('Proceed')


class OtherSymptomForm(Form):
    symptom = RadioField('', choices=[('yes', 'Yes'), ('no', 'No')])