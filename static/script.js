function generateStory() {
    const userInput = document.getElementById('userInput').value;
    fetch('/generate-story', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('storyOutput').textContent = data.story;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('storyOutput').textContent = 'Failed to generate story.';
    });
}
