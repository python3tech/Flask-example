from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Email %r>' % self.email

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    payload = request.json
    try:
        client = User(username=payload.get('username'), email=payload.get('email'))
        db.session.add(client)
        db.session.commit()
    except:
        return jsonify({"responseMessage":"User already exist with given credentials.","data":payload})
    return jsonify({"responseMessage":"User created successfully.","data":payload})



@app.route("/get_data", methods=['GET', 'POST'])
def get_data():
    payload = request.json
    try:
        client = User.query.filter_by(username=payload.get('username')).first()
        return jsonify({
            'success': True,
            'data': client.serialize()
        })
    except:
        return jsonify({
            'success': False,
            'data': 'User does not exist.'
            })
    return jsonify({"responseMessage":"User created successfully.","data":payload})


@app.route("/update_data", methods=['GET', 'POST'])
def update_data():
    payload = request.json
    try:
        client = User.query.filter_by(username=payload.get('username')).first()
        client.email = payload.get('email')
        client.username = payload.get('username')
        db.session.add(client)
        db.session.commit()
        return jsonify({
            'success': True,
            'data': client.serialize()
        })
    except:
        return jsonify({"responseMessage":"User already exist with given credentials.","data":payload})
    return jsonify({"responseMessage":"User updated successfully.","data":payload})



@app.route("/delete_data", methods=['GET', 'POST'])
def delete_data():
    payload = request.json
    try:
        client = User.query.filter_by(username=payload.get('username')).first()
        db.session.delete(client)
        db.session.commit()
        return jsonify({
            'success': True,
            'data': "User deleted successfully."
        })
    except:
        return jsonify({"responseMessage":"User already exist with given credentials.","data":payload})
    return jsonify({"responseMessage":"User updated successfully.","data":payload})



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)