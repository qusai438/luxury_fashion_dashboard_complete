document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("videoForm");
    const result = document.getElementById("result");
    const videoPlayer = document.getElementById("videoPlayer");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const title = document.getElementById("title").value.trim();
        const description = document.getElementById("description").value.trim();

        if (!title || !description) {
            alert("Please enter both title and description.");
            return;
        }

        const payload = {
            product_info: { title, description }
        };

        try {
            const response = await fetch("/api/video/generate", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });

            const data = await response.json();

            if (response.ok && data.video_url) {
                videoPlayer.src = data.video_url;
                result.classList.remove("d-none");
            } else {
                alert(data.error || "Failed to generate video.");
            }
        } catch (err) {
            console.error("Error generating video:", err);
            alert("An error occurred while generating the video.");
        }
    });
});
