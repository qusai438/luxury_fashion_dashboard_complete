document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("reviewForm");
    const reviewsList = document.getElementById("reviewsList");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const productId = document.getElementById("productId").value.trim();
        const rating = parseInt(document.getElementById("rating").value);
        const comment = document.getElementById("comment").value.trim();

        if (!productId || !rating || !comment) {
            alert("Please fill out all fields.");
            return;
        }

        const payload = { product_id: productId, rating, comment };

        try {
            const response = await fetch("/api/reviews/submit", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload)
            });

            const data = await response.json();

            if (response.ok && data.review) {
                alert("Review submitted!");
                loadReviews(productId);
                form.reset();
            } else {
                alert(data.error || "Failed to submit review.");
            }
        } catch (err) {
            console.error("Error submitting review:", err);
            alert("An error occurred.");
        }
    });

    async function loadReviews(productId) {
        try {
            const response = await fetch(`/api/reviews/product/${productId}`);
            const data = await response.json();

            reviewsList.innerHTML = "";
            (data.reviews || []).forEach(review => {
                const li = document.createElement("li");
                li.classList.add("list-group-item");
                li.innerHTML = `<strong>${review.rating}★</strong> — ${review.comment}`;
                reviewsList.appendChild(li);
            });
        } catch (err) {
            console.error("Error loading reviews:", err);
        }
    }
});
