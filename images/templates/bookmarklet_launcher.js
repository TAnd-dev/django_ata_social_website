(function () {
    if (!window.bookmarklet) {
        const bookmarklet_js = document.body.appendChild(document.createElement('script'));
        bookmarklet_js.src = '//ata.com:8000/static/js/bookmarklet.js?r=' + Math.floor(Math.random() * 999999999999);
        window.bookmarklet = true;
    } else {
        bookmarkletLaunch();
    }
})();