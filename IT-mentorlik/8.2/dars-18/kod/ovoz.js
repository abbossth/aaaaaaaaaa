// Web Audio API bilan oddiy nota chalish
const ctx = new AudioContext();

export function chal(chastota, davomiylik = 0.3) {
  const osc = ctx.createOscillator();
  const gain = ctx.createGain();
  osc.type = "sine";
  osc.frequency.value = chastota;
  gain.gain.setValueAtTime(0.3, ctx.currentTime);
  gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + davomiylik);
  osc.connect(gain).connect(ctx.destination);
  osc.start();
  osc.stop(ctx.currentTime + davomiylik);
}

export const NOTALAR = { a: 262, s: 294, d: 330, f: 349, g: 392, h: 440, j: 494 };
