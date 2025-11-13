window.onload = function (){
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

}