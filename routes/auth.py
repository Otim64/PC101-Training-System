from flask import Blueprint, request, redirect, render_template, session, url_for, flash
from models.user import User
from utils.security import hash_password, verify_password

auth = Blueprint("auth", __name__)

# -------------------------
# REGISTER
# -------------------------
@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # OPTIONAL: basic validation
        if not username or not email or not password:
            flash("All fields are required", "error")
            return redirect("/register")

        # hash password
        password_hash = hash_password(password)

        try:
            # save user to database
            User.create_user(username, email, password_hash)

            flash("Account created successfully! Please login.", "success")
            return redirect("/")

        except Exception as e:
            flash("Username or email already exists", "error")
            return redirect("/register")

    return render_template("register.html")


# -------------------------
# LOGIN
# -------------------------
@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.get_user_by_username(username)

        if user and verify_password(user["password_hash"], password):

            session["user_id"] = user["id"]
            session["username"] = user["username"]

            flash("Login successful! Welcome back " + user["username"], "success")
            return redirect("/dashboard")

        flash("Invalid username or password", "error")
        return redirect("/")

    return render_template("index.html")


# -------------------------
# LOGOUT
# -------------------------
@auth.route("/logout")
def logout():

    session.clear()

    flash("You have been logged out successfully", "success")
    return redirect("/")