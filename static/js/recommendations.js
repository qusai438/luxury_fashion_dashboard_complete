document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("recForm");
    const container = document.getElementById("recommendations");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const productId = document.getElementById("productId").value.trim();
        if (!productId) {
            alert("Please enter a product ID.");
            return;
        }

        try {
            const response = await fetch(`/api/recommendations/product/${productId}`);
            const data = await response.json();

            container.innerHTML = "";

            if (response.ok && Array.isArray(data.related)) {
                data.related.forEach(product => {
                    const card = document.createElement("div");
                    card.className = "col-md-4";

                    card.innerHTML = `
                        <div class="card h-100 shadow-sm">
                            <div class="card-body">
                                <h5 class="card-title">${product.title}</h5>
                                <p class="card-text">$${product.price}</p>
                                <button class="btn btn-outline-primary w-100">View Product</button>
                            </div>
                        </div>
                    `;

                    container.appendChild(card);
                });
            } else {
                container.innerHTML = "<p class='text-muted'>No recommendations found.</p>";
            }
        } catch (err) {
            console.error("Recommendation fetch error:", err);
            container.innerHTML = "<p class='text-danger'>Error loading recommendations.</p>";
        }
    });
});
