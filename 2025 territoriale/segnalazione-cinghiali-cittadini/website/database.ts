import { createPool } from 'mysql2'; // do not use 'mysql2/promises'!
import { Kysely, MysqlDialect } from 'kysely';
import { DB } from './db';

const dialect = new MysqlDialect({
	pool: createPool({
		database: process.env.DB_NAME,
		host: process.env.DB_HOST,
		user: process.env.DB_USER,
		password: process.env.DB_PASSWORD,
		port: 3306,
		connectionLimit: 10
	})
});

// Database interface is passed to Kysely's constructor, and from now on, Kysely
// knows your database structure.
// Dialect is passed to Kysely's constructor, and from now on, Kysely knows how
// to communicate with your database.
export const db = new Kysely<DB>({
	dialect
});

// create admin account
export const ADMIN_USERNAME = crypto.randomUUID();

(async () => {
	let retries = 10;
	while (retries > 0) {
		try {
			await db
				.insertInto('users')
				.values({
					username: ADMIN_USERNAME,
					password: ADMIN_USERNAME,
					is_admin: 1
				})
				.executeTakeFirstOrThrow();
			console.log('Db successfully initialized!');
			return;
		} catch {
			console.error('Cannot initialize db, retry in 5 seconds...');
			retries--;
			if (retries == 0) {
				console.error('Maximum attempts reached, quitting');
				process.exit(1);
			}
			await new Promise((resolve) => setTimeout(resolve, 5000));
		}
	}
})();
