document.addEventListener("DOMContentLoaded", function () {

    const filterBtn = document.querySelector(".btn-filter");
    const dateInput = document.getElementById("filterDate");
    const tableBody = document.getElementById("historyTable");

    filterBtn.addEventListener("click", function () {

        fetch("/attendance/history/filter", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                date: dateInput.value
            })
        })
        .then(res => res.json())
        .then(data => {

            console.log("Response:", data);

            tableBody.innerHTML = "";

            if (!data.success) {
                tableBody.innerHTML = `<tr><td colspan="5">${data.message}</td></tr>`;
                return;
            }

            if (data.data.length === 0) {
                tableBody.innerHTML = `<tr><td colspan="5">No records found</td></tr>`;
                return;
            }

            data.data.forEach(r => {

                tableBody.innerHTML += `
                    <tr>
                        <td>${r.id}</td>
                        <td>${r.full_name}</td>
                        <td>${r.course}</td>
                        <td>${r.status}</td>
                        <td>${r.date}</td>
                    </tr>
                `;
            });

        })
        .catch(err => {
            console.error(err);
            alert("Server error while filtering");
        });

    });

});