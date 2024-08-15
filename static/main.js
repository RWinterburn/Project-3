function deleteNote(noteId) {
    fetch('/delete-note', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ noteId: noteId })
    })
    .then(response => {
        if (!response.ok) {
            return response.text().then(text => { // Get the response as text
                throw new Error(text); // Throw an error with the response text
            });
        }
        return response.json(); // Parse the JSON response
    })
    .then(data => {
        if (data.message) {
            alert(data.message); // Notify the user of success
            location.reload(); // Reload the page to reflect changes
        } else if (data.error) {
            alert(data.error); // Notify the user of the error
        }
    })
    .catch(error => {
        console.error('Error:', error); // Log any errors
        alert('An unexpected error occurred'); // Notify the user of unexpected errors
    });
}
