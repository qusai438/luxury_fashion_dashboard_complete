document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("adForm");
    const resultBox = document.getElementById("resultBox");
    const adOutput = document.getElementById("adOutput");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const title = document.getElementById("title").value.trim();
        const description = document.getElementById("description").value.trim();
        const audience = document.getElementById("audience").value.trim();

        if (!title || !description || !audience) {
            alert("Please fill in all fields.");
            return;
        }

        const payload = {
            product: { title, description, audience }
        };

        try {
            const response = await fetch("/api/ads/generate", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });

            const data = await response.json();

            if (response.ok && data.ad_copy) {
                adOutput.textContent = data.ad_copy;
                resultBox.classList.remove("d-none");
            } else {
                alert(data.error || "Failed to generate ad.");
            }
        } catch (err) {
            console.error("Ad generation error:", err);
            alert("An unexpected error occurred.");
        }
    });
});
