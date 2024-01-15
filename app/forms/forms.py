# forms.py

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class SignupForm(FlaskForm):
    user_name = StringField('ユーザー名', validators=[DataRequired()])
    mail_address = StringField('メールアドレス', validators=[DataRequired(), Email()])
    password = PasswordField('パスワード', validators=[DataRequired()])
    confirm_password = PasswordField('パスワードの確認', validators=[DataRequired(), EqualTo('password', message="パスワードが一致しません")])
    profile_image = FileField('アカウント画像を選択してください', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('サインアップ')

