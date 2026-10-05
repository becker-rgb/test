// Malerbetrieb – Basis-Skripte
(function () {
  "use strict";

  // Mobile Navigation
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      document.body.classList.toggle("nav-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Referenz-Filter
  var filterButtons = document.querySelectorAll(".filter button");
  var items = document.querySelectorAll(".gallery__item");
  filterButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var cat = btn.getAttribute("data-filter");
      filterButtons.forEach(function (b) { b.classList.toggle("is-active", b === btn); });
      items.forEach(function (item) {
        item.hidden = cat !== "alle" && item.getAttribute("data-category") !== cat;
      });
    });
  });

  // Kontaktformular – Platzhalter, bis ein Formular-Backend angebunden ist
  var form = document.querySelector(".form[data-demo]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var status = form.querySelector(".form__status");
      if (status) status.textContent = "Vielen Dank! Wir melden uns schnellstmöglich bei Ihnen.";
      form.reset();
    });
  }

  // Aktuelles Jahr im Footer
  var year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();
})();
