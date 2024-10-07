// Get API token from the DOM
const apiToken = document.getElementById('apiToken').textContent;

async function uploadImage() {
    const input = document.getElementById('imageInput');
    const file = input.files[0];
    if (!file) {
        alert('Please select an image file');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('/upload/', {
            method: 'POST',
            headers: {
                'X-API-Key': apiToken
            },
            body: formData
        });

        if (response.ok) {
            alert('Image uploaded successfully');
            loadImages();
        } else {
            const error = await response.json();
            alert(`Upload failed: ${error.detail}`);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while uploading the image');
    }
}

async function loadImages() {
    try {
        const response = await fetch('/images/', {
            headers: {
                'X-API-Key': apiToken
            }
        });

        if (response.ok) {
            const data = await response.json();
            const container = document.getElementById('imageContainer');
            container.innerHTML = '';

            data.images.forEach(image => {
                const img = document.createElement('img');
                img.src = `/static/uploads/${image}`;
                img.alt = image;
                img.style.maxWidth = '200px';
                img.style.margin = '10px';
                container.appendChild(img);
            });
        } else {
            console.error('Failed to load images');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// Load images on page load
loadImages();