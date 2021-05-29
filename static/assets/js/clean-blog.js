(function () {
    "use strict"; // Start of use strict

    // Show the navbar when the page is scrolled up
    let MQL = 992;
    let vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0);
    let mainNav = document.querySelector('#mainNav');

    //primary navigation slide-in effect
    if (mainNav && vw > MQL) {
        let headerHeight = mainNav.offsetHeight;
        let previousTop = window.pageYOffset;

        window.addEventListener('scroll', function () {
            let currentTop = window.pageYOffset;
            //check if user is scrolling up
            if (currentTop < previousTop) {
                //if scrolling up...
                if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                    mainNav.classList.add('is-visible');
                } else {
                    mainNav.classList.remove('is-visible', 'is-fixed');
                }
            } else if (currentTop > previousTop) {
                //if scrolling down...
                mainNav.classList.remove('is-visible');

                if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                    mainNav.classList.add('is-fixed');
                }
            }
            previousTop = currentTop;
        });
    }

})(); // End of use strict
