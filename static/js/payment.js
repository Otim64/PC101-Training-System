document.addEventListener("DOMContentLoaded", () => {

    console.log("Payments module loaded");

    const searchInput = document.getElementById("paymentSearch");

    if (!searchInput) return;

    searchInput.addEventListener("keyup", () => {

        fetch("/payments/search?query=" + searchInput.value)

            .then(response => response.json())

            .then(data => {

                const tbody = document.getElementById("paymentsTable");

                tbody.innerHTML = "";

                data.forEach(payment => {

                    tbody.innerHTML += `
                        <tr>
                            <td>${payment.id}</td>
                            <td>${payment.full_name}</td>
                            <td>${payment.amount}</td>
                            <td>${payment.date_paid}</td>
                            <td>${payment.description}</td>
                            <td><span class="status paid">Paid</span></td>
                        </tr>
                    `;

                });

            });

    });

});

document.addEventListener("DOMContentLoaded", function () {

    formatAllMoneyElements();

});