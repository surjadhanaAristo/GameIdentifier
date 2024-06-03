// Open the modal
function openModal() {
    document.getElementById('modal').style.display = 'block';
}

// Close the modal
function closeModal() {
    document.getElementById('modal').style.display = 'none';
}

// Close the modal when clicking outside of the modal content
window.onclick = function(event) {
    var modal = document.getElementById('modal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

// Register a new user
function registerUser(event) {
    event.preventDefault();
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    var users = JSON.parse(localStorage.getItem('users')) || [];
    users.push({ username: username, email: email, password: password });
    localStorage.setItem('users', JSON.stringify(users));

    alert('Registration successful!');
    closeModal();
}

// Login a user
function loginUser(event) {
    event.preventDefault();
    var email = document.getElementById('login-email').value;
    var password = document.getElementById('login-password').value;

    var users = JSON.parse(localStorage.getItem('users')) || [];
    var user = users.find(user => user.email === email && user.password === password);

    if (user) {
        alert('Login successful!');
        window.location.href = 'dashboard.html';
    } else {
        alert('Invalid email or password.');
    }
}

// Logout function
function logout() {
    alert('Logged out successfully!');
    window.location.href = 'index.html';
}

// Try AI function
function tryAI() {
    alert('AI functionality will be implemented here.');
}
