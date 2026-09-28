import pg from "pg";
import { createApp, initDb } from "./app.js";

const PORT = process.env.PORT || 3000;
const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL });

await initDb(pool);
createApp(pool).listen(PORT, () => console.log(`API: http://localhost:${PORT}/api/health`));
