from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from models.database import init_db, db
from models.User import User
from models.Category import Category
from models.Postinformation import Postinformation
from models.Comment import Comment
from models.Good import Good
from werkzeug.security import generate_password_hash
from forms.forms import SignupForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test_user:password@db/schoool_days_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'lemontea'
csrf = CSRFProtect(app)
init_db(app)

@app.route("/")
def index():
    return render_template('header.html')
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()  # YourFormClassを実際のフォームクラスに置き換える

    if request.method == 'POST' and form.validate_on_submit():
        user_name = form.user_name.data
        mail_address = form.mail_address.data
        password = form.password.data

        # パスワードをハッシュ化
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # ユーザーを作成してデータベースに追加
        new_user = User(user_name=user_name, mail_address=mail_address, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8888)
