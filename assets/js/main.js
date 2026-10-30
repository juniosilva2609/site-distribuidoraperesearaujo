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

  var seletores = document.querySelectorAll(".wa-escolha");
  seletores.forEach(function (d) {
    d.addEventListener("toggle", function () {
      if (!d.open) return;
      seletores.forEach(function (o) { if (o !== d) o.removeAttribute("open"); });
    });
    d.querySelectorAll(".wa-lista a").forEach(function (a) {
      a.addEventListener("click", function () { d.removeAttribute("open"); });
    });
  });
  document.addEventListener("click", function (e) {
    seletores.forEach(function (d) { if (!d.contains(e.target)) d.removeAttribute("open"); });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") seletores.forEach(function (d) { d.removeAttribute("open"); });
  });
});
