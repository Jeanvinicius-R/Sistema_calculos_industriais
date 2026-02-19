function toggleTheme() {
    const html = document.documentElement;
    const atual = html.getAttribute('data-theme');
    const novo = atual === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', novo);
    localStorage.setItem('tema', novo);
    document.getElementById('btn-theme').textContent = novo === 'dark' ? '🌙' : '☀️';
}

function toggleLayout() {
    const body = document.body;
    if (body.classList.contains('layout-top')) {
        body.classList.replace('layout-top', 'layout-side');
        localStorage.setItem('layout', 'side');
        document.getElementById('btn-layout').textContent = '⊟';
    } else {
        body.classList.replace('layout-side', 'layout-top');
        localStorage.setItem('layout', 'top');
        document.getElementById('btn-layout').textContent = '☰';
    }
}

window.onload = function () {
    const tema = localStorage.getItem('tema') || 'light';
    const layout = localStorage.getItem('layout') || 'top';

    document.documentElement.setAttribute('data-theme', tema);
    document.body.classList.add('layout-' + layout);

    document.getElementById('btn-theme').textContent = tema === 'dark' ? '🌙' : '☀️';
    document.getElementById('btn-layout').textContent = layout === 'side' ? '⊟' : '☰';
}