const matrixContainer = document.getElementById('matrix');
const columns = Math.floor(matrixContainer.clientWidth / 15); // Reduced the column width to increase the number of columns
let drops = Array(columns).fill(0);

function matrixEffect() {
    matrixContainer.innerHTML = ''; // Clear existing content

    drops.forEach((y, index) => {
        const text = String.fromCharCode(65 + Math.random() * 57); // Generate letters (A-Z, a-z)
        const x = index * 15; // Adjusted x position for more columns
        const span = document.createElement('span');

        span.textContent = text;
        span.style.cssText = `position:absolute; left:${x}px; top:${y}px; color:#0F0; font-family:Retro Computer;`;

        matrixContainer.appendChild(span);

        // Randomly reset to the top of the screen or move the character down
        drops[index] = y > matrixContainer.clientHeight + Math.random() * 5000 ? 0 : y + 15; // Decreased the step to increase density
    });
}

let intervalId;

function startMatrixEffect() {
    if (intervalId) {
        clearInterval(intervalId);
    }
    intervalId = setInterval(matrixEffect, 50);
}

function stopMatrixEffect() {
    clearInterval(intervalId);
    matrixContainer.innerHTML = '';
}

// Listen for form submission
document.getElementById('crack-form').addEventListener('submit', function (e) {
    e.preventDefault();
    submitForm();
    startMatrixEffect(); // Start the Matrix effect when the form is submitted
});
