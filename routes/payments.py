from flask import Blueprint, render_template, request, redirect, jsonify
from models.payment import Payment
from models.student import Student
from utils.helpers import login_required

payment = Blueprint("payment", __name__)


# VIEW PAYMENTS
@payment.route("/payments")
@login_required
def payments():

    data = Payment.get_all_payments()

    total_collected = Payment.total_payments()
    transactions = Payment.count_payments()

    student_count = Student.count_students()

    pending_payments = Payment.calculate_pending_payments(
        student_count,
        total_collected
    )

    return render_template(
        "payments.html",
        payments=data,
        total_collected=total_collected,
        transactions=transactions,
        pending_payments=pending_payments
    )


# ADD PAYMENT
@payment.route("/payments/add", methods=["GET", "POST"])
@login_required
def add_payment():

    if request.method == "POST":

        student_id = request.form["student_id"]
        amount = request.form["amount"]
        description = request.form["description"]

        Payment.add_payment(
            student_id,
            amount,
            description
        )

        return redirect("/payments")

    students = Student.get_all_students()

    return render_template(
        "payment_form.html",
        students=students
    )


# DELETE PAYMENT
@payment.route("/payments/delete/<int:id>")
@login_required
def delete_payment(id):

    Payment.delete_payment(id)

    return redirect("/payments")

@payment.route("/payments/search")
@login_required
def search_payments():

    query = request.args.get("query", "")

    payments = Payment.search_payments(query)

    return jsonify(payments)