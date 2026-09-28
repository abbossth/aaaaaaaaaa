// Foydalanish:
//   node index.js add "Uy vazifasini qilish"
//   node index.js list
//   node index.js done 1
//   node index.js remove 1
import fs from "node:fs";
import chalk from "chalk";

const FILE = new URL("./todos.json", import.meta.url);

function load() {
  if (!fs.existsSync(FILE)) return [];
  return JSON.parse(fs.readFileSync(FILE, "utf-8"));
}

function save(todos) {
  fs.writeFileSync(FILE, JSON.stringify(todos, null, 2));
}

const [command, ...args] = process.argv.slice(2);
const todos = load();

switch (command) {
  case "add": {
    const text = args.join(" ").trim();
    if (!text) {
      console.log(chalk.red("Vazifa matnini yozing"));
      break;
    }
    todos.push({ id: Date.now(), text, done: false });
    save(todos);
    console.log(chalk.green(`✅ Qo'shildi: ${text}`));
    break;
  }
  case "list":
    if (todos.length === 0) console.log(chalk.gray("Ro'yxat bo'sh"));
    todos.forEach((t, i) => {
      const mark = t.done ? chalk.green("✔") : chalk.yellow("○");
      console.log(`${i + 1}. ${mark} ${t.done ? chalk.strikethrough(t.text) : t.text}`);
    });
    break;
  case "done": {
    const todo = todos[Number(args[0]) - 1];
    if (!todo) {
      console.log(chalk.red("Bunday raqam yo'q"));
      break;
    }
    todo.done = true;
    save(todos);
    console.log(chalk.green(`🎉 Bajarildi: ${todo.text}`));
    break;
  }
  case "remove": {
    const [removed] = todos.splice(Number(args[0]) - 1, 1);
    save(todos);
    console.log(removed ? chalk.red(`🗑 O'chirildi: ${removed.text}`) : "Bunday raqam yo'q");
    break;
  }
  default:
    console.log(`Buyruqlar: ${chalk.cyan("add <matn> | list | done <n> | remove <n>")}`);
}
