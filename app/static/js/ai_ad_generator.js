document.addEventListener("DOMContentLoaded", function () {
  const generateBtn = document.getElementById("generateAdBtn");
  const resultBox = document.getElementById("adResultBox");
  const loading = document.getElementById("loadingSpinner");

  generateBtn.addEventListener("click", async function () {
    const imageUrl = document.getElementById("imageUrlInput").value.trim();

    if (!imageUrl) {
      alert("Please enter a product image URL.");
      return;
    }

    loading.style.display = "inline-block";
    resultBox.innerText = "";

    try {
      const response = await fetch("/ai_media/generate/ad-copy", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ image_url: imageUrl }),
      });

      const data = await response.json();

      if (response.ok) {
        resultBox.innerText = data.ad_copy;
      } else {
        resultBox.innerText = "Error: " + data.error;
      }
    } catch (error) {
      resultBox.innerText = "An error occurred while generating the ad.";
    } finally {
      loading.style.display = "none";
    }
  });
});
