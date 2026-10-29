(() => {
  const backToTop = document.getElementById("backToTop");
  if (backToTop) {
    const updateButton = () => backToTop.classList.toggle("visible", window.scrollY > 420);
    window.addEventListener("scroll", updateButton, { passive: true });
    updateButton();
    backToTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
  }

  // Add a subtle shadow to the sticky navigation after scrolling.
  const nav = document.querySelector(".main-nav");
  if (nav) {
    const updateNav = () => nav.classList.toggle("nav-scrolled", window.scrollY > 10);
    window.addEventListener("scroll", updateNav, { passive: true });
    updateNav();
  }
})();
