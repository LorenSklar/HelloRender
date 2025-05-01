async function sendGreeting() {
    const name = document.getElementById('name').value;
    const language = document.getElementById('language').value;
    const resultDiv = document.getElementById('result');

    // Construct the full URL with the correct Flask server port
    const apiUrl = new URL('/api/v1/greet', 'https://hellorender-ft25.onrender.com');

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

async function toggleLanguage() {
    const currentLanguage = document.getElementById('language').value;
    const languages = ['en', 'es', 'fr', 'de', 'it'];
    const currentIndex = languages.indexOf(currentLanguage);
    const nextIndex = (currentIndex + 1) % languages.length; 
    const nextLanguage = languages[nextIndex];
    document.getElementById('language').value = nextLanguage;
    document.getElementById('language-link').innerText = {
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'it': 'Italian'
    }[nextLanguage];
}
