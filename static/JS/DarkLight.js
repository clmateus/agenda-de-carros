function toggleTheme() {
    const html = document.documentElement;
    const btn = document.getElementById('theme-toggle');

    if (html.getAttribute('data-theme') === 'dark') {
        html.removeAttribute('data-theme');
        localStorage.setItem('theme', 'light');
        if (btn) btn.textContent = '🌙 Dark';
    } else {
        html.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        if (btn) btn.textContent = '☀️ Light';
    }
}

// Aplica o tema salvo ao carregar a página
document.addEventListener('DOMContentLoaded', () => {
    const saved = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const btn = document.getElementById('theme-toggle');

    if (saved === 'dark' || (!saved && prefersDark)) {
        document.documentElement.setAttribute('data-theme', 'dark');
        if (btn) btn.textContent = '☀️ Light';
    }
});