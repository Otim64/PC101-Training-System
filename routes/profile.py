from flask import Blueprint, render_template, session, redirect
from utils.helpers import login_required
import os
from werkzeug.utils import secure_filename
from flask import request
from models.user import User

profile = Blueprint("profile", __name__)


@profile.route("/profile")
@login_required
def profile_page():

    user_id = session.get("user_id")

    user = User.get_user_by_id(user_id)

    return render_template("profile.html", user=user)

from flask import request, jsonify

@profile.route("/profile/update", methods=["POST"])
@login_required
def update_profile():

    user_id = session.get("user_id")

    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    phone = data.get("phone")

    User.update_user_profile(user_id, username, email, phone)

    return jsonify({
        "success": True,
        "message": "Profile updated successfully"
    })

import os
from werkzeug.utils import secure_filename

@profile.route("/profile/upload-image", methods=["POST"])
@login_required
def upload_image():

    user_id = session.get("user_id")

    file = request.files["image"]

    if file:

        filename = secure_filename(file.filename)

        path = os.path.join("static/uploads", filename)
        file.save(path)

        User.update_profile_image(user_id, filename)

        return jsonify({
            "success": True,
            "message": "Profile image updated"
        })

    return jsonify({
        "success": False,
        "message": "No image uploaded"
    })