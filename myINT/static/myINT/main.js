document.addEventListener('DOMContentLoaded', function () {
  //   // Load more articles
 //  //new Load More Button functionality
  let currentVisible = 4;

  document.getElementById("new-load-more-btn").addEventListener("click", function () {
    const cards = document.querySelectorAll(".blog-card");
    
    // Show next 4 cards
    for (let i = currentVisible; i < Math.min(currentVisible + 4, cards.length); i++) {
      cards[i].classList.remove("hidden");
    }

    currentVisible += 4;

    // Optional: Hide button when all cards are shown
    if (currentVisible >= cards.length) {
      this.style.display = "none";
    }
  });

  const scroller = document.getElementById('logoScroller');
  let scrollAmount = 0;
  const speed = 1; // Pixels per frame, adjust for speed
  const totalWidth = scroller.scrollWidth / 2; // Half the width due to duplication

  function scrollLogos() {
    scrollAmount -= speed;
    if (Math.abs(scrollAmount) >= totalWidth) {
      scrollAmount = 0; // Reset to start for seamless loop
    }
    scroller.style.transform = `translateX(${scrollAmount}px)`;
    requestAnimationFrame(scrollLogos);
  }

  // Start scrolling
  scrollLogos();

  // Pause on hover
  scroller.addEventListener('mouseenter', () => {
    scroller.style.animationPlayState = 'paused';
  });
  scroller.addEventListener('mouseleave', () => {
    scrollLogos();
  });

  // ================
  // SEARCH FUNCTION
  // ================
const searchInput = document.getElementById("search-input");

    if (searchInput) {
      searchInput.addEventListener("input", function () {
        const searchTerm = this.value.toLowerCase();
        const cards = document.querySelectorAll(".blog-card");

        cards.forEach(card => {
          const title = card.querySelector("h3")?.textContent.toLowerCase() || "";
          if (title.includes(searchTerm)) {
            card.classList.remove("hidden");
          } else {
            card.classList.add("hidden");
          }
        });
      });
    };

    // Select all nav-links
    const navLinks = document.querySelectorAll('.nav-link');

    // Function to handle click events
    function handleNavLinkClick(event) {
        navLinks.forEach(link => {
            link.classList.remove('active');
        });
        event.target.classList.add('active');
    }

    // Attach click event listeners to each nav-link
    navLinks.forEach(link => {
        link.addEventListener('click', handleNavLinkClick);
    });

    // Set the active link based on the current URL
    const currentUrl = window.location.href;
    navLinks.forEach(link => {
        if (link.href === currentUrl) {
            link.classList.add('active');
        }
    });

  // ================
  const slider = document.getElementById('slider');
  const dots = document.querySelectorAll('.dot');

  // Update dots when user scrolls
  slider.addEventListener('scroll', () => {
    const cardWidth = 96 * 4; // Tailwind w-96 is 24rem = ~384px
    const index = Math.round(slider.scrollLeft / cardWidth);
    
    dots.forEach((dot, i) => {
      dot.classList.toggle('bg-sky-700', i === index);
      dot.classList.toggle('bg-sky-300', i !== index);
    });
  });

  // Optional: Click on dot to scroll
  dots.forEach(dot => {
    dot.addEventListener('click', () => {
      const index = parseInt(dot.getAttribute('data-index'));
      const cardWidth = 96 * 4;

      slider.scrollTo({
        left: index * cardWidth,
        behavior: 'smooth'
      });

      dots.forEach(d => {
        d.classList.remove('bg-sky-700');
        d.classList.add('bg-sky-300');
      });
      dot.classList.add('bg-sky-700');
    });
  });

 
  

    //Dropdown functionality
  const dropdownButton = document.getElementById('dropdownButton');
  const dropdownMenu = document.getElementById('dropdownMenu');
  const selectedOption = document.getElementById('selectedOption');

  dropdownButton.addEventListener('click', () => {
    dropdownMenu.classList.toggle('hidden');
  });

  document.querySelectorAll('.dropdown-item').forEach(item => {
    item.addEventListener('click', () => {
      selectedOption.textContent = item.textContent;
      categoryInput.value = selectedOption.textContent;
      dropdownMenu.classList.add('hidden');
    });
  });

  document.addEventListener('click', (e) => {
    if (!dropdownButton.contains(e.target) && !dropdownMenu.contains(e.target)) {
      dropdownMenu.classList.add('hidden');
    }
  });

  //navbar functionality
  document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', () => {
    document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active-case-studies'));
    link.classList.add('active-case-studies');
  });
});

//success message auto-hide
const successMessage = document.querySelector('.text-green-600');
    if (successMessage) {
        setTimeout(() => {
            successMessage.style.display = 'none';
        }, 10000); // Hide after 10 seconds
    }


    
})