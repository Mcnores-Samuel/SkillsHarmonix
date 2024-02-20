// Load this script after the page has loaded
const categories = document.querySelector('.Categories-icon');
const categoriesMenu = document.querySelector('.Categories-menu');


document.addEventListener("DOMContentLoaded", function () {
  const sections = document.querySelectorAll("li");

  sections.forEach((section) => {
      section.addEventListener("click", function () {
          // Remove "active" class from all sections
          sections.forEach((s) => s.classList.remove("active"));
          // Add "active" class to the clicked section
          section.classList.add("active");
      });
  });
});


