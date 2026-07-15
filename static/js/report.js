document.addEventListener("DOMContentLoaded", function () {

    const tableBody = document.getElementById("reportTable");

    const typeSelect = document.getElementById("reportType");
    const fromDate = document.getElementById("fromDate");
    const toDate = document.getElementById("toDate");

    function loadReports() {

        fetch("/reports/filter", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                type: typeSelect.value,
                from: fromDate.value,
                to: toDate.value
            })
        })
        .then(res => res.json())
        .then(data => {

            tableBody.innerHTML = "";

            if (!data.data.length) {
                tableBody.innerHTML = `
                    <tr>
                        <td colspan="5">No records found</td>
                    </tr>
                `;
                return;
            }

            data.data.forEach(r => {

                tableBody.innerHTML += `
                    <tr>
                        <td>${r.id}</td>
                        <td>${r.type}</td>
                        <td>${r.description}</td>
                        <td>${r.date}</td>
                        <td><span class="status">${r.status}</span></td>
                    </tr>
                `;
            });

        });

    }

    // 🔥 LIVE REACTIVITY (THIS IS WHAT YOU WERE MISSING)
    typeSelect.addEventListener("change", loadReports);
    fromDate.addEventListener("change", loadReports);
    toDate.addEventListener("change", loadReports);

    // initial load
    loadReports();

});

document.addEventListener("DOMContentLoaded", function () {

    formatAllMoneyElements();

});