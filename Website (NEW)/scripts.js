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
