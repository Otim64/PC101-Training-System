document.addEventListener("DOMContentLoaded", function () {

    console.log("System page loaded");

    const statusMessage = document.getElementById("statusMessage");
    const networkBox = document.getElementById("networkBox");

    // =========================
    // 1. CHECK INTERNET STATUS
    // =========================

    function updateNetworkStatus() {

        if (navigator.onLine) {

            networkBox.innerText = "Status: Online";
            networkBox.classList.remove("offline");
            networkBox.classList.add("online");

            statusMessage.innerText = "You are connected to the system.";

        } else {

            networkBox.innerText = "Status: Offline";
            networkBox.classList.remove("online");
            networkBox.classList.add("offline");

            statusMessage.innerText = "No internet connection detected. Please check your network.";

        }
    }

    // Run on load
    updateNetworkStatus();

    // =========================
    // 2. REAL-TIME LISTENERS
    // =========================

    window.addEventListener("online", updateNetworkStatus);
    window.addEventListener("offline", updateNetworkStatus);

});