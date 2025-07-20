document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("emailForm");
    const successMsg = document.getElementById("successMsg");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const to = document.getElementById("to").value.trim();
        const subject = document.getElementById("subject").value.trim();
        const body = document.getElementById("body").value.trim();

        if (!to || !subject || !body) {
            alert("Please fill in all fields.");
            return;
        }

        try {
            const response = await fetch("/api/email/send", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ to, subject, body })
            });

            const data = await response.json();

            if (response.ok && data.status === "sent") {
                successMsg.classList.remove("d-none");
                form.reset();
            } else {
                alert(data.error || "Failed to send email.");
            }
        } catch (err) {
            console.error("Email sending error:", err);
            alert("An unexpected error occurred.");
        }
    });
});
