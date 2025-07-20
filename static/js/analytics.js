document.addEventListener("DOMContentLoaded", async function () {
    const metricsContainer = document.getElementById("metrics");
    const suggestionsList = document.getElementById("suggestions");

    try {
        const response = await fetch("/api/analytics/analytics");
        const data = await response.json();

        const metrics = data.metrics || {};
        const suggestions = data.suggestions || [];

        // عرض المقاييس
        Object.entries(metrics).forEach(([key, value]) => {
            const col = document.createElement("div");
            col.className = "col-md-3";

            const card = document.createElement("div");
            card.className = "card text-center shadow-sm";

            card.innerHTML = `
                <div class="card-body">
                    <h5 class="card-title text-capitalize">${key}</h5>
                    <p class="card-text display-6 fw-bold">${value}</p>
                </div>
            `;

            col.appendChild(card);
            metricsContainer.appendChild(col);
        });

        // عرض الاقتراحات
        suggestions.forEach(text => {
            const li = document.createElement("li");
            li.className = "list-group-item";
            li.textContent = text;
            suggestionsList.appendChild(li);
        });
    } catch (err) {
        console.error("Failed to load analytics data:", err);
        metricsContainer.innerHTML = "<p class='text-danger'>Unable to load analytics data.</p>";
    }
});
