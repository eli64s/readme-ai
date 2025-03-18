document.addEventListener('DOMContentLoaded', function () {
    // Debug information and logo state tracking
    let lastTheme = '';
    const debugMode = false; // Set to true to enable console logging for debugging

    function debugLog(message) {
        if (debugMode) {
            console.log(`[ReadmeAI Debug] ${message}`);
        }
    }

    // Initial debug information
    debugLog(`Initial color scheme: ${document.body.getAttribute('data-md-color-scheme')}`);
    debugLog(`Light logo exists: ${Boolean(document.querySelector('.light-mode-logo'))}`);
    debugLog(`Dark logo exists: ${Boolean(document.querySelector('.dark-mode-logo'))}`);

    // Main function to detect theme and update logo visibility
    function updateLogoVisibility() {
        // Get current theme
        const scheme = document.body.getAttribute('data-md-color-scheme') || 'default';
        const isDarkTheme = scheme === 'slate' || scheme === 'dark';

        // If theme hasn't changed, don't do unnecessary DOM operations
        if (lastTheme === scheme) {
            debugLog(`Theme unchanged: ${scheme}`);
            return;
        }

        lastTheme = scheme;
        debugLog(`Theme changed to: ${scheme} (isDarkTheme: ${isDarkTheme})`);

        // Get all logos
        const lightLogos = document.querySelectorAll('.light-mode-logo');
        const darkLogos = document.querySelectorAll('.dark-mode-logo');

        debugLog(`Found ${lightLogos.length} light logos and ${darkLogos.length} dark logos`);

        // Update light logo visibility
        lightLogos.forEach(logo => {
            if (isDarkTheme) {
                logo.style.display = 'none';
                logo.style.visibility = 'hidden';
                logo.style.opacity = '0';
            } else {
                logo.style.display = 'block';
                logo.style.visibility = 'visible';
                logo.style.opacity = '1';
            }
        });

        // Update dark logo visibility
        darkLogos.forEach(logo => {
            if (isDarkTheme) {
                logo.style.display = 'block';
                logo.style.visibility = 'visible';
                logo.style.opacity = '1';
            } else {
                logo.style.display = 'none';
                logo.style.visibility = 'hidden';
                logo.style.opacity = '0';
            }
        });

        debugLog("Logo visibility updated via JavaScript");
    }

    // Run initial logo visibility update
    updateLogoVisibility();

    // Watch for theme changes via MutationObserver
    const observer = new MutationObserver(function (mutations) {
        mutations.forEach(function (mutation) {
            if (mutation.attributeName === 'data-md-color-scheme') {
                debugLog(`Mutation observer detected theme change: ${document.body.getAttribute('data-md-color-scheme')}`);
                updateLogoVisibility();
            }
        });
    });

    // Start observing the document body for theme changes
    observer.observe(document.body, {
        attributes: true,
        attributeFilter: ['data-md-color-scheme']
    });

    // Watch for clicks on theme toggle buttons
    const themeToggleButtons = document.querySelectorAll('.md-header__button[data-md-toggle="palette"]');
    themeToggleButtons.forEach(button => {
        debugLog(`Found theme toggle button: ${button}`);
        button.addEventListener('click', function () {
            debugLog("Theme toggle button clicked");
            // Small delay to allow the theme to change before updating logos
            setTimeout(updateLogoVisibility, 50);
        });
    });

    // Add a class to indicate JS is available (enables certain CSS features)
    document.documentElement.classList.add('js-enabled');

    // Handle theme preference changes from OS
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
        debugLog("OS theme preference changed");
        setTimeout(updateLogoVisibility, 50);
    });

    // Create a periodic check as a fallback for any edge cases
    const logoCheckInterval = setInterval(() => {
        updateLogoVisibility();
    }, 2000); // Check every 2 seconds

    // Clear the interval after 30 seconds (theme should be stable by then)
    setTimeout(() => {
        clearInterval(logoCheckInterval);
        debugLog("Cleared periodic logo check interval");
    }, 30000);

    // Smooth scrolling for anchor links with error handling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');

            // Only handle actual anchor links
            if (targetId === '#' || targetId.length <= 1) return;

            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                e.preventDefault();
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
    scrollButton.setAttribute('aria-label', 'Scroll to top');
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

    // Fix for iOS Safari theme issues
    if (navigator.userAgent.match(/(iPad|iPhone|iPod)/g)) {
        document.documentElement.classList.add('ios-device');
        debugLog("iOS device detected, applying special fixes");
    }

    // Force reload of logos on window resize
    // (helps with some edge cases where logos don't update properly)
    let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            updateLogoVisibility();
            debugLog("Window resized, updated logo visibility");
        }, 250);
    });

    // Force update logos when page becomes visible again
    document.addEventListener('visibilitychange', () => {
        if (document.visibilityState === 'visible') {
            updateLogoVisibility();
            debugLog("Page became visible, updated logo visibility");
        }
    });

    debugLog("ReadmeAI theme script initialization complete");
});
