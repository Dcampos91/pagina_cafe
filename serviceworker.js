var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/core/CSS/Style.css',
    '/static/core/IMG/logo.png',
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
      fetch(event.request)
      .then(function(result){
        return caches.open(CACHE_NAME)
        .then(function(c){
          c.put(event.request.url, result.clone());
          return result;
        })
      })
      .catch(function(e){
        return caches.match(event.request)
      })
    );
});

importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');
var firebaseConfig = {
  apiKey: "AIzaSyAgRL3rzIhIUYD9M0D_MpLFTkZ6BZLtzp0",
  authDomain: "cafeduoc2020.firebaseapp.com",
  databaseURL: "https://cafeduoc2020.firebaseio.com",
  projectId: "cafeduoc2020",
  storageBucket: "cafeduoc2020.appspot.com",
  messagingSenderId: "327542197525",
  appId: "1:327542197525:web:253fa84115d26398732d1c"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
let messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function(payload){
  console.log("Ha llegado notificacion")
  let title = payload.notification.title;

  let options = {
    body: payload.notification.body,
    icon: payload.notification.icon
  }

  self.registration.showNotification(title, options);
});
