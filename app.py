from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'  
db = SQLAlchemy(app)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    permissions = db.relationship('Permission', backref='role', lazy=True)

    def __repr__(self):
        return f"Role(name='{self.name}')"


class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

    def __repr__(self):
        return f"Permission(name='{self.name}')"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        role_name = request.form['role']
        if role_name:
            role = Role.query.filter_by(name=role_name).first()
            if role is not None:
                permissions = [p.name for p in role.permissions]
                return render_template('result.html', role=role.name, permissions=permissions)
    return render_template('index.html')


if __name__ == '__main__':
    db.create_all()  
    app.run(debug=True)
