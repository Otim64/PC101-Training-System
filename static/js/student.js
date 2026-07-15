// =========================
// STUDENTS MODULE JS
// =========================
console.log("🔥 students.js is LOADED");
document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("searchInput");
    const tableBody = document.getElementById("studentsTable");

    // -------------------------
    // 1. LIVE SEARCH (FRONTEND ONLY)
    // -------------------------
    searchInput.addEventListener("keyup", function () {

        const filter = searchInput.value.toLowerCase();
        const rows = tableBody.getElementsByTagName("tr");

        for (let row of rows) {

            let text = row.innerText.toLowerCase();

            if (text.includes(filter)) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }
        }
    });


    // -------------------------
    // 2. DELETE STUDENT (AJAX)
    // -------------------------
    window.deleteStudent = function (id) {

        if (!confirm("Are you sure you want to delete this student?")) {
            return;
        }

        fetch(`/students/delete/${id}`, {
            method: "GET"
        })
        .then(res => res.json())
        .then(data => {

            if (data.success) {

                // remove row instantly
                const row = document.getElementById(`student-${id}`);

                if (row) {
                    row.remove();
                }

            } else {
                alert("Failed to delete student");
            }

        })
        .catch(err => {
            console.error("Error deleting student:", err);
        });
    };


    // -------------------------
    // 3. AUTO UI REFRESH FUNCTION (OPTIONAL FUTURE USE)
    // -------------------------
    window.refreshStudentsTable = function () {

        fetch("/students")
        .then(res => res.text())
        .then(html => {

            const parser = new DOMParser();
            const doc = parser.parseFromString(html, "text/html");

            const newTable = doc.getElementById("studentsTable");

            if (newTable) {
                tableBody.innerHTML = newTable.innerHTML;
            }
        });
    };

});