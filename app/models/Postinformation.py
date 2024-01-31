from .database import db

# Postinformationモデルの定義
class Postinformation(db.Model):
    __tablename__ = 'Postinformation'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    post_title = db.Column(db.String(64), nullable=False)
    post_details = db.Column(db.Text, nullable=False)
    post_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    poster_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    tag = db.Column(db.String(128))
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'))

    # ForeignKey制約の設定
    poster = db.relationship('User', backref='posts_information')
    category = db.relationship('Category', backref='posting_relation', lazy=True)
    comments = db.relationship('Comment', backref='post')

    def to_dict(self):
        return {
            'id': self.id,
            'post_title': self.post_title,
            'post_details': self.post_details,
            'post_date': self.post_date,
            'poster_id': self.poster_id,
            'tag': self.tag,
            'category_id': self.category_id
        }
