// Umumiy "interfeys": har bir bildirishnomada send(message) bor
class SmsNotification {
  constructor(phone) { this.phone = phone; }
  send(message) { console.log(`📱 SMS -> ${this.phone}: ${message}`); }
}

class EmailNotification {
  constructor(email) { this.email = email; }
  send(message) { console.log(`📧 Email -> ${this.email}: ${message}`); }
}

class TelegramNotification {
  constructor(chatId) { this.chatId = chatId; }
  send(message) { console.log(`✈️ Telegram -> ${this.chatId}: ${message}`); }
}

const creators = {
  sms: SmsNotification,
  email: EmailNotification,
  telegram: TelegramNotification,
};

export function createNotification(type, to) {
  const Creator = creators[type];
  if (!Creator) throw new Error(`Noma'lum bildirishnoma turi: ${type}`);
  return new Creator(to);
}

// Mijoz kodi — aniq klasslarni bilmaydi
const users = [
  { name: "Aziz", channel: "telegram", contact: "@aziz_dev" },
  { name: "Malika", channel: "email", contact: "malika@mail.uz" },
  { name: "Bobur", channel: "sms", contact: "+998901234567" },
];

for (const user of users) {
  createNotification(user.channel, user.contact).send(`Salom, ${user.name}! Buyurtmangiz tayyor.`);
}
