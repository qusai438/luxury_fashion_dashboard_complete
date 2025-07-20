document.addEventListener("DOMContentLoaded", function () {
    const refreshBtn = document.getElementById("refreshBtn");
    const ordersBody = document.getElementById("ordersBody");

    async function loadOrders() {
        try {
            const response = await fetch("/api/orders/");
            const data = await response.json();

            ordersBody.innerHTML = "";

            if (response.ok && Array.isArray(data.orders)) {
                data.orders.forEach(order => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${order.id}</td>
                        <td>${order.customer}</td>
                        <td>$${order.total.toFixed(2)}</td>
                        <td>${order.status}</td>
                    `;
                    ordersBody.appendChild(row);
                });
            } else {
                ordersBody.innerHTML = "<tr><td colspan='4'>No orders found.</td></tr>";
            }
        } catch (err) {
            console.error("Error loading orders:", err);
            ordersBody.innerHTML = "<tr><td colspan='4'>Failed to load orders.</td></tr>";
        }
    }

    refreshBtn.addEventListener("click", loadOrders);

    // Load on page load
    loadOrders();
});
