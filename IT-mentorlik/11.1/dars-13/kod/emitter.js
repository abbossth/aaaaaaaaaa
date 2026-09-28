export class EventEmitter {
  #listeners = new Map();

  on(event, handler) {
    if (!this.#listeners.has(event)) this.#listeners.set(event, new Set());
    this.#listeners.get(event).add(handler);
    return () => this.off(event, handler); // unsubscribe funksiyasi
  }

  off(event, handler) {
    this.#listeners.get(event)?.delete(handler);
  }

  once(event, handler) {
    const wrapper = (...args) => {
      this.off(event, wrapper);
      handler(...args);
    };
    return this.on(event, wrapper);
  }

  emit(event, ...args) {
    for (const handler of this.#listeners.get(event) ?? []) handler(...args);
  }

  listenerCount(event) {
    return this.#listeners.get(event)?.size ?? 0;
  }
}

// ===== Namuna: onlayn do'kon =====
const shop = new EventEmitter();

const sendSms = (order) => console.log(`📱 SMS: buyurtma #${order.id} qabul qilindi`);
const updateStock = (order) => console.log(`📦 Ombor: ${order.items.length} ta mahsulot kamaytirildi`);
const notifyAdmin = (order) => console.log(`👨‍💼 Admin: yangi buyurtma, ${order.total} so'm`);

shop.on("order:created", sendSms);
shop.on("order:created", updateStock);
const unsubscribeAdmin = shop.on("order:created", notifyAdmin);
shop.once("order:created", () => console.log("🎁 Birinchi buyurtma uchun sovg'a!"));

shop.emit("order:created", { id: 1, items: ["telefon", "chexol"], total: 3_100_000 });
console.log("---");
unsubscribeAdmin();
shop.emit("order:created", { id: 2, items: ["quloqchin"], total: 650_000 });
console.log("Obunachilar:", shop.listenerCount("order:created"));
