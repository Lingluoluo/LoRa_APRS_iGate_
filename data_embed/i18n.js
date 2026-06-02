// Minimal i18n - server handles all translation via %KEY% replacement.
// This script only manages the language cookie for switching.
(function() {
    const select = document.getElementById('lang-select');
    if (!select) return;

    // Read current lang from cookie
    const cookieLang = document.cookie.match(/(?:^|;\s*)lang=([^;]+)/);
    if (cookieLang) {
        select.value = cookieLang[1];
    }

    // Switch language: set cookie and reload
    select.addEventListener('change', function() {
        document.cookie = 'lang=' + this.value + ';path=/;max-age=31536000';
        location.reload();
    });
})();
