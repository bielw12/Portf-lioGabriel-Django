// Mobile Navigation Toggle
document.addEventListener("DOMContentLoaded", () => {
  const navToggle = document.getElementById("nav-toggle")
  const navMenu = document.getElementById("nav-menu")

  if (navToggle && navMenu) {
    navToggle.addEventListener("click", () => {
      navMenu.classList.toggle("active")
      navToggle.classList.toggle("active")
    })

    // Close menu when clicking on a link
    const navLinks = document.querySelectorAll(".nav-link")
    navLinks.forEach((link) => {
      link.addEventListener("click", () => {
        navMenu.classList.remove("active")
        navToggle.classList.remove("active")
      })
    })
  }
})

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault()
    const target = document.querySelector(this.getAttribute("href"))
    if (target) {
      target.scrollIntoView({
        behavior: "smooth",
        block: "start",
      })
    }
  })
})

// Add scroll effect to navbar
window.addEventListener("scroll", () => {
  const navbar = document.querySelector(".navbar")
  if (window.scrollY > 50) {
    navbar.style.backgroundColor = "rgba(255, 255, 255, 0.95)"
    navbar.style.backdropFilter = "blur(10px)"
  } else {
    navbar.style.backgroundColor = "var(--background-primary)"
    navbar.style.backdropFilter = "none"
  }
})

// Form validation and enhancement
const contactForm = document.querySelector(".contact-form form")
if (contactForm) {
  contactForm.addEventListener("submit", (e) => {
    const requiredFields = contactForm.querySelectorAll("[required]")
    let isValid = true

    requiredFields.forEach((field) => {
      if (!field.value.trim()) {
        isValid = false
        field.style.borderColor = "#dc2626"
      } else {
        field.style.borderColor = "var(--border-color)"
      }
    })

    if (!isValid) {
      e.preventDefault()
      alert("Por favor, preencha todos os campos obrigatórios.")
    }
  })
}

// Animate elements on scroll
const observerOptions = {
  threshold: 0.1,
  rootMargin: "0px 0px -50px 0px",
}

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("fade-in-up")
    }
  })
}, observerOptions)

// Observe cards and sections
document.querySelectorAll(".card, .project-card, .skill-category").forEach((el) => {
  observer.observe(el)
})

// Copy to clipboard functionality
function copyToClipboard(text) {
  navigator.clipboard.writeText(text).then(() => {
    // Show success message
    const message = document.createElement("div")
    message.textContent = "Copiado para a área de transferência!"
    message.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--primary-color);
            color: white;
            padding: 10px 20px;
            border-radius: var(--border-radius);
            z-index: 9999;
            animation: fadeInUp 0.3s ease;
        `
    document.body.appendChild(message)

    setTimeout(() => {
      message.remove()
    }, 3000)
  })
}

// Add loading states to buttons
document.querySelectorAll(".btn").forEach((button) => {
  if (button.type === "submit") {
    button.addEventListener("click", function () {
      const originalText = this.textContent
      this.textContent = "Enviando..."
      this.disabled = true

      // Re-enable after form submission
      setTimeout(() => {
        this.textContent = originalText
        this.disabled = false
      }, 3000)
    })
  }
})

// Lazy loading for images
if ("IntersectionObserver" in window) {
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const img = entry.target
        img.src = img.dataset.src
        img.classList.remove("lazy")
        imageObserver.unobserve(img)
      }
    })
  })

  document.querySelectorAll("img[data-src]").forEach((img) => {
    imageObserver.observe(img)
  })
}

// Dark mode toggle (optional feature)
function toggleDarkMode() {
  document.body.classList.toggle("dark-mode")
  localStorage.setItem("darkMode", document.body.classList.contains("dark-mode"))
}

// Load dark mode preference
if (localStorage.getItem("darkMode") === "true") {
  document.body.classList.add("dark-mode")
}

// Performance optimization: Debounce scroll events
function debounce(func, wait) {
  let timeout
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout)
      func(...args)
    }
    clearTimeout(timeout)
    timeout = setTimeout(later, wait)
  }
}

// Apply debounce to scroll events
const debouncedScrollHandler = debounce(() => {
  // Scroll-based animations or effects can go here
}, 10)

window.addEventListener("scroll", debouncedScrollHandler)
