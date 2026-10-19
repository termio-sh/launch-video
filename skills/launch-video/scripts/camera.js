// Camera + pointer core from termio-sh/launch-video/20261019-horizontal-tabs/index.html.
// Paste into a HyperFrames composition after `const tl = gsap.timeline({ paused: true })`.
// Needs: an element `.cam` (the world), `#pointer` (flat, above everything), and
// <svg><filter id="mb"><feGaussianBlur id="mb-k" stdDeviation="0 0"/></filter></svg>.

// Cubic-bezier easing solved for x (bisection, 40 steps). GSAP's CustomEase is not needed.
const bezier = (x1, y1, x2, y2) => {
  const cx = 3 * x1, bx = 3 * (x2 - x1) - cx, ax = 1 - cx - bx;
  const cy = 3 * y1, by = 3 * (y2 - y1) - cy, ay = 1 - cy - by;
  const X = (t) => ((ax * t + bx) * t + cx) * t;
  const Y = (t) => ((ay * t + by) * t + cy) * t;
  return (p) => {
    if (p <= 0) return 0;
    if (p >= 1) return 1;
    let lo = 0, hi = 1, t = p;
    for (let i = 0; i < 40; i += 1) { if (X(t) < p) lo = t; else hi = t; t = (lo + hi) / 2; }
    return Y(t);
  };
};
// Camera: leaves rest gently, spends most of the move decelerating.
const GLIDE = bezier(0.4, 0, 0.1, 1);
// Pointer: a hand's move, quick then a long settle.
const HAND = bezier(0.3, 0, 0.15, 1);
const slope = (ease, p) => {
  const a = Math.max(0, p - 0.002), b = Math.min(1, p + 0.002);
  return (ease(b) - ease(a)) / (b - a);
};

// Focus point (px,py) in world pixels lands on screen spot (sx,sy). Scale is stored as its
// log, so a zoom changes by the same ratio every frame.
const cam = { px: 0, py: 0, ls: Math.log(1), r: 0, sx: 960, sy: 540 };
const state = { ...cam }; // mirror: every tween starts where the previous one ended
const pans = [];
const camTo = (to, at, duration, { pan = false, ease = GLIDE } = {}) => {
  const target = { ...to };
  if ("s" in target) { target.ls = Math.log(target.s); delete target.s; }
  const from = Object.fromEntries(Object.keys(target).map((k) => [k, state[k]]));
  if (pan) pans.push({ at, duration, ease, dx: (target.px - from.px) * Math.exp(state.ls) });
  Object.assign(state, target);
  tl.fromTo(cam, from, { ...target, duration, ease, immediateRender: false }, at);
};

const hand = { x: 0, y: 0, o: 0, k: 1 };
const handState = { ...hand };
const handTo = (to, at, duration, ease = HAND) => {
  const from = Object.fromEntries(Object.keys(to).map((k) => [k, handState[k]]));
  Object.assign(handState, to);
  tl.fromTo(hand, from, { ...to, duration, ease, immediateRender: false }, at);
};
// A click is a press, never a move: the camera and the hand are both still.
const click = (at) => {
  handTo({ k: 0.86 }, at - 0.06, 0.06, "power2.out");
  handTo({ k: 1 }, at + 0.06, 0.16, "power2.out");
};

const panSpeed = (time) => pans.reduce((sum, p) => {
  const u = (time - p.at) / p.duration;
  return u <= 0 || u >= 1 ? sum : sum + Math.abs(p.dx) * slope(p.ease, u) / p.duration;
}, 0);

const render = () => {
  const s = Math.exp(cam.ls);
  const rad = (cam.r * Math.PI) / 180, cos = Math.cos(rad), sin = Math.sin(rad);
  const ox = cam.sx - s * (cos * cam.px - sin * cam.py);
  const oy = cam.sy - s * (sin * cam.px + cos * cam.py);
  gsap.set(".cam", { x: ox, y: oy, rotation: cam.r, scale: s, transformOrigin: "0 0" });
  // Horizontal shutter blur in proportion to pan speed; zero at rest.
  const streak = (0.28 * panSpeed(tl.time())) / 60 / s;
  document.getElementById("mb-k").setAttribute("stdDeviation", `${streak.toFixed(3)} 0`);
  document.querySelector(".cam").style.filter = streak > 0.05 ? "url(#mb)" : "none";
  gsap.set("#pointer", {
    x: ox + s * (cos * hand.x - sin * hand.y), y: oy + s * (sin * hand.x + cos * hand.y),
    rotation: cam.r, scale: s * 0.5 * hand.k, opacity: hand.o, transformOrigin: "0 0",
  });
};
tl.eventCallback("onUpdate", render);
// After all camTo/handTo calls: render(); so frame 0 is placed before the first seek.
