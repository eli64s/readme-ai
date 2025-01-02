document.addEventListener('DOMContentLoaded', function() {
  // Smooth scrolling for anchor links with error handling
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
          e.preventDefault();
          const targetId = this.getAttribute('href');
          const targetElement = document.querySelector(targetId);

          if (targetElement) {
              targetElement.scrollIntoView({
                  behavior: 'smooth',
                  block: 'start'
              });

              // Update URL without jumping
              history.pushState(null, null, targetId);
          }
      });
  });

  // Enhanced code block interactions
//   const codeBlocks = document.querySelectorAll('pre code');
//   codeBlocks.forEach(block => {
//       // Add copy button
//       const pre = block.closest('pre');
//       const copyButton = document.createElement('button');
//       copyButton.className = 'code-copy-button';
//       copyButton.innerHTML = 'Copy';

//       copyButton.addEventListener('click', async () => {
//           try {
//               await navigator.clipboard.writeText(block.textContent);
//               copyButton.innerHTML = 'Copied!';
//               setTimeout(() => {
//                   copyButton.innerHTML = 'Copy';
//               }, 2000);
//           } catch (err) {
//               console.error('Failed to copy:', err);
//               copyButton.innerHTML = 'Error!';
//           }
//       });

//       pre.appendChild(copyButton);

//       // Enhanced hover effects
//       const applyHoverEffect = () => {
//           pre.style.boxShadow = '0 2px 6px var(--custom-shadow-color, rgba(0, 0, 0, 0.1))';
//           pre.style.transform = 'translateY(-1px)';
//       };

//       const removeHoverEffect = () => {
//           pre.style.boxShadow = '';
//           pre.style.transform = '';
//       };

//       block.addEventListener('mouseenter', applyHoverEffect);
//       block.addEventListener('mouseleave', removeHoverEffect);
//   });

  // Add scroll to top button
  const scrollButton = document.createElement('button');
  scrollButton.className = 'scroll-to-top';
  scrollButton.innerHTML = '↑';
  document.body.appendChild(scrollButton);

  const toggleScrollButton = () => {
      if (window.scrollY > 500) {
          scrollButton.classList.add('visible');
      } else {
          scrollButton.classList.remove('visible');
      }
  };

  window.addEventListener('scroll', toggleScrollButton);
  scrollButton.addEventListener('click', () => {
      window.scrollTo({
          top: 0,
          behavior: 'smooth'
      });
  });

  // Add dark mode toggle animation
  const darkModeToggle = document.querySelector('[data-md-color-scheme]');
  if (darkModeToggle) {
      darkModeToggle.addEventListener('click', () => {
          document.body.classList.add('theme-transition');
          setTimeout(() => {
              document.body.classList.remove('theme-transition');
          }, 300);
      });
  }
});
