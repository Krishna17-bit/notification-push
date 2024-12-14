const CACHE_NAME = 'notification-chatbot-cache-v1';
const urlsToCache = [
  '/', // Cache the root URL
  '/static/image.png', // Cache the single icon
  '/static/manifest.json', // Cache the manifest file
  '/static/ecommerce.png' // Cache the background image (if applicable)
];

// Install event: Cache the files
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('Opened cache');
      return cache.addAll(urlsToCache);
    })
  );
});

// Fetch event: Serve cached files if available
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      // Return the cached response if found, otherwise fetch from the network
      return response || fetch(event.request);
    })
  );
});

// Activate event: Clear old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((cacheName) => cacheName !== CACHE_NAME)
          .map((cacheName) => caches.delete(cacheName))
      );
    })
  );
});
