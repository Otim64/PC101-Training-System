document.addEventListener("DOMContentLoaded", function () {

    console.log("Edit Student page loaded");

    const form = document.getElementById("editStudentForm");

    form.addEventListener("submit", function (e) {

        let fullName = form.full_name.value.trim();

        if (fullName.length < 3) {
            e.preventDefault();
            alert("Full name must be at least 3 characters");
            return;
        }

        alert("Student update ready (backend will process this later)");

    });

});