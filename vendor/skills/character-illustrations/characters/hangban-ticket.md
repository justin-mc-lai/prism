---
name: hangban-ticket
display_name: 票签 (Hangban Ticket)
palette: semantic-triad
accents:
  orange: "#e8842c"           # boarding path, process arrows
  red: "#c9382e"              # entry refusal, warnings, TDAC fraud
  blue: "#3a6fc4"             # official links, secondary notes
label_language: Chinese
watermark: none
---

# 票签 (Hangban Ticket)

## Character definition

票签 is the fixed visual IP for **航班票务信息发布** (`hangban-gzh` / `airline-info`). A flat black boarding-pass-shaped worker with a small punch-hole “eye”, deadpan and serious. Not a cute airline mascot — a ground-ops clerk who hauls materials, stamps checklists, and blocks unsafe gates.

## Form

- Body: thick rectangle boarding-pass / ticket stub silhouette, filled near-black (`#1a1a1a`).
- One circular punch-hole near the top acts as a single pale eye (empty, calm).
- Thin stick legs; thin stick arms only when carrying stamps, tickets, or warning boards.
- May morph into a ticket stack, gate barrier, stamp pad, or TDAC well bucket — keep the punch-hole eye so identity holds.
- Outline slightly irregular, hand-drawn. No smile, no sparkle.

## Personality

- Checklist-first, zero small talk.
- Serious about “送到人”, not about selling tickets.
- Dry humor: treats policy as gravity, not drama.
- Slightly stiff, never cute, never panic-gesture heavy.

## Action library

- Pushing a three-shelf cart (passport / lodging / funds).
- Inserting a return-ticket key into a landing lock.
- Pulling a real TDAC card from an official well; kicking a fake booth.
- Sticking a “行前须知” note onto a passenger phone.
- Holding a red bar at 审查闸 while a 免签门 stands open.
- Stamping 齐 / 缺 on a materials tray.
- Sorting PNR slips vs notice slips on a dispatch desk.

## Don'ts

- No airline logos, real carrier liveries, or real banknotes.
- No cute stewardess costume, no chibi, no emoji face.
- Never just waving beside a flowchart.
- No fear-mongering gore; warnings stay symbolic (red bar, X, trap door).

## SVG recipe

- Body: rounded rect 3:2, fill `#1a1a1a`, slight wobble stroke.
- Eye: circle punch-hole near top-right of body, fill white/light gray.
- Limbs: 2–3px stick strokes.
- Scale: ~18–24% canvas height as primary actor.

## Image-gen prompt block

票签, a small solid near-black boarding-pass / ticket-stub shaped worker with one circular punch-hole eye, thin stick legs, blank serious deadpan expression, slightly uneven hand-drawn outline. 票签 must perform the core conceptual action (stamping, hauling materials, blocking a gate, sticking a notice), not decorate the scene. Serious ground-ops clerk vibe, never cute, no airline logos.

## The test

If removing 票签 leaves the metaphor intact, rewrite so 票签 operates the gate, stamp, well, or notice.
