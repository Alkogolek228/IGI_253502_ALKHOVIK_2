document.addEventListener("DOMContentLoaded", function() {
    const toggleControls = document.getElementById('toggle-controls');
    const styleControls = document.getElementById('style-controls');
    const fontSizeInput = document.getElementById('font-size');
    const textColorInput = document.getElementById('text-color');
    const backgroundColorInput = document.getElementById('background-color');

    toggleControls.addEventListener('change', function() {
        styleControls.style.display = this.checked ? 'block' : 'none';
    });

    fontSizeInput.addEventListener('input', function() {
        document.body.style.fontSize = this.value + 'px';
    });

    textColorInput.addEventListener('input', function() {
        document.body.style.color = this.value;
    });

    backgroundColorInput.addEventListener('input', function() {
        document.body.style.backgroundColor = this.value;
    });
});