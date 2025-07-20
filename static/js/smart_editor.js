document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("editorForm");
    const instructionInput = document.getElementById("instruction");
    const resultContainer = document.getElementById("resultContainer");
    const previewBox = document.getElementById("previewBox");
    const rawCode = document.getElementById("rawCode");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();
        const instruction = instructionInput.value.trim();

        if (!instruction) {
            alert("Please enter an instruction.");
            return;
        }

        try {
            const response = await fetch("/api/smart-editor/generate-section", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ instruction })
            });

            const data = await response.json();

            if (response.ok && data.html) {
                resultContainer.classList.remove("d-none");
                previewBox.innerHTML = data.html;
                rawCode.textContent = data.html;
            } else {
                alert(data.error || "Failed to generate section.");
            }
        } catch (err) {
            console.error("Smart editor error:", err);
            alert("An unexpected error occurred.");
        }
    });
});
