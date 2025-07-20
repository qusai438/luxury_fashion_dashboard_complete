document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("chatForm");
    const input = document.getElementById("messageInput");
    const chatbox = document.getElementById("chatbox");

    function appendMessage(sender, text) {
        const msg = document.createElement("div");
        msg.classList.add("mb-2");

        msg.innerHTML = `<strong>${sender}:</strong> ${text}`;
        chatbox.appendChild(msg);
        chatbox.scrollTop = chatbox.scrollHeight;
    }

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const userMessage = input.value.trim();
        if (!userMessage) return;

        appendMessage("You", userMessage);
        input.value = "";

        try {
            const response = await fetch("/api/chatbot/ask", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userMessage })
            });

            const data = await response.json();

            if (response.ok && data.reply) {
                appendMessage("Bot", data.reply);
            } else {
                appendMessage("Bot", data.error || "Something went wrong.");
            }
        } catch (err) {
            console.error("Chatbot error:", err);
            appendMessage("Bot", "An error occurred while contacting the server.");
        }
    });
});
