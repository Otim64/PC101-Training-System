from flask import Blueprint, render_template, jsonify, request
from utils.helpers import login_required
from models.student import Student
from models.payment import Payment
from models.attendance import Attendance
from flask import send_file
from fpdf import FPDF
from datetime import datetime
import os

reports = Blueprint("reports", __name__)


@reports.route("/reports")
@login_required
def reports_page():

    # -----------------------
    # SUMMARY DATA
    # -----------------------
    student_count = Student.count_students()
    payment_total = Payment.total_payments()
    attendance_total = Attendance.count_attendance()

    attendance_rate = 75 if attendance_total > 0 else 0

    # -----------------------
    # ACTIVITY FEED (TABLE)
    # -----------------------

    payments = Payment.get_all_payments()[:3]
    attendance = Attendance.get_all_attendance()[:3]
    students = Student.get_all_students()[:3]

    report_rows = []

    # Convert payments → report format
    for p in payments:
        report_rows.append({
            "id": p["id"],
            "type": "Payment",
            "description": f"{p['full_name']} paid {p['amount']}",
            "date": p["date_paid"],
            "status": "Completed"
        })

    # Convert attendance → report format
    for a in attendance:
        report_rows.append({
            "id": a["id"],
            "type": "Attendance",
            "description": f"{a['full_name']} marked {a['status']}",
            "date": a["date"],
            "status": "Recorded"
        })

    # Convert students → report format
    for s in students:
        report_rows.append({
            "id": s["id"],
            "type": "Student",
            "description": f"{s['full_name']} registered",
            "date": s["date_registered"],
            "status": "Active"
        })

    return render_template(
        "reports.html",
        student_count=student_count,
        payment_total=payment_total,
        attendance_rate=attendance_rate,
        report_rows=report_rows
    )

@reports.route("/reports/pdf")
@login_required
def generate_pdf():

    from flask import request, send_file
    from fpdf import FPDF
    from datetime import datetime

    report_type = request.args.get("type", "all")
    from_date = request.args.get("from")
    to_date = request.args.get("to")

    def in_range(date_str):
        if not from_date and not to_date:
            return True

        try:
            d = datetime.strptime(date_str, "%Y-%m-%d").date()
        except:
            return False

        if from_date and d < datetime.strptime(from_date, "%Y-%m-%d").date():
            return False

        if to_date and d > datetime.strptime(to_date, "%Y-%m-%d").date():
            return False

        return True

    rows = []

    for p in Payment.get_all_payments():
        if report_type in ["all", "payments"] and in_range(p["date_paid"]):
            rows.append({
                "id": p["id"],
                "type": "Payment",
                "description": f"{p['full_name']} paid {p['amount']}",
                "date": p["date_paid"],
                "status": "Completed"
            })

    for a in Attendance.get_all_attendance():
        if report_type in ["all", "attendance"] and in_range(a["date"]):
            rows.append({
                "id": a["id"],
                "type": "Attendance",
                "description": f"{a['full_name']} marked {a['status']}",
                "date": a["date"],
                "status": "Recorded"
            })

    for s in Student.get_all_students():
        if report_type in ["all", "students"] and in_range(s["date_registered"]):
            rows.append({
                "id": s["id"],
                "type": "Student",
                "description": f"{s['full_name']} registered",
                "date": s["date_registered"],
                "status": "Active"
            })

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 14)
    pdf.cell(190, 10, "SYSTEM REPORT", ln=True, align="C")
    pdf.ln(5)

    # TABLE HEADER
    pdf.set_font("Arial", "B", 10)
    pdf.cell(10, 10, "ID", 1)
    pdf.cell(30, 10, "TYPE", 1)
    pdf.cell(70, 10, "DESCRIPTION", 1)
    pdf.cell(30, 10, "DATE", 1)
    pdf.cell(30, 10, "STATUS", 1)
    pdf.ln()

    # TABLE DATA
    pdf.set_font("Arial", size=9)

    for r in rows:
        pdf.cell(10, 10, str(r["id"]), 1)
        pdf.cell(30, 10, r["type"], 1)
        pdf.cell(70, 10, r["description"], 1)
        pdf.cell(30, 10, r["date"], 1)
        pdf.cell(30, 10, r["status"], 1)
        pdf.ln()

    pdf.output("report.pdf")

    return send_file("report.pdf", as_attachment=True)



@reports.route("/reports/filter", methods=["POST"])
@login_required
def filter_reports():

    data = request.get_json()

    report_type = data.get("type", "all")
    from_date = data.get("from")
    to_date = data.get("to")

    report_rows = []

    def in_range(date_str):
        if not from_date and not to_date:
            return True

        try:
            d = datetime.strptime(date_str, "%Y-%m-%d").date()
        except:
            return False

        if from_date:
            if d < datetime.strptime(from_date, "%Y-%m-%d").date():
                return False

        if to_date:
            if d > datetime.strptime(to_date, "%Y-%m-%d").date():
                return False

        return True

    # ---------------- PAYMENTS ----------------
    if report_type in ["all", "payments"]:
        for p in Payment.get_all_payments():

            if in_range(p["date_paid"]):

                report_rows.append({
                    "id": p["id"],
                    "type": "Payment",
                    "description": f"{p['full_name']} paid {p['amount']}",
                    "date": p["date_paid"],
                    "status": "Completed"
                })

    # ---------------- ATTENDANCE ----------------
    if report_type in ["all", "attendance"]:
        for a in Attendance.get_all_attendance():

            if in_range(a["date"]):

                report_rows.append({
                    "id": a["id"],
                    "type": "Attendance",
                    "description": f"{a['full_name']} marked {a['status']}",
                    "date": a["date"],
                    "status": "Recorded"
                })

    # ---------------- STUDENTS ----------------
    if report_type in ["all", "students"]:
        for s in Student.get_all_students():

            if in_range(s["date_registered"]):

                report_rows.append({
                    "id": s["id"],
                    "type": "Student",
                    "description": f"{s['full_name']} registered",
                    "date": s["date_registered"],
                    "status": "Active"
                })

    return jsonify({
        "success": True,
        "data": report_rows
    })