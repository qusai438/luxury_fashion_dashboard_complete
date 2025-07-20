document.addEventListener("DOMContentLoaded", async function () {
    const tableBody = document.getElementById("returnsBody");

    try {
        const response = await fetch("/api/returns/all");
        const data = await response.json();

        tableBody.innerHTML = "";

        if (response.ok && Array.isArray(data.returns)) {
            if (data.returns.length === 0) {
                tableBody.innerHTML = "<tr><td colspan='5' class='text-center text-muted'>No return requests found.</td></tr>";
            } else {
                data.returns.forEach(r => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${r.id}</td>
                        <td>${r.order_id}</td>
                        <td>${r.reason}</td>
                        <td>${r.status}</td>
                        <td>${new Date(r.requested_at).toLocaleString()}</td>
                    `;
                    tableBody.appendChild(row);
                });
            }
        } else {
            tableBody.innerHTML = "<tr><td colspan='5' class='text-danger'>Failed to load returns.</td></tr>";
        }
    } catch (err) {
        console.error("Error loading return requests:", err);
        tableBody.innerHTML = "<tr><td colspan='5' class='text-danger'>An error occurred.</td></tr>";
    }
});
