document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Replace with your actual database check logic
    const dbUsername = 'admin';
    const dbPassword = 'password123';

    if (username === dbUsername && password === dbPassword) {
        alert('Login successful!');
        // Redirect to another page or perform other actions
    } else {
        alert('Invalid username or password.');
    }
});