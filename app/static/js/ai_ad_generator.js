document.addEventListener('DOMContentLoaded', function () {
    const generateBtn = document.getElementById('generateAdBtn');
    const imageUrlInput = document.getElementById('imageUrlInput');
    const resultBox = document.getElementById('adResultBox');
    const spinner = document.getElementById('loadingSpinner');

    generateBtn.addEventListener('click', async function () {
        const imageUrl = imageUrlInput.value.trim();
        if (!imageUrl) {
            alert("Please enter a valid image URL.");
            return;
        }

        spinner.style.display = 'inline-block';
        resultBox.textContent = '';

        try {
            const response = await fetch('/ai-media/generate-ad-from-image', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ image_url: imageUrl })
            });

            const data = await response.json();
            if (response.ok) {
                resultBox.textContent = data.ad_copy;
            } else {
                resultBox.textContent = data.error || "Something went wrong.";
            }
        } catch (err) {
            resultBox.textContent = "Request failed.";
        } finally {
            spinner.style.display = 'none';
        }
    });
});
