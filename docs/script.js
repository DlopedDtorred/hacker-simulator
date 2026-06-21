// ============================================================
// Hacker Simulator 2077 - Website Scripts
// ============================================================

// 1. Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ============================================================
// 2. GET LATEST VERSION FROM GITHUB API
// ============================================================
async function getLatestVersion() {
    try {
        const response = await fetch('https://api.github.com/repos/DlopedDtorred/hacker-simulator/releases/latest');
        if (!response.ok) throw new Error('Network response was not ok');
        const data = await response.json();
        return data.tag_name || 'v10.0.0';
    } catch (error) {
        console.log('Could not fetch latest version:', error);
        return 'v10.0.0';
    }
}

async function updateVersionDisplay() {
    const version = await getLatestVersion();
    const displays = document.querySelectorAll('#version-display, #download-version, #footer-version');
    displays.forEach(el => {
        if (el) el.textContent = version;
    });
    const badge = document.querySelector('.hero-badge');
    if (badge) {
        badge.innerHTML = `⚡ ${version} · Ultimate Edition`;
    }
}

// ============================================================
// 3. GET STARS AND DOWNLOADS FROM GITHUB API
// ============================================================
async function getGitHubStats() {
    try {
        // Get repo info (stars)
        const repoResponse = await fetch('https://api.github.com/repos/DlopedDtorred/hacker-simulator');
        if (!repoResponse.ok) throw new Error('Network response was not ok');
        const repoData = await repoResponse.json();

        const stars = repoData.stargazers_count || 0;
        const starElement = document.getElementById('stat-stars');
        if (starElement) starElement.textContent = `⭐ ${stars}`;
        const starCountElement = document.getElementById('star-count');
        if (starCountElement) starCountElement.textContent = stars;

        // Get downloads from all releases
        try {
            const releasesResponse = await fetch('https://api.github.com/repos/DlopedDtorred/hacker-simulator/releases');
            if (releasesResponse.ok) {
                const releases = await releasesResponse.json();
                let totalDownloads = 0;
                
                releases.forEach(release => {
                    if (release.assets) {
                        release.assets.forEach(asset => {
                            totalDownloads += asset.download_count || 0;
                        });
                    }
                });
                
                const downloadElement = document.getElementById('download-count');
                if (downloadElement) downloadElement.textContent = totalDownloads || 0;
            }
        } catch (e) {
            console.log('Could not fetch download stats:', e);
            const downloadElement = document.getElementById('download-count');
            if (downloadElement) downloadElement.textContent = '?';
        }
    } catch (error) {
        console.log('Could not fetch GitHub stats:', error);
        const starElement = document.getElementById('stat-stars');
        if (starElement) starElement.textContent = '⭐ ?';
        const downloadElement = document.getElementById('download-count');
        if (downloadElement) downloadElement.textContent = '?';
    }
}

// ============================================================
// 4. THEME TOGGLE
// ============================================================
function initTheme() {
    const savedTheme = localStorage.getItem('hacker-theme') || 'dark';
    if (savedTheme === 'light') {
        document.body.classList.add('light-mode');
        const toggle = document.getElementById('themeToggle');
        if (toggle) toggle.innerHTML = '<i class="fas fa-sun"></i>';
    } else {
        document.body.classList.remove('light-mode');
        const toggle = document.getElementById('themeToggle');
        if (toggle) toggle.innerHTML = '<i class="fas fa-moon"></i>';
    }
}

function toggleTheme() {
    const isLight = document.body.classList.toggle('light-mode');
    localStorage.setItem('hacker-theme', isLight ? 'light' : 'dark');
    const toggle = document.getElementById('themeToggle');
    if (toggle) {
        toggle.innerHTML = isLight ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
    }
}

// ============================================================
// 5. TYPING EFFECT
// ============================================================
function initTyping() {
    const texts = [
        'Aprende hacking ético jugando en tu terminal',
        'Learn ethical hacking by playing in your terminal',
        'Hack servers, evade firewalls, crack passwords',
        '20 servers · 25+ achievements · Open Source'
    ];
    let textIndex = 0;
    let charIndex = 0;
    const element = document.getElementById('typing-text');
    if (!element) return;
    let isDeleting = false;

    function type() {
        const currentText = texts[textIndex];
        if (isDeleting) {
            element.innerHTML = currentText.substring(0, charIndex - 1) + '<span class="cursor"></span>';
            charIndex--;
            if (charIndex === 0) {
                isDeleting = false;
                textIndex = (textIndex + 1) % texts.length;
                setTimeout(type, 1000);
                return;
            }
            setTimeout(type, 30);
        } else {
            element.innerHTML = currentText.substring(0, charIndex + 1) + '<span class="cursor"></span>';
            charIndex++;
            if (charIndex === currentText.length) {
                isDeleting = true;
                setTimeout(type, 3000);
                return;
            }
            setTimeout(type, 50);
        }
    }

    type();
}

// ============================================================
// 6. SCROLL ANIMATIONS
// ============================================================
function initScrollAnimations() {
    const elements = document.querySelectorAll('.animate-on-scroll');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    elements.forEach(el => observer.observe(el));
}

// ============================================================
// 7. PROGRESS BAR
// ============================================================
function initProgressBar() {
    const progressBar = document.getElementById('progress-bar');
    if (!progressBar) return;
    window.addEventListener('scroll', () => {
        const scrollTop = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = (scrollTop / docHeight) * 100;
        progressBar.style.width = progress + '%';
    });
}

// ============================================================
// 8. BACK TO TOP
// ============================================================
function initBackToTop() {
    const btn = document.getElementById('back-to-top');
    if (!btn) return;
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            btn.classList.add('show');
        } else {
            btn.classList.remove('show');
        }
    });
    btn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

// ============================================================
// 9. FAQ ACCORDION
// ============================================================
function initFAQ() {
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        if (!question) return;
        question.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            faqItems.forEach(i => i.classList.remove('active'));
            if (!isActive) {
                item.classList.add('active');
            }
        });
    });
}

// ============================================================
// 10. LANGUAGE TOGGLE FOR GUIDES
// ============================================================
function initGuideLangToggle() {
    const toggle = document.getElementById('langToggle');
    if (!toggle) return;
    
    let currentLang = 'es';
    const label = document.getElementById('langLabel');
    const esContent = document.getElementById('content-es');
    const enContent = document.getElementById('content-en');
    
    toggle.addEventListener('click', function() {
        if (currentLang === 'es') {
            if (esContent) esContent.style.display = 'none';
            if (enContent) enContent.style.display = 'block';
            if (label) label.textContent = '🇬🇧 EN';
            currentLang = 'en';
        } else {
            if (esContent) esContent.style.display = 'block';
            if (enContent) enContent.style.display = 'none';
            if (label) label.textContent = '🇪🇸 ES';
            currentLang = 'es';
        }
    });
}

// ============================================================
// 11. INIT ALL
// ============================================================
document.addEventListener('DOMContentLoaded', function() {
    initTheme();
    updateVersionDisplay();
    getGitHubStats();
    initTyping();
    initScrollAnimations();
    initProgressBar();
    initBackToTop();
    initFAQ();
    initGuideLangToggle();

    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }
});
