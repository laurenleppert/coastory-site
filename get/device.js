/* A convenience hint, never an access check. No redirects, storage or tracking. */
(() => {
  const agent = navigator.userAgent || '';
  const platformHint = navigator.userAgentData?.platform || '';
  let platform;
  if (/Android/i.test(agent) || /Android/i.test(platformHint)) {
    platform = 'android';
  } else if (/iPad|iPhone|iPod/i.test(agent)
    || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1)) {
    // iPadOS may request desktop pages with a Mac user agent.
    platform = 'ios';
  }
  if (!platform) return;
  document.documentElement.setAttribute('data-platform', platform);
  const link = document.getElementById(platform === 'ios' ? 'app-store' : 'google-play');
  link?.setAttribute('aria-description', 'Suggested for your device');
})();
