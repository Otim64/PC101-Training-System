from flask import Blueprint, render_template, session
from utils.helpers import login_required
from models.student import Student
from models.payment import Payment
from models.attendance import Attendance

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/dashboard")
@login_required
def home():

    username = session.get("username")

    # ---- CORE METRICS ----
    student_count = Student.count_students()
    payment_total = Payment.total_payments()
    attendance_total = Attendance.count_attendance()

    # ---- ATTENDANCE RATE (MVP VERSION) ----
    # later we will refine with PRESENT/ABSENT logic
    attendance_rate = 75 if attendance_total > 0 else 0

    # ---- RECENT STUDENTS (PROPER ORDER) ----
    recent_students = Student.get_all_students()[-5:]

    return render_template(
        "dashboard.html",
        username=username,
        student_count=student_count,
        payment_total=payment_total,
        attendance_rate=attendance_rate,
        recent_students=recent_students
    )