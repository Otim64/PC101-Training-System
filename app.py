from flask import Flask, render_template
from routes.auth import auth
from routes.dashboard import dashboard
from routes.student import student
from routes.attendance import attendance
from routes.payments import payment
from routes.reports import reports
from routes.profile import profile


app = Flask(__name__)
app.secret_key = "supersecretkey"

app.register_blueprint(student)
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(attendance)
app.register_blueprint(payment)
app.register_blueprint(reports)
app.register_blueprint(profile)


@app.route("/")
def home():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)