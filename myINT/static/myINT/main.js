document.addEventListener('DOMContentLoaded', function () {
    // Load more articles
  document.getElementById('load-more-btn').addEventListener('click', function () {
    const hiddenArticles = document.getElementById('hidden-articles');
    const btn = this;
    hiddenArticles.style.display = 'contents'; // or 'grid' / 'flex'
    btn.style.display = 'none';
  });

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
})