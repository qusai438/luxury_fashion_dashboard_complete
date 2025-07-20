document.addEventListener("DOMContentLoaded", () => {
  const overviewList = document.getElementById("overviewList");
  const socialList = document.getElementById("socialList");
  const suggestionList = document.getElementById("suggestionList");

  fetch("/api/analytics/overview")
    .then(res => res.json())
    .then(data => {
      Object.entries(data).forEach(([key, value]) => {
        const li = document.createElement("li");
        li.className = "list-group-item";
        li.textContent = `${key.replace(/_/g, ' ')}: ${value}`;
        overviewList.appendChild(li);
      });
    })
    .catch(err => console.error("Overview error:", err));

  fetch("/api/analytics/social")
    .then(res => res.json())
    .then(data => {
      const metrics = data.metrics || {};
      const suggestions = data.suggestions || [];

      Object.entries(metrics).forEach(([key, value]) => {
        const li = document.createElement("li");
        li.className = "list-group-item";
        li.textContent = `${key}: ${value}`;
        socialList.appendChild(li);
      });

      suggestions.forEach(s => {
        const li = document.createElement("li");
        li.className = "list-group-item";
        li.textContent = s;
        suggestionList.appendChild(li);
      });
    })
    .catch(err => console.error("Social error:", err));
});
