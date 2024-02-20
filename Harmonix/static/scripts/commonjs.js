document.addEventListener("DOMContentLoaded", function () {
  const button = document.querySelector(".scroll-back");

  window.onscroll = function () {
      if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
          button.style.display = "block";
      } else {
          button.style.display = "none";
      }
  };

  button.addEventListener("click", function () {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
  });
});