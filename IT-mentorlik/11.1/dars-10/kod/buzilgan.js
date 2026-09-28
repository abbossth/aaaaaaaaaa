// Amaliyot uchun: bu kodda SOLID qayerda buzilgan?
class Order {
  constructor(items, paymentType) {
    this.items = items;
    this.paymentType = paymentType;
  }

  total() {
    return this.items.reduce((s, i) => s + i.price * i.qty, 0);
  }

  pay() {
    if (this.paymentType === "click") {
      console.log("Click API'ga so'rov...", this.total());
    } else if (this.paymentType === "payme") {
      console.log("Payme API'ga so'rov...", this.total());
    } else if (this.paymentType === "cash") {
      console.log("Naqd to'lov", this.total());
    }
  }

  saveToDatabase() {
    console.log("INSERT INTO orders ...");
  }

  printReceipt() {
    console.log("=== CHEK ===");
    this.items.forEach((i) => console.log(i.name, i.price * i.qty));
  }

  sendSms(phone) {
    console.log(`SMS ${phone}: Buyurtmangiz qabul qilindi`);
  }
}
