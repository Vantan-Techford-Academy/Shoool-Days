from .database import db

# Categoryモデルの定義
class Category(db.Model):
    __tablename__ = 'Category'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    category_name = db.Column(db.String(50), nullable=False, unique=True)
    posts_relation = db.relationship('Postinformation', backref='category_relation', lazy=True)


    def to_dict(self):
        return {
            'id': self.id,
            'category_name': self.category_name
        }