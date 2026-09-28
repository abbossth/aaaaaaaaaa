class Logger {
  static #instance = null;
  #logs = [];

  static getInstance() {
    if (!Logger.#instance) Logger.#instance = new Logger();
    return Logger.#instance;
  }

  log(level, message) {
    const entry = `[${new Date().toISOString()}] ${level.toUpperCase()}: ${message}`;
    this.#logs.push(entry);
    console.log(entry);
  }

  info(msg) { this.log("info", msg); }
  error(msg) { this.log("error", msg); }
  get count() { return this.#logs.length; }
}

// Ilovaning turli qismlari
function paymentModule() { Logger.getInstance().info("To'lov qabul qilindi"); }
function authModule() { Logger.getInstance().error("Parol noto'g'ri"); }

paymentModule();
authModule();

const a = Logger.getInstance();
const b = Logger.getInstance();
console.log("Bir xil obyektmi?", a === b);   // true
console.log("Jami loglar:", a.count);          // 2
