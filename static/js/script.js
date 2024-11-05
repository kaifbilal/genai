document.querySelectorAll('.copy-button').forEach(button => {
    button.addEventListener('click', () => {
        // Select the code text inside the <pre><code> tag
        const code = button.nextElementSibling.innerText;
        
        // Copy the code to the clipboard
        navigator.clipboard.writeText(code).then(() => {
            // Change button text to "Copied!"
            button.textContent = 'Copied!';
            
            // Revert button text back to "Copy code" after 2 seconds
            setTimeout(() => {
                button.textContent = 'Copy code';
            }, 2000);
        }).catch(() => {
            alert('Failed to copy text.');
        });
    });
});
