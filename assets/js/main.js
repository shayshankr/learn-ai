// Learn AI — shared behavior: theme toggle, active nav, lesson progress

(function () {
  const root = document.documentElement;
  const stored = localStorage.getItem('learnai-theme');
  if (stored) root.setAttribute('data-theme', stored);

  function currentTheme() {
    if (root.getAttribute('data-theme')) return root.getAttribute('data-theme');
    return window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
  }

  window.toggleTheme = function () {
    const next = currentTheme() === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    localStorage.setItem('learnai-theme', next);
    const btn = document.querySelector('.theme-toggle');
    if (btn) btn.textContent = next === 'dark' ? '☀️' : '🌙';
  };

  document.addEventListener('DOMContentLoaded', () => {
    const btn = document.querySelector('.theme-toggle');
    if (btn) btn.textContent = currentTheme() === 'dark' ? '☀️' : '🌙';

    // highlight active nav link
    const path = location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-links a').forEach(a => {
      if (a.getAttribute('href') && a.getAttribute('href').endsWith(path)) a.classList.add('active');
    });

    // mark current lesson as visited/complete on scroll-to-bottom or explicit button
    const lessonId = document.body.dataset.lesson;
    if (lessonId) {
      window.markLessonComplete = function () {
        const done = JSON.parse(localStorage.getItem('learnai-progress') || '{}');
        done[lessonId] = true;
        localStorage.setItem('learnai-progress', JSON.stringify(done));
        const marker = document.getElementById('complete-marker');
        if (marker) marker.textContent = '✓ Marked complete — nice work!';
      };
      const done = JSON.parse(localStorage.getItem('learnai-progress') || '{}');
      if (done[lessonId]) {
        const marker = document.getElementById('complete-marker');
        if (marker) marker.textContent = '✓ Already completed';
      }
    }
  });

  window.getProgress = function () {
    return JSON.parse(localStorage.getItem('learnai-progress') || '{}');
  };
})();
