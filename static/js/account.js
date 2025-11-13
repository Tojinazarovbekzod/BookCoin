window.addEventListener("load", function () {
    let input1 = document.getElementById("input1");
    let toggle = document.getElementById("toggle");

    toggle.addEventListener("click", () => {
        if (input1.type === "password") {
            input1.type = "text";
            toggle.src = "/static/images/eye2.png";
        } else {
            input1.type = "password";
            toggle.src = "/static/images/eye1.png";
        }
        toggle.style.width = "30px";
        toggle.style.height = "30px";
    });

    document.getElementById("registerform").addEventListener("submit", async function (e) {
        e.preventDefault();

        const data = {
            username: document.getElementById("int1").value,
            surname: document.getElementById("int2").value,
            email: document.getElementById("int3").value,
            password: document.getElementById("input1").value
        };

        try {
            const response = await fetch("/api/signup/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (result.success) {
                alert("✅Ro'yxatdan o'tish muvaffaqiyatli!");
                window.location.href = "/login/";
            } else {
                alert("❌Xatolik: " + (result.error || "Notog'ri ma'lumot"));
            }
        } catch (err) {
            alert("Server bilan bog'lanishda xato");
            console.error(err);
        }
    });
});
