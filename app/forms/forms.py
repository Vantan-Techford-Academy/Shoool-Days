# forms.py

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class SignupForm(FlaskForm):
    user_name = StringField('', validators=[DataRequired()], render_kw={"placeholder":""})
    mail_address = StringField('', validators=[DataRequired(), Email()], render_kw={"placeholder":""})
    password = PasswordField('', validators=[DataRequired()], render_kw={"placeholder":""})
    confirm_password = PasswordField('', validators=[DataRequired(), EqualTo('password', message="パスワードが一致しません")], render_kw={"placeholder":""})
    profile_image = FileField('アカウント画像を選択してください', validators=[FileAllowed(['jpg', 'jpeg', 'png'])], render_kw={"placeholder":""})
    submit = SubmitField('登録')

class LoginForm(FlaskForm):
    user_name = StringField('', validators=[DataRequired()])
    password = PasswordField('', validators=[DataRequired()])
    submit = SubmitField('ログイン')
