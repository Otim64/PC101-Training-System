document.addEventListener("DOMContentLoaded", function () {

    console.log("Add Student page loaded");

    const form = document.getElementById("addStudentForm");

    form.addEventListener("submit", function (e) {

        // ---------------------------
        // FRONTEND VALIDATION ONLY
        // ---------------------------

        let fullName = form.full_name.value.trim();
        let email = form.email.value.trim();

        if (fullName.length < 3) {
            e.preventDefault();
            alert("Full name must be at least 3 characters");
            return;
        }

        if (email !== "" && !email.includes("@")) {
            e.preventDefault();
            alert("Please enter a valid email");
            return;
        }

        alert("Student form ready to submit (backend will handle saving later)");

    });

});