document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("profileForm");

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        let username = document.getElementById("nameInput").value;
        let email = document.getElementById("emailInput").value;
        let phone = document.getElementById("phoneInput").value;

        fetch("/profile/update", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username,
                email,
                phone
            })
        })
        .then(res => res.json())
        .then(data => {

            showMessage(data.message || "Profile updated");

            document.getElementById("displayName").innerText = username;

        });

    });

});

const changePhotoBtn = document.getElementById("changePhotoBtn");
const photoInput = document.getElementById("photoInput");
changePhotoBtn.addEventListener("click", function () {
    photoInput.click();
});
photoInput.addEventListener("change", function () {

    let file = photoInput.files[0];

    if (!file) return;

    let formData = new FormData();
    formData.append("image", file);

    fetch("/profile/upload-image", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {

        showMessage(data.message || "Image updated");

        // instantly update preview
        document.querySelector(".profile-image img").src =
            URL.createObjectURL(file);

    });

});