document.addEventListener("DOMContentLoaded", async function () {
    const status = document.getElementById("status");
    const message = document.getElementById("message");
    const uptime = document.getElementById("uptime");
    const version = document.getElementById("version");

    try {
        const response = await fetch("/api/admin/status");
        const data = await response.json();

        if (response.ok) {
            status.textContent = data.status;
            message.textContent = data.message;
            uptime.textContent = data.uptime;
            version.textContent = data.version;
        } else {
            status.textContent = "ERROR";
            message.textContent = data.error || "Failed to fetch system status.";
        }
    } catch (err) {
        console.error("System status error:", err);
        status.textContent = "ERROR";
        message.textContent = "An unexpected error occurred.";
    }
});
