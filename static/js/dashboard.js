document.addEventListener("DOMContentLoaded", function () {

    console.log("Dashboard loaded successfully");

    // -------------------------------
    // 1. Animate cards on load
    // -------------------------------
    const cards = document.querySelectorAll(".card");

    cards.forEach((card, index) => {

        card.style.opacity = "0";
        card.style.transform = "translateY(20px)";

        setTimeout(() => {
            card.style.transition = "0.4s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, 150 * index);

    });

    // -------------------------------
    // 2. Highlight important stats (future-ready)
    // -------------------------------
    const studentCard = document.querySelector(".card h3");

    if (studentCard && studentCard.innerText === "Students") {
        studentCard.style.color = "#1d4ed8";
    }

    // -------------------------------
    // 3. Table row hover effect enhancement
    // -------------------------------
    const rows = document.querySelectorAll("table tr");

    rows.forEach(row => {

        row.addEventListener("mouseenter", function () {
            this.style.backgroundColor = "#f1f5f9";
        });

        row.addEventListener("mouseleave", function () {
            this.style.backgroundColor = "transparent";
        });

    });

    // -------------------------------
    // 4. Format Money Values
    // -------------------------------
    const moneyElements = document.querySelectorAll(".money");

    moneyElements.forEach(element => {

        const value = parseFloat(element.dataset.value || 0);

        element.textContent =
            "UGX " + value.toLocaleString("en-UG", {
                minimumFractionDigits: 0,
                maximumFractionDigits: 0
            });

    });

});

