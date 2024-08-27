function deleteNote(noteId) {
    fetch('/profile', {
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


function deleteProfile() {
    if (confirm('Are you sure you want to delete your profile? This action cannot be undone.')) {
        fetch("{{ url_for('auth.delete_profile') }}", {
            method: "POST",
            body: JSON.stringify({})
        }).then(response => response.json())
          .then(data => {
              if (data.message) {
                  alert(data.message);
                  window.location.href = "{{ url_for('auth.login') }}";  // Redirect to login page after deletion
              } else if (data.error) {
                  alert(data.error);
              }
          })
          .catch(error => {
              console.error("Error:", error);
          });
    }
}
