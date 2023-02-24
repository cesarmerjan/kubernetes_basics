from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask.cli import AppGroup
import click
from . import token_service
from datetime import datetime

SECRET_KEY = "H4ard t0 Gu3Ss"

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@authentication-database-service:5432/authentication"
# "postgres:///test.sqlite"
db = SQLAlchemy()
db.init_app(app)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


@app.before_request
def access_controller():
    if request.path != "/login":
        token = request.cookies.get("access-token")
        if token:
            try:
                token_service.validate_token(token, SECRET_KEY)
            except Exception as error:
                return jsonify({"message": "unauthorazied"}), 401
        else:
            return jsonify({"message": "missing access token"}), 400


@app.post("/login")
def login():
    body = request.json

    user = db.session.query(User).filter_by(email=body["email"]).first()
    if user and user.password == body["password"]:
        token = token_service.generate_token(
            {"user_id": "1"}, SECRET_KEY, datetime(year=2023, month=3, day=1))

        response = make_response(jsonify({"message": "OK"}), 200)
        response.set_cookie(key="access-token",
                            value=token,
                            path="/",
                            httponly=True
                            )

        return response
    else:
        return jsonify({"message": "Not Found"}), 404


@app.get("/logout")
def logout():
    response = make_response(jsonify({"message": "OK"}), 200)
    response.delete_cookie("access-token")
    return response


@app.post("/sign_in")
def sign_in():
    body = request.json
    user = User(
        name=body["name"],
        email=body["email"],
        password=body["password"]
    )
    db.session.add(user)
    db.session.commit()
    return "OK", 201


user_cli = AppGroup("user")


@user_cli.command("create")
@click.argument("name")
@click.argument("email")
@click.argument("password")
def create_user(name, email, password):
    user = db.session.query(User).filter_by(email=email).first()
    if not user:
        user = User(
            name=name,
            email=email,
            password=password
        )
        db.session.add(user)
        db.session.commit()
        print(f"User {name} was created.")
    else:
        print(f"User already exists.")


app.cli.add_command(user_cli)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
