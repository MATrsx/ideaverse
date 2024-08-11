function render_image (src, height=16, width=16) {
    return `<img src="${src}" height="${height}" width="${width}">`;
}

module.exports = render_image;