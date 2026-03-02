/* ================================
   PORTERGEIST ART - INTERACTIONS
   ================================ */

// Portfolio images data (REPLACE WITH REAL IMAGES)
const portfolioImages = [
    { id: 1, src: 'images/portfolio-1.jpg', category: 'neo-traditional', caption: 'Flying Eyeball' },
    { id: 2, src: 'images/portfolio-2.jpg', category: 'pop-culture', caption: 'Chef Kirby' },
    { id: 3, src: 'images/portfolio-3.jpg', category: 'traditional', caption: 'Floral Vase & Frog' },
    { id: 4, src: 'images/portfolio-4.jpg', category: 'traditional', caption: 'Devil Hand' },
    { id: 5, src: 'images/portfolio-5.jpg', category: 'traditional', caption: 'Mom & Dad Dagger Heart' },
    { id: 6, src: 'images/portfolio-6.jpg', category: 'traditional', caption: 'Strawberry Vine' },
    { id: 7, src: 'images/portfolio-7.jpg', category: 'traditional', caption: 'Valentine Flash Sheet' },
    { id: 8, src: 'images/portfolio-8.jpg', category: 'neo-traditional', caption: '"MEH" Candy Heart' },
    { id: 9, src: 'images/portfolio-9.jpg', category: 'traditional', caption: 'Floral Script Lettering' },
    { id: 10, src: 'images/portfolio-10.jpg', category: 'traditional', caption: 'Sacred Heart & Snake' },
    { id: 11, src: 'images/portfolio-11.jpg', category: 'pop-culture', caption: 'Dracula Snoopy' },
    { id: 12, src: 'images/portfolio-12.jpg', category: 'neo-traditional', caption: 'Cat Portrait' },
];

// Flash designs data (REPLACE WITH REAL IMAGES)
const flashDesigns = [
    { id: 1, src: 'images/flash-zappers-1.jpg', title: 'Zappers Board', size: 'Various', available: true },
    { id: 2, src: 'images/flash-zappers-2.jpg', title: 'Zappers Board Pt. 2', size: 'Various', available: true },
    { id: 3, src: 'images/flash-october.jpg', title: 'October Flash', size: 'Various', available: true },
    { id: 4, src: 'images/flash-halloween-1.jpg', title: 'Halloween Flash', size: 'Various', available: true },
    { id: 5, src: 'images/flash-halloween-2.jpg', title: 'Halloween Flash Pt. 2', size: 'Various', available: true },
];

// ================================
// NAVIGATION
// ================================

const navbar = document.getElementById('navbar');
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
const navLinks = document.querySelectorAll('.nav-link');

// Sticky navbar on scroll
window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Mobile menu toggle
navToggle.addEventListener('click', () => {
    navToggle.classList.toggle('active');
    navMenu.classList.toggle('active');
});

// Close mobile menu on link click
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navToggle.classList.remove('active');
        navMenu.classList.remove('active');
    });
});

// Smooth scroll offset for fixed nav
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const offset = 80;
            const targetPosition = target.offsetTop - offset;
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// ================================
// PORTFOLIO GALLERY
// ================================

const portfolioGallery = document.getElementById('portfolioGallery');
const filterBtns = document.querySelectorAll('.filter-btn');

// Render portfolio gallery
function renderPortfolio() {
    portfolioGallery.innerHTML = portfolioImages.map(img => `
        <div class="gallery-item" data-category="${img.category}" data-id="${img.id}">
            <img src="${img.src}" alt="${img.caption}" loading="lazy">
            <div class="gallery-item-overlay">
                <div class="gallery-item-caption">${img.caption}</div>
            </div>
        </div>
    `).join('');
    
    // Add click listeners for lightbox
    document.querySelectorAll('.gallery-item').forEach(item => {
        item.addEventListener('click', () => {
            const id = parseInt(item.dataset.id);
            openLightbox(id, portfolioImages);
        });
    });
}

// Filter portfolio
filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        const filter = btn.dataset.filter;
        
        // Update active button
        filterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        
        // Filter items
        const items = document.querySelectorAll('.gallery-item');
        items.forEach(item => {
            if (filter === 'all' || item.dataset.category === filter) {
                item.classList.remove('hidden');
            } else {
                item.classList.add('hidden');
            }
        });
    });
});

// ================================
// FLASH GALLERY
// ================================

const flashGrid = document.getElementById('flashGrid');

function renderFlash() {
    flashGrid.innerHTML = flashDesigns.map(flash => `
        <div class="flash-item" data-id="${flash.id}">
            <img src="${flash.src}" alt="${flash.title}" loading="lazy">
            <div class="flash-badge ${flash.available ? '' : 'claimed'}">
                ${flash.available ? 'Available' : 'Claimed'}
            </div>
            <div class="flash-item-info">
                <div class="flash-item-title">${flash.title}</div>
                <div class="flash-item-size">${flash.size}</div>
            </div>
        </div>
    `).join('');
    
    // Add click listeners for lightbox
    document.querySelectorAll('.flash-item').forEach(item => {
        item.addEventListener('click', () => {
            const id = parseInt(item.dataset.id);
            openLightbox(id, flashDesigns);
        });
    });
}

// ================================
// LIGHTBOX
// ================================

const lightbox = document.getElementById('lightbox');
const lightboxImage = document.getElementById('lightboxImage');
const lightboxCaption = document.getElementById('lightboxCaption');
const lightboxClose = document.getElementById('lightboxClose');
const lightboxPrev = document.getElementById('lightboxPrev');
const lightboxNext = document.getElementById('lightboxNext');

let currentImageIndex = 0;
let currentGallery = [];

function openLightbox(id, gallery) {
    currentGallery = gallery;
    currentImageIndex = gallery.findIndex(img => img.id === id);
    updateLightbox();
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
}

function updateLightbox() {
    const img = currentGallery[currentImageIndex];
    lightboxImage.src = img.src;
    lightboxImage.alt = img.caption || img.title || '';
    lightboxCaption.textContent = img.caption || img.title || '';
}

function showPrevImage() {
    currentImageIndex = (currentImageIndex - 1 + currentGallery.length) % currentGallery.length;
    updateLightbox();
}

function showNextImage() {
    currentImageIndex = (currentImageIndex + 1) % currentGallery.length;
    updateLightbox();
}

lightboxClose.addEventListener('click', closeLightbox);
lightboxPrev.addEventListener('click', showPrevImage);
lightboxNext.addEventListener('click', showNextImage);

// Close lightbox on background click
lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) {
        closeLightbox();
    }
});

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('active')) return;
    
    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') showPrevImage();
    if (e.key === 'ArrowRight') showNextImage();
});

// ================================
// CONSULTATION FORM
// ================================

const consultationForm = document.getElementById('consultationForm');
const fileInput = document.getElementById('references');
const fileInfo = document.getElementById('fileInfo');

// File input feedback
if (fileInput) {
    fileInput.addEventListener('change', (e) => {
        const files = e.target.files;
        if (files.length > 0) {
            fileInfo.textContent = `${files.length} file${files.length > 1 ? 's' : ''} selected`;
        } else {
            fileInfo.textContent = 'No files selected';
        }
    });
}

// Form submission (placeholder - needs backend)
if (consultationForm) {
    consultationForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Get form data
        const formData = new FormData(consultationForm);
        const data = Object.fromEntries(formData.entries());
        
        // TODO: Send to backend
        console.log('Form submission:', data);
        
        // Show success message (placeholder)
        alert('Thank you for your consultation request! I\'ll review your submission and get back to you within 24-48 hours.');
        
        // Reset form
        consultationForm.reset();
        fileInfo.textContent = 'No files selected';
    });
}

// ================================
// SCROLL REVEAL ANIMATIONS
// ================================

const revealElements = document.querySelectorAll('[data-scroll-reveal]');

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
            revealObserver.unobserve(entry.target);
        }
    });
}, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
});

revealElements.forEach(el => {
    revealObserver.observe(el);
});

// ================================
// INITIALIZE
// ================================

document.addEventListener('DOMContentLoaded', () => {
    renderPortfolio();
    renderFlash();
    
    // Trigger initial scroll reveal for hero
    const heroElements = document.querySelectorAll('#hero [data-scroll-reveal]');
    setTimeout(() => {
        heroElements.forEach(el => el.classList.add('revealed'));
    }, 300);
});

// ================================
// PLACEHOLDER IMAGE GENERATION
// ================================

// Generate placeholder images with gradient backgrounds
function generatePlaceholderImages() {
    const canvas = document.createElement('canvas');
    canvas.width = 600;
    canvas.height = 800;
    const ctx = canvas.getContext('2d');
    
    const gradients = [
        ['#1a0000', '#8B0000'],
        ['#0a0a0a', '#2a0000'],
        ['#1a1a1a', '#4a0000'],
        ['#0a0000', '#6a0000'],
        ['#2a2a2a', '#8B0000'],
    ];
    
    portfolioImages.forEach((img, i) => {
        const gradient = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
        const colors = gradients[i % gradients.length];
        gradient.addColorStop(0, colors[0]);
        gradient.addColorStop(1, colors[1]);
        
        ctx.fillStyle = gradient;
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        // Add border
        ctx.strokeStyle = '#8B0000';
        ctx.lineWidth = 4;
        ctx.strokeRect(0, 0, canvas.width, canvas.height);
        
        // Add text
        ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
        ctx.font = 'bold 48px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(img.caption, canvas.width / 2, canvas.height / 2);
        
        // Save as data URL (for demo purposes - replace with real images)
        // img.src = canvas.toDataURL('image/jpeg', 0.9);
    });
}

// Note: Actual placeholder images should be created separately
// This function is here for reference only
