'use strict';
const BootBot = require('bootbot');

const bot = new BootBot({
  accessToken: process.env.FB_PAGE_ACCESS_TOKEN
  verifyToken: process.env.FB_VERIFY_TOKEN,
  appSecret: process.env.FB_APP_SECRET
});

bot.on('message', (payload, chat) => {
	const text = payload.message.text;
	console.log(`The user said: ${text}`);
});

bot.hear(['hello', 'hi', /hey( there)?/i], (payload, chat) => {
	console.log('The user said "hello", "hi", "hey", or "hey there"');
  chat.say(`Echo: ${text}`);

});