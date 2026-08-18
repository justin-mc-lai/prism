/* wechat-card-kit · 动效初始化
   依赖：vendor/anime.min.js + vendor/rough-notation.iife.js
   所有动画完成后置位 window.__kitMotionDone = true，供渲染器等待结束态截图。
   prefers-reduced-motion 时跳过 JS 动画，立即置位。 */
(function () {
  "use strict";

  var reduce =
    window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var finished = false;

  function finish() {
    if (finished) return;
    finished = true;
    window.__kitMotionDone = true;
  }

  function ready(fn) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      fn();
    }
  }

  ready(function () {
    /* RoughNotation：立即 show()，手绘标注必须是静态最终态 */
    if (window.RoughNotation) {
      document.querySelectorAll("[data-rough]").forEach(function (el) {
        var type = el.getAttribute("data-rough") || "highlight";
        var color = el.getAttribute("data-rough-color") || "#ea7a00";
        var stroke = parseFloat(el.getAttribute("data-rough-stroke") || "4");
        var pad = parseFloat(el.getAttribute("data-rough-pad") || "8");
        var annotation = RoughNotation.annotate(el, {
          type: type,
          color: color,
          strokeWidth: stroke,
          padding: pad,
          animate: !reduce,
        });
        annotation.show();
      });
    }

    if (reduce || !window.anime) {
      setTimeout(finish, 120);
      return;
    }

    var pending = 0;

    function track(opts) {
      pending += 1;
      opts.complete = (function (original) {
        return function () {
          if (typeof original === "function") original();
          pending -= 1;
          if (pending <= 0) setTimeout(finish, 380);
        };
      })(opts.complete);
      return anime(opts);
    }

    /* 入场 */
    document.querySelectorAll('[data-motion="reveal"]').forEach(function (el) {
      track({
        targets: el,
        opacity: [0, 1],
        translateY: [26, 0],
        duration: 680,
        easing: "easeOutCubic",
      });
    });

    /* 错落入场：作用于父级子元素 */
    document.querySelectorAll('[data-motion="stagger"]').forEach(function (parent) {
      var children = Array.prototype.slice.call(parent.children);
      if (!children.length) return;
      track({
        targets: children,
        opacity: [0, 1],
        translateY: [18, 0],
        duration: 460,
        delay: anime.stagger(90),
        easing: "easeOutQuad",
      });
    });

    /* 扫光：CSS 动画，结束态即静态渐变 */
    document.querySelectorAll('[data-motion="sweep"]').forEach(function (el) {
      el.classList.add("kit-anim-sweep");
    });

    /* 打字：逐字出现（预览用；截图请用结束态） */
    document.querySelectorAll('[data-motion="typing"]').forEach(function (el) {
      var text = el.textContent;
      el.textContent = "";
      var spans = [];
      text.split("").forEach(function (ch) {
        var span = document.createElement("span");
        span.innerHTML = ch === " " ? "&nbsp;" : ch;
        span.style.opacity = "0";
        el.appendChild(span);
        spans.push(span);
      });
      track({
        targets: spans,
        opacity: 1,
        duration: 30,
        delay: anime.stagger(34),
        easing: "linear",
      });
    });

    /* 数字滚动：结束态显示最终数字 */
    document.querySelectorAll('[data-motion="countup"]').forEach(function (el) {
      var raw = el.getAttribute("data-count") || el.textContent || "0";
      var target = parseFloat(raw) || 0;
      var decimals = raw.indexOf(".") >= 0 ? 1 : 0;
      var state = { v: 0 };
      track({
        targets: state,
        v: target,
        duration: 900,
        easing: "easeOutCubic",
        update: function () {
          el.textContent = state.v.toFixed(decimals);
        },
      });
    });

    /* 呼吸：循环微动（非关键元素） */
    document.querySelectorAll('[data-motion="pulse"]').forEach(function (el) {
      el.classList.add("kit-anim-pulse");
    });

    if (pending === 0) setTimeout(finish, 480);
  });
})();
