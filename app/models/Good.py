from .database import db

class Good(db.Model):
    __tablename__ = 'Good'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    gooder_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('Postinformation.id'), nullable=False)

    # ForeignKey制約の設定
    gooder = db.relationship('User', backref='goods_given')
    post = db.relationship('Postinformation', backref='goods_received')

    def to_dict(self):
        return {
            'id': self.id,
            'gooder_id': self.gooder_id,
            'post_id': self.post_id
        }
