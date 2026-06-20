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

// ============================================================
// 3. UPDATE VERSION DISPLAYS
// ============================================================
async function updateVersionDisplay() {
    const version = await getLatestVersion();
    
    // Update all version displays
    const displays = document.querySelectorAll('#version-display, #download-version, #footer-version');
    displays.forEach(el => {
        if (el) el.textContent = version;
    });
    
    // Update hero badge
    const badge = document.querySelector('.hero-badge');
    if (badge) {
        badge.innerHTML = `⚡ ${version} · Ultimate Edition`;
    }
}

// ============================================================
// 4. RUN ON PAGE LOAD
// ============================================================
document.addEventListener('DOMContentLoaded', function() {
    // Update version
    updateVersionDisplay();
    
    // Add year to footer (optional)
    const yearSpan = document.getElementById('year');
    if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }
});