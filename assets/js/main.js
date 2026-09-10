document.addEventListener("DOMContentLoaded", function () {
  var hamb = document.querySelector(".hamb");
  var menu = document.querySelector(".menu");
  if (hamb && menu) {
    hamb.addEventListener("click", function () {
      menu.classList.toggle("aberto");
    });
    menu.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        menu.classList.remove("aberto");
      });
    });
  }

  var ano = document.querySelector("[data-ano]");
  if (ano) ano.textContent = new Date().getFullYear();
});
