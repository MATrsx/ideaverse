function render_image () {
    document.querySelectorAll('.suggestion-item').forEach(function(item) {
        if (item.textContent.includes('Float right')) {
            item.innerHTML = '👉 ' + item.innerHTML;
        }
    });
}

module.exports = render_image;