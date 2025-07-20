document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("contentForm");
    const resultBox = document.getElementById("result");
    const outputText = document.getElementById("outputText");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const title = document.getElementById("title").value.trim();
        const description = document.getElementById("description").value.trim();
        const action = e.submitter?.dataset?.action;

        if (!title) {
            alert("Please enter a product title.");
            return;
        }

        let endpoint = "";
        let payload = { title };

        if (action === "description") {
            endpoint = "/api/ai-content/generate-description";
        } else if (action === "caption") {
            endpoint = "/api/ai-content/generate-caption";
        } else if (action === "ad") {
            if (!description) {
                alert("Please enter a product description for the ad copy.");
                return;
            }
            endpoint = "/api/ai-content/generate-ad-copy";
            payload.description = description;
        } else {
            alert("Invalid action.");
            return;
        }

        try {
            const response = await fetch(endpoint, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });

            const data = await response.json();

            if (response.ok) {
                outputText.textContent =
                    data.description || data.caption || data.ad_copy || "No content returned.";
                resultBox.classList.remove("d-none");
            } else {
                alert(data.error || "Failed to generate content.");
            }
        } catch (err) {
            console.error("AI content error:", err);
            alert("Something went wrong.");
        }
    });
});
