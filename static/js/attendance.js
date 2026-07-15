document.addEventListener("DOMContentLoaded", function () {

    console.log("Attendance module loaded");

    const markButton = document.querySelector(".btn-mark");
    const dateInput = document.getElementById("attendanceDate");

    // =========================
    // 1. DEFAULT DATE = TODAY
    // =========================

    const today = new Date().toISOString().split("T")[0];
    if (dateInput) {
        dateInput.value = today;
    }

    // =========================
    // 2. MARK ATTENDANCE ACTION
    // =========================

    markButton.addEventListener("click", function () {

        let selectedDate = dateInput.value;

        if (!selectedDate) {
            alert("Please select a date first");
            return;
        }

        // Collect attendance data from table
        let rows = document.querySelectorAll("table tbody tr");

        let attendanceData = [];

        rows.forEach(row => {

            let id = row.cells[0].innerText;
            let name = row.cells[1].innerText;
            let course = row.cells[2].innerText;
            let status = row.querySelector(".status").value;

            attendanceData.push({
                id: id,
                name: name,
                course: course,
                status: status,
                date: selectedDate
            });

        });

        console.log("Attendance Data:", attendanceData);

        // =========================
        // 3. UI FEEDBACK (SIMULATION)
        // =========================

        fetch("/attendance/save", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(attendanceData)
        })
        .then(response => response.json())
        .then(data => {

            console.log("Backend Response:", data);

            if (data.success) {

                showMessage(data.message);

            } else if (data.exists) {

                alert(data.message);

            } else {

                alert(data.message);

            }

        })
        .catch(error => {

            console.error(error);

            alert("Something went wrong while saving attendance.");

        });

    });

});

const historyBtn = document.querySelector(".btn-history");

historyBtn.addEventListener("click", () => {

    window.location.href = "/attendance/history";

});

document.addEventListener("DOMContentLoaded", function () {

    formatAllMoneyElements();

});