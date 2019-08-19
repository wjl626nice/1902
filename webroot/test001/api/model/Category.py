from app import db
#创建模型对象
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cate_name = db.Column(db.String(80), unique=True, nullable=False)
    describles = db.Column(db.String(120), unique=True, nullable=False)
    pic = db.Column(db.String(120), unique=True, nullable=False)
    is_menu = db.Column(db.Integer, default=0, nullable=False)
    weight = db.Column(db.SmallInteger, nullable=False)
    seo_title = db.Column(db.String(120), nullable=False)
    seo_keyword = db.Column(db.String(120), nullable=False)
    seo_description = db.Column(db.String(120), nullable=False)
    num = db.Column(db.Integer, default=0, nullable=False)

def __repr__(self):
    return '<Category %r>' % self.cate_name


