from flask import Flask, url_for, request, render_template, redirect
from model import User, get_next_id

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def get_users():
    if request.method == "GET":
        # return [user.to_dict() for user in USERS]
        users = User.load()
        print(users)
        return render_template("users_table.html", users_list=users)


@app.route("/user_create", methods=["GET", "POST"])
def user_create():
    if request.method == "GET":
        return render_template("user_create.html")
    elif request.method == "POST":
        name = request.form.get("user_name")
        age = request.form.get("age")
        email = request.form.get("email")
        role = request.form.get("role")
        users = User.load()
        print(users)
        user = User(
            user_id=get_next_id(users), name=name, age=age, email=email, role=role
        )
        # Process and save the new user here (e.g., save to database)
        User.add(user)
        return redirect(url_for("get_users"))
if __name__ == "__main__":
    # app_2000.run(host="0.0.0.0", port=80)


    app.run(host="0.0.0.0", port=5000)
