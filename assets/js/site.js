/* Distribuidora Peres & Araújo — comportamento do site */
(function () {
  var doc = document.documentElement;

  /* Data de hoje no horário de Brasília (UTC-3, sem horário de verão) */
  function hojeBRT() {
    var agora = new Date();
    return new Date(agora.getTime() + agora.getTimezoneOffset() * 60000 - 3 * 3600000);
  }
  var hoje = hojeBRT();

  /* 12 anos: de 08/01/2027 00:00 a 31/01/2027 23:59 (Brasília) */
  var ini = new Date(2027, 0, 8), fim = new Date(2027, 1, 1);
  if (hoje >= ini && hoje < fim) doc.classList.add("festa12");
  else doc.classList.remove("festa12");

  /* Anos de empresa: fundação em 08/01/2015 */
  var anos = hoje.getFullYear() - 2015;
  if (hoje.getMonth() === 0 && hoje.getDate() < 8) anos--;
  document.querySelectorAll("[data-anos]").forEach(function (el) { el.textContent = anos; });
  document.querySelectorAll("[data-ano]").forEach(function (el) { el.textContent = hoje.getFullYear(); });

  document.addEventListener("DOMContentLoaded", function () {
    /* Menu mobile */
    var hamb = document.querySelector(".hamb");
    if (hamb) {
      hamb.addEventListener("click", function () {
        var aberto = doc.classList.toggle("menu-aberto");
        hamb.setAttribute("aria-expanded", aberto ? "true" : "false");
      });
      document.querySelectorAll(".menu > a").forEach(function (a) {
        a.addEventListener("click", function () {
          doc.classList.remove("menu-aberto");
          hamb.setAttribute("aria-expanded", "false");
        });
      });
    }

    /* Seletores de WhatsApp: um aberto por vez, fecham com clique fora ou Esc */
    var seletores = document.querySelectorAll(".wa-escolha");
    seletores.forEach(function (d) {
      d.addEventListener("toggle", function () {
        if (!d.open) return;
        seletores.forEach(function (o) { if (o !== d) o.removeAttribute("open"); });
      });
    });
    document.addEventListener("click", function (e) {
      seletores.forEach(function (d) { if (!d.contains(e.target)) d.removeAttribute("open"); });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key !== "Escape") return;
      seletores.forEach(function (d) {
        if (d.open) { d.removeAttribute("open"); var s = d.querySelector("summary"); if (s) s.focus(); }
      });
      if (doc.classList.contains("menu-aberto") && hamb) { doc.classList.remove("menu-aberto"); hamb.setAttribute("aria-expanded", "false"); hamb.focus(); }
    });

    /* Entrada suave ao rolar */
    var itens = document.querySelectorAll(".revelar");
    if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      var io = new IntersectionObserver(function (entradas) {
        entradas.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add("visivel"); io.unobserve(en.target); }
        });
      }, { rootMargin: "0px 0px -8% 0px" });
      itens.forEach(function (el) { io.observe(el); });
    } else {
      itens.forEach(function (el) { el.classList.add("visivel"); });
    }

    /* Novidades: posts com data futura ficam ocultos até o dia */
    var iso = hoje.getFullYear() + "-" + ("0" + (hoje.getMonth() + 1)).slice(-2) + "-" + ("0" + hoje.getDate()).slice(-2);
    document.querySelectorAll("[data-publicar]").forEach(function (el) {
      if (el.getAttribute("data-publicar") > iso) el.hidden = true; else el.hidden = false;
    });

    /* Novidades: filtro por categoria */
    var filtros = document.querySelectorAll(".filtros button");
    filtros.forEach(function (b) {
      b.addEventListener("click", function () {
        var cat = b.getAttribute("data-cat");
        filtros.forEach(function (o) { o.setAttribute("aria-pressed", o === b ? "true" : "false"); });
        document.querySelectorAll(".news-grid .news-card").forEach(function (c) {
          var ok = cat === "todas" || c.getAttribute("data-cat") === cat;
          var futuro = c.getAttribute("data-publicar") > iso;
          c.hidden = !ok || futuro;
        });
      });
    });

    /* Contato: monta a mensagem e abre no WhatsApp do sócio escolhido ou no e-mail */
    var form = document.getElementById("form-contato");
    if (form) {
      var via = "whatsapp";
      form.querySelectorAll("button[data-via]").forEach(function (b) {
        b.addEventListener("click", function () { via = b.getAttribute("data-via"); });
      });
      form.addEventListener("submit", function (ev) {
        ev.preventDefault();
        var erro = document.getElementById("form-erro");
        var v = function (id) { return (form.querySelector("#" + id).value || "").trim(); };
        var falta = [];
        if (!v("nome")) falta.push("seu nome");
        if (!v("mensagem")) falta.push("a mensagem");
        if (falta.length) {
          erro.textContent = "Preencha " + falta.join(" e ") + " para enviar.";
          erro.hidden = false;
          form.querySelector(!v("nome") ? "#nome" : "#mensagem").focus();
          return;
        }
        erro.hidden = true;
        var linhas = ["Olá, tudo bem? Acessei o site da Distribuidora Peres & Araújo.", "",
          "Nome: " + v("nome")];
        if (v("orgao")) linhas.push("Órgão/Empresa: " + v("orgao"));
        if (v("email")) linhas.push("E-mail: " + v("email"));
        if (v("telefone")) linhas.push("Telefone: " + v("telefone"));
        linhas.push("Assunto: " + v("assunto"), "", v("mensagem"));
        var texto = linhas.join("\n");
        if (via === "email") {
          location.href = "mailto:distribuidora.peres@hotmail.com?subject=" +
            encodeURIComponent("Contato pelo site: " + v("assunto")) + "&body=" + encodeURIComponent(texto);
        } else {
          var socio = form.querySelector("input[name=socio]:checked").value;
          var url = "https://wa.me/" + socio + "?text=" + encodeURIComponent(texto);
          var w = window.open(url, "_blank");
          if (w) w.opener = null; else location.href = url;
        }
      });
    }
  });
})();
