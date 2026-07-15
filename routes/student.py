from flask import Blueprint, render_template, request, redirect
from models.student import Student
from utils.helpers import login_required
from flask import jsonify

student = Blueprint("student", __name__)

# VIEW ALL STUDENTS
@student.route("/students")
@login_required
def students_list():
    data = Student.get_all_students()
    return render_template("students.html", students=data)

# ADD STUDENT FORM
@student.route("/students/add", methods=["GET", "POST"])
@login_required
def add_student():
    if request.method == "POST":
        full_name = request.form["full_name"]
        phone = request.form["phone"]
        email = request.form["email"]
        course = request.form["course"]

        Student.add_student(full_name, phone, email, course)

        return redirect("/students")

    return render_template("add_student.html")

@student.route("/students/delete/<int:id>", methods=["GET"])
@login_required
def delete_student(id):

    Student.delete_student(id)

    return jsonify({
        "success": True,
        "id": id
    })

@student.route("/students/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_student(id):

    student = Student.get_student_by_id(id)

    if not student:
        return "Student not found", 404

    if request.method == "POST":

        full_name = request.form["full_name"]
        phone = request.form["phone"]
        email = request.form["email"]
        course = request.form["course"]

        Student.update_student(id, full_name, phone, email, course)

        return redirect("/students")

    return render_template("edit_student.html", student=student)