importScripts('https://www.gstatic.com/firebasejs/7.14.6/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/7.14.6/firebase-messaging.js');

const firebaseConfig = {
      
    apiKey: "AIzaSyCkBqdpVdhS9khOqkas4Klx8StnNz1jKIw",

    authDomain: "fcmtest-4b3c4.firebaseapp.com",

    projectId: "fcmtest-4b3c4",

    storageBucket: "fcmtest-4b3c4.appspot.com",

    messagingSenderId: "1058017262200",

    appId: "1:1058017262200:web:101ccd16af114b1a77cb8d"

  };

firebase.initializeApp(firebaseConfig);
const messaging=firebase.messaging();

messaging.setBackgroundMessageHandler(function (payload) {
    console.log(payload);
    const notification=JSON.parse(payload);
    const notificationOption={
        body:notification.body,
        icon:notification.icon
    };
    return self.registration.showNotification(payload.notification.title,notificationOption);
});