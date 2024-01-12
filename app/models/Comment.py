from .database import db

# Commentモデルの定義
class Comment(db.Model):
    __tablename__ = 'Comment'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    commenter_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('Postinformation.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'commenter_id': self.commenter_id,
            'post_id': self.post_id
        }
