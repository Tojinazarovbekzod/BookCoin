window.addEventListener("load", function () {
    let int2 = document.getElementById("int2");
    let toggle = document.getElementById("toggle");

    toggle.addEventListener("click", () => {
        if (int2.type === "password") {
            int2.type = "text";
            toggle.src = "/static/images/eye2.png";
        } else {
            int2.type = "password";
            toggle.src = "/static/images/eye1.png";
        }
        toggle.style.width = "40px";
        toggle.style.height = "40px";
    });

    document.getElementById("loginForm").addEventListener("submit", async function (e) {
        e.preventDefault();

        const data = {
            username: document.getElementById("int1").value,
            password: document.getElementById("int2").value
        };

        try {
            const response = await fetch("/api/login/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (result.success) {
                alert("✅ Login muvaffaqiyatli: " + result.username);
                window.location.href = "/main/";
            } else {
                alert("❌ Xatolik: " + (result.error || "Noto'g'ri ma'lumot"));
            }
        } catch (err) {
            alert("⚠️ Serverga ulanib bo'lmadi!");
            console.error(err);
        }
    });
});
