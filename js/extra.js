document.addEventListener('DOMContentLoaded', function() {
  // Smooth scrolling for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });

  // Add subtle hover effect to code blocks
  const codeBlocks = document.querySelectorAll('pre code');
  codeBlocks.forEach(block => {
    block.addEventListener('mouseenter', function() {
      this.closest('pre').style.boxShadow = '0 2px 6px rgba(0, 0, 0, 0.1)';
    });
    block.addEventListener('mouseleave', function() {
      this.closest('pre').style.boxShadow = '';
    });
  });
});
