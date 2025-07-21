document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("returnForm");
  const responseBox = document.getElementById("responseBox");

  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const orderId = document.getElementById("orderId").value.trim();
    const reason = document.getElementById("reason").value.trim();

    if (!orderId || !reason) {
      showResponse("Please fill in all fields.", false);
      return;
    }

    try {
      const response = await fetch("/returns/request", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ order_id: orderId, reason: reason })
      });

      const result = await response.json();
      if (response.ok) {
        showResponse(result.message || "Return request submitted successfully.", true);
        form.reset();
      } else {
        showResponse(result.error || "An error occurred while processing your request.", false);
      }
    } catch (err) {
      showResponse("Unexpected error occurred.", false);
    }
  });

  function showResponse(message, success) {
    responseBox.classList.remove("d-none", "alert-success", "alert-danger");
    responseBox.classList.add(success ? "alert-success" : "alert-danger");
    responseBox.textContent = message;
  }
});
