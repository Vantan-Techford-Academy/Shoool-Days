from flask import Flask, render_template, request, redirect, flash, url_for
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from models.database import init_db, db
from models.User import User
from models.Category import Category
from models.Postinformation import Postinformation
from models.Comment import Comment
from models.Good import Good
from werkzeug.security import generate_password_hash, check_password_hash
from forms.forms import SignupForm, LoginForm
import os
import secrets
from PIL import Image
import pymysql

app = Flask(__name__)

def getConnection():
    return pymysql.connect(
        host='localhost',
        db='mydb',
        user='root',
        password='',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )

IMG_FOLDER = os.path.join("static", "image")
app.config["UPLOAD_FOLDER"] = IMG_FOLDER
IMG_FOLDER_ICON = os.path.join("static", "profile_img")
app.config["UPLOAD_FOLDER_ICON"] = IMG_FOLDER_ICON

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test_user:password@db/schoool_days_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'lemontea'
csrf = CSRFProtect(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
init_db(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def save_picture(form_profile_image): #画像保存関数
    if form_profile_image:
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(form_profile_image.filename)
        picture_fn = random_hex + f_ext
        picture_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), 'static/profile_img', picture_fn)
        i = Image.open(form_profile_image)
        i.thumbnail((200, 200))
        i.save(picture_path)
        return picture_fn
    else:
        return None


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST' and form.validate_on_submit():
        user_name = form.user_name.data
        mail_address = form.mail_address.data
        password = form.password.data
        profile_image = save_picture(form.profile_image.data)
    # メールアドレスの重複を確認
        existing_user = User.query.filter_by(mail_address=form.mail_address.data).first()

        if existing_user:
            # 既に存在する場合は警告メッセージを表示
            flash('このメールアドレスは既に使用されています。別のメールアドレスをお試しください。', 'warning')
        else:
            # パスワードをハッシュ化
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            # ユーザーを作成してデータベースに追加
            new_user = User(user_name=user_name, mail_address=mail_address, password=hashed_password, profile_image = profile_image)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect('/Mypage')
    return render_template('signup.html', form=form)

@app.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(user_name=form.user_name.data).first()
        password = check_password_hash(user.password, form.password.data)
        if user and password:
            login_user(user)
            return redirect('/Mypage')

    return render_template('login.html', form=form)

@app.route("/Mypage", methods=["GET", "POST"])
def mainpage():
    Flask_Icon_1 = os.path.join(app.config["UPLOAD_FOLDER"], "HomeImage.png")
    Flask_Icon_2 = os.path.join(app.config["UPLOAD_FOLDER"], "CategoryImage.png")
    Flask_Icon_3 = os.path.join(app.config["UPLOAD_FOLDER"], "InquiryImage.png")
    Flask_Icon_4 = os.path.join(app.config["UPLOAD_FOLDER_ICON"], current_user.profile_image)
    user_Text = {
        "User_name": current_user.user_name,
        "User_Email": current_user.mail_address,
    }
    return render_template('Mypage.html', Home_Icon = Flask_Icon_1, Category_Icon = Flask_Icon_2, Inquiry_Icon = Flask_Icon_3, Human_Icon = Flask_Icon_4, User = user_Text)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route("/goSignup")
def goSignup():
    return redirect("/signup")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8888)
