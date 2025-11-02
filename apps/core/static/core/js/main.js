document.addEventListener("DOMContentLoaded", () => {
  const video = document.getElementById("heroVideo");
  if (video) {
    video.play().catch(() => {
      // fallback if autoplay fails
      document.querySelector(".hero-slideshow").style.display = "block";
    });
  }
});
