document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("returnForm");
    const confirmation = document.getElementById("confirmation");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const orderId = document.getElementById("orderId").value.trim();
        const reason = document.getElementById("reason").value.trim();

        if (!orderId || !reason) {
            alert("Please fill out both fields.");
            return;
        }

        const payload = { order_id: orderId, reason };

        try {
            const response = await fetch("/api/returns/request", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });

            const data = await response.json();

            if (response.ok && data.status !== "error") {
                confirmation.classList.remove("d-none");
                form.reset();
            } else {
                alert(data.error || "Failed to submit return request.");
            }
        } catch (err) {
            console.error("Error submitting return request:", err);
            alert("An error occurred.");
        }
    });
});
