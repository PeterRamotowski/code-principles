(() => {
  const normalize = (value) => value.trim().toLocaleLowerCase();

  const initCatalogFilters = () => {
    document.querySelectorAll("[data-catalog-filter]").forEach((input) => {
      if (input.dataset.catalogFilterReady === "true") return;
      input.dataset.catalogFilterReady = "true";

      const root = input.closest(".md-content") || document;
      const items = Array.from(root.querySelectorAll("[data-catalog-item]"));
      const count = root.querySelector("[data-catalog-count]");
      const empty = root.querySelector("[data-catalog-empty]");

      const apply = () => {
        const query = normalize(input.value);
        let visible = 0;

        items.forEach((item) => {
          const matches = !query || normalize(item.dataset.search || item.textContent || "").includes(query);
          item.hidden = !matches;
          if (matches) visible += 1;
        });

        root.querySelectorAll(".catalog-group").forEach((group) => {
          const groupVisible = Array.from(group.querySelectorAll("[data-catalog-item]")).some((item) => !item.hidden);
          group.hidden = !groupVisible;
        });

        if (count) count.textContent = `${visible} ${visible === 1 ? "entry" : "entries"}`;
        if (empty) empty.hidden = visible !== 0;
      };

      input.addEventListener("input", apply);
      apply();
    });
  };

  if (typeof document$ !== "undefined") {
    document$.subscribe(initCatalogFilters);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initCatalogFilters);
  } else {
    initCatalogFilters();
  }
})();
