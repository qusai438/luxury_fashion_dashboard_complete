document.addEventListener("DOMContentLoaded", async () => {
  const container = document.getElementById("recommendationsContainer");

  try {
    const response = await fetch("/api/recommendations/products");
    const data = await response.json();

    if (response.ok && Array.isArray(data.recommendations)) {
      data.recommendations.forEach(product => {
        const col = document.createElement("div");
        col.className = "col-md-4";

        col.innerHTML = `
          <div class="card shadow-sm h-100">
            <div class="card-body">
              <h5 class="card-title">${product.name}</h5>
              <p class="card-text">Price: €${product.price.toFixed(2)}</p>
              <button class="btn btn-outline-primary w-100">View</button>
            </div>
          </div>
        `;

        container.appendChild(col);
      });
    } else {
      container.innerHTML = `<div class="col-12"><p class="text-danger">Failed to load recommendations.</p></div>`;
    }
  } catch (err) {
    console.error("Recommendation error:", err);
    container.innerHTML = `<div class="col-12"><p class="text-danger">An unexpected error occurred.</p></div>`;
  }
});
