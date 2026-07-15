document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    form.addEventListener("submit", function () {

        console.log("Login attempt sent to server...");

    });

});

document.addEventListener("DOMContentLoaded", function () {
    const alertBox = document.querySelector(".alert");
    if (alertBox) {
        setTimeout(() => {
            alertBox.style.opacity = "0";
            setTimeout(() => {
                alertBox.remove();
            }, 500);
        }, 3000); // 3 seconds
    }
});
