from flask import Flask, url_for, request, render_template, redirect
from model import users as USERS, User, get_next_id

app_2000 = Flask(__name__)


@app_2000.route('/')
def user():
    return 'Hello, User!'

@app_2000.route("/user", methods=['GET', 'POST'])
def get_users():
    if request.method == "GET":
        # return [user.to_dict() for user in USERS]
        return render_template("users_table.html", users_list=USERS)
    elif request.method == "POST":
        data = request.json
        USERS.append(User(**data))
        return "create"

@app_2000.route("/user/<int:user_id>")
def get_user(user_id):
    user = None
    for user in USERS:
        if user.user_id == user_id:
            return user.to_dict()
    return "error user id not found"


@app_2000.route('/user_create', methods=['GET', 'POST'])
def user_create():
    if request.method == "GET":
        return render_template('user_create.html')
    elif request.method == "POST":
        name = request.form.get('user_name')
        age = request.form.get('age')
        email = request.form.get('email')
        role = request.form.get('role')
        USERS.append(User(user_id=get_next_id(USERS), 
                          name=name, 
                          age=age,
                          email=email,
                          role=role))
        # Process and save the new user here (e.g., save to database)
        
        return redirect(url_for("get_users"))  # Redirect to the users list page
    

if __name__ == '__main__':
    # app_2000.run(host="0.0.0.0", port=80)
    with app_2000.test_request_context():
        print(url_for("get_users"))
        print(url_for("get_user", user_id=5))

    app_2000.run(host="0.0.0.0", port=5000)
