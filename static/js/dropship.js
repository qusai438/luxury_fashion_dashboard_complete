document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("importForm");
    const list = document.getElementById("importedList");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const category = document.getElementById("category").value.trim();
        if (!category) {
            alert("Please enter a category.");
            return;
        }

        try {
            const response = await fetch("/api/dropship/import", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ category })
            });

            const data = await response.json();
            list.innerHTML = "";

            if (response.ok && Array.isArray(data.imported)) {
                if (data.imported.length === 0) {
                    list.innerHTML = "<li class='list-group-item text-muted'>No products found in this category.</li>";
                } else {
                    data.imported.forEach(product => {
                        const li = document.createElement("li");
                        li.className = "list-group-item";
                        li.textContent = `${product.title} (ID: ${product.id})`;
                        list.appendChild(li);
                    });
                }
            } else {
                alert(data.error || "Failed to import products.");
            }
        } catch (err) {
            console.error("Import error:", err);
            alert("An unexpected error occurred.");
        }
    });
});
