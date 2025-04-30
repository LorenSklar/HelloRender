async function sendGreeting() {
    const name = document.getElementById('name').value;
    const language = document.getElementById('language').value;
    const resultDiv = document.getElementById('result');

    // Construct the full URL with the correct Flask server port
    const apiUrl = new URL('/api/v1/greet', 'http://localhost:5010');

    try {
        const response = await fetch(apiUrl.toString(), {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: name || 'World',
                language: language
            })
        });

        const data = await response.json();

        if (response.ok) {
            resultDiv.className = 'success';
            resultDiv.textContent = data.greeting;
        } else {
            resultDiv.className = 'error';
            resultDiv.textContent = `Error: ${data.error}`;
        }
    } catch (error) {
        console.error('Error details:', error);
        resultDiv.className = 'error';
        resultDiv.textContent = `Error: ${error.message}`;
    }
}