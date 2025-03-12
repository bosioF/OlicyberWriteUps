import express from 'express';
import { db } from './database';
import { UndirectedOrderByExpression } from 'kysely/dist/cjs/parser/order-by-parser';
import { DB } from './db';
import session from 'express-session';
import bodyParser = require('body-parser');
import crypto from 'crypto';

declare module 'express-session' {
	interface SessionData {
		user_id: number;
	}
}

const app = express();
const PORT = 3000;

app.use(
	session({
		secret: crypto.randomBytes(16).toString('hex'),
		resave: false,
		saveUninitialized: false
	})
);

app.use(bodyParser.urlencoded());

app.set('view engine', 'ejs');

app.all('/', async (req, res, next) => {
	try {
		if (req.session.user_id) {
			// user is logged
			if (req.method === 'POST') {
				// create new entry
				const name = req.body.name;
				const secret = req.body.secret;

				if (!!name && !!secret) {
					await db
						.insertInto('entries')
						.values({
							owner: req.session.user_id,
							name: name,
							secret: secret
						})
						.execute();
				}
			} else if (req.method !== 'GET') {
				res.sendStatus(405);
				return;
			}

			// retrieve user information
			const { username } = await db
				.selectFrom('users')
				.selectAll()
				.where('id', '=', req.session.user_id)
				.executeTakeFirstOrThrow();

			// get all entries
			const order_by = (req.query.order ?? 'created_at') as UndirectedOrderByExpression<DB, 'entries', {}>;
			const user_entries = await db
				.selectFrom('entries')
				.where('owner', '=', req.session.user_id)
				.orderBy(order_by)
				.select(['name', 'created_at'])
				.execute();

			res.render('index', {
				username,
				user_entries
			});
		} else {
			if (req.method === 'POST') {
				// register
				const username = crypto.randomUUID();

				// create user
				const { insertId: user_id } = await db
					.insertInto('users')
					.values({ username: username })
					.executeTakeFirstOrThrow();

				// add flag to user entries
				await db
					.insertInto('entries')
					.values({
						owner: Number(user_id),
						name: 'flag',
						secret: process.env.FLAG || 'flag{REDACTED}'
					})
					.execute();

				// save session
				req.session.user_id = Number(user_id);
				res.redirect('/');
				return;
			} else if (req.method !== 'GET') {
				res.sendStatus(405);
				return;
			}

			// show register page
			res.render('register');
		}
	} catch (err) {
		next(err);
	}
});

app.listen(PORT, () => {
	console.log(`App listening on port ${PORT}`);
});
