document.addEventListener("DOMContentLoaded", function () {
    const socket = io("/livechat");
    const form = document.getElementById("liveChatForm");
    const input = document.getElementById("chatInput");
    const chatbox = document.getElementById("chatbox");

    function appendMessage(sender, message) {
        const msg = document.createElement("div");
        msg.classList.add("mb-2");
        msg.innerHTML = `<strong>${sender}:</strong> ${message}`;
        chatbox.appendChild(msg);
        chatbox.scrollTop = chatbox.scrollHeight;
    }

    socket.on("connect", () => {
        appendMessage("System", "✅ Connected to live chat.");
    });

    socket.on("status", (data) => {
        appendMessage("System", data.message);
    });

    socket.on("message", (data) => {
        appendMessage(data.user || "Visitor", data.message);
    });

    form.addEventListener("submit", function (e) {
        e.preventDefault();
        const message = input.value.trim();
        if (!message) return;

        socket.emit("message", { user: "You", message });
        appendMessage("You", message);
        input.value = "";
    });
});
