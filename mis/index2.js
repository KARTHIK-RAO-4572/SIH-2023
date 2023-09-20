// Function to handle adding videos
function addVideo() {
    const videoInput = document.getElementById('videoInput');
    const videoContainer = document.getElementById('videoContainer');

    if (videoInput.files.length === 0) {
        alert('Please select a video file.');
        return;
    }

    const videoFile = videoInput.files[0];
    const videoURL = URL.createObjectURL(videoFile);

    const videoElement = document.createElement('video');
    videoElement.src = videoURL;
    videoElement.controls = true;

    videoContainer.appendChild(videoElement);

    // Optionally, you can clear the input field after adding the video
    videoInput.value = '';
}

// Event listener for the "Add Video" button
document.getElementById('addVideo').addEventListener('click', addVideo);
