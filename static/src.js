document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function() {
        // Example: You can perform validation or AJAX submission here if needed
        console.log('Form submitted');
    };
});

document.getElementById('enrollmentForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);
    const formObject = {};
    formData.forEach((value, key) => formObject[key] = value);

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formObject)
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
});
