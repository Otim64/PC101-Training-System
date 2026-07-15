function formatMoney(value) {

    if (value === null || value === undefined || value === "") {
        return "0";
    }

    return Number(value).toLocaleString("en-US");
}

function formatAllMoneyElements() {

    const elements = document.querySelectorAll(".money");

    elements.forEach(el => {

        let rawValue;

        // CASE 1: has data-value (cards, dashboard)
        if (el.getAttribute("data-value")) {
            rawValue = el.getAttribute("data-value");
        }

        // CASE 2: normal table cell text
        else {
            rawValue = el.innerText.replace("UGX", "").trim();
        }

        el.innerText = "UGX " + formatMoney(rawValue);
    });
}