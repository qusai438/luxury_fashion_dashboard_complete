document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("mediaForm");
    const result = document.getElementById("result");
    const outputImage = document.getElementById("outputImage");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const imageUrl = document.getElementById("imageUrl").value.trim();
        const action = e.submitter?.dataset?.action;

        if (!imageUrl || !action) {
            alert("Please provide an image URL and select an action.");
            return;
        }

        const endpoint = action === "upscale" ? "/api/ai-media/upscale" : "/api/ai-media/enhance";

        try {
            const response = await fetch(endpoint, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ image_url: imageUrl })
            });

            const data = await response.json();

            if (response.ok && data.enhanced_url) {
                outputImage.src = data.enhanced_url;
                result.classList.remove("d-none");
            } else {
                alert(data.error || "Failed to process image.");
            }
        } catch (err) {
            console.error("AI media processing error:", err);
            alert("An unexpected error occurred.");
        }
    });
});
