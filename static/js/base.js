document.addEventListener("DOMContentLoaded", function () {

    const links = document.querySelectorAll(".sidebar nav a");

    links.forEach(link => {

        if (link.href === window.location.href) {
            link.style.backgroundColor = "#1d3557";
            link.style.borderRadius = "8px";
        }

    });

});

document.addEventListener("DOMContentLoaded", function () {

    const logoutLink = document.querySelector('a[href="/logout"]');

    if (logoutLink) {
        logoutLink.addEventListener("click", function (e) {

            const confirmLogout = confirm("Are you sure you want to logout?");

            if (!confirmLogout) {
                e.preventDefault();
            }

        });
    }

});

document.addEventListener("DOMContentLoaded", function () {

    document.body.style.opacity = "0";
    document.body.style.transition = "0.3s ease-in-out";

    setTimeout(() => {
        document.body.style.opacity = "1";
    }, 50);

});

function showMessage(message) {

    const box = document.createElement("div");

    box.innerText = message;

    box.style.position = "fixed";
    box.style.top = "20px";
    box.style.right = "20px";
    box.style.background = "#1d4ed8";
    box.style.color = "white";
    box.style.padding = "10px 15px";
    box.style.borderRadius = "8px";
    box.style.zIndex = "9999";

    document.body.appendChild(box);

    setTimeout(() => {
        box.remove();
    }, 3000);
}