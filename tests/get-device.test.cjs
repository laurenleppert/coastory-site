const { test } = require('node:test');
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const vm = require('node:vm');
const source = readFileSync(new URL('../get/device.js', `file://${__filename}`), 'utf8');

function render(navigator) {
  const root = {};
  const descriptions = {};
  const document = {
    documentElement: { setAttribute: (key, value) => { root[key] = value; } },
    getElementById: (id) => ({ setAttribute: (key, value) => { descriptions[id] = { [key]: value }; } }),
  };
  // No network, location, timers or storage: enhancement must only annotate the page.
  vm.runInNewContext(source, { navigator, document });
  return { root, descriptions };
}

for (const [name, navigator, platform] of [
  ['iPhone', { userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X)' }, 'ios'],
  ['iPad', { userAgent: 'Mozilla/5.0 (iPad; CPU OS 18_0 like Mac OS X)' }, 'ios'],
  ['iPad desktop mode', { userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15)', platform: 'MacIntel', maxTouchPoints: 5 }, 'ios'],
  ['Android phone', { userAgent: 'Mozilla/5.0 (Linux; Android 15; Pixel 9)' }, 'android'],
  ['reduced Android UA with platform hint', { userAgent: '', userAgentData: { platform: 'Android' } }, 'android'],
]) {
  test(`${name} suggests only its matching store`, () => {
    const { root, descriptions } = render(navigator);
    assert.equal(root['data-platform'], platform);
    assert.deepEqual(Object.keys(descriptions), [platform === 'ios' ? 'app-store' : 'google-play']);
    assert.equal(Object.values(descriptions)[0]['aria-description'], 'Suggested for your device');
  });
}

for (const [name, navigator] of [
  ['Mac desktop', { userAgent: 'Mozilla/5.0 (Macintosh)', platform: 'MacIntel', maxTouchPoints: 0 }],
  ['Windows touchscreen', { userAgent: 'Mozilla/5.0 (Windows NT 10.0)', platform: 'Win32', maxTouchPoints: 10 }],
  ['unknown device', { userAgent: 'Unrecognized' }],
  ['missing optional navigator fields', {}],
]) {
  test(`${name} keeps the stores equal`, () => {
    assert.deepEqual(render(navigator), { root: {}, descriptions: {} });
  });
}
