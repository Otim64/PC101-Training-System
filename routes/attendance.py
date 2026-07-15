from flask import Blueprint, render_template, request, jsonify, redirect
from models.attendance import Attendance
from models.student import Student
from utils.helpers import login_required

attendance = Blueprint("attendance", __name__)


# VIEW ATTENDANCE
@attendance.route("/attendance")
@login_required
def attendance_list():

    students = Student.get_all_students()

    return render_template(
        "attendance.html",
        students=students
    )


@attendance.route("/attendance/save", methods=["POST"])
@login_required
def save_attendance():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No attendance data received."
        })

    attendance_date = data[0]["date"]

    existing = Attendance.get_attendance_by_date(attendance_date)

    if existing:
        return jsonify({
            "success": False,
            "exists": True,
            "message": "Attendance for this date already exists."
        })

    for record in data:

        Attendance.mark_attendance(
            record["id"],
            record["status"],
            record["date"]
        )

    return jsonify({
        "success": True,
        "message": "Attendance saved successfully."
    })

@attendance.route("/attendance/history")
@login_required
def attendance_history():

    # Try today's date first
    from datetime import date

    today = date.today().isoformat()

    records = Attendance.get_attendance_by_date(today)

    # If no records today → fallback to latest records
    if not records:
        records = Attendance.get_all_attendance()

    return render_template(
        "attendance_history.html",
        records=records,
        default_date=today
    )

@attendance.route("/attendance/history/filter", methods=["POST"])
@login_required
def filter_attendance():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No JSON data received"
        })

    date = data.get("date")

    if not date:
        from datetime import date as dt
        date = dt.today().isoformat()

    records = Attendance.get_attendance_by_date(date)

    return jsonify({
        "success": True,
        "data": records
    })

