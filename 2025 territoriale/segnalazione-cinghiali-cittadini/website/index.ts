import express from 'express';
import { db, ADMIN_USERNAME } from './database';
import session from 'express-session';
import bodyParser from 'body-parser';
import crypto from 'crypto';
import hashcash from '@mawoka/hashcash';

declare module 'express-session' {
	interface SessionData {
		username: string;
		pow: string;
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

app.use(express.static('public'));
app.set('view engine', 'ejs');

// home page
app.get('/', async (req, res, next) => {
	try {
		const reports = req.session.username
			? await db.selectFrom('entries').selectAll().where('owner', '=', req.session.username).execute()
			: [];

		res.render('index', {
			username: req.session.username,
			reports
		});
	} catch (err) {
		next(err);
	}
});

// register a new user, generating a random username and password
app.post('/register', async (req, res, next) => {
	try {
		const username = crypto.randomUUID();

		await db
			.insertInto('users')
			.values({ username: username, password: crypto.randomUUID() })
			.executeTakeFirstOrThrow();

		// save session
		req.session.username = username;
		res.redirect('/');
	} catch (err) {
		next(err);
	}
});

// login, this is used by the admin
app.post('/login', async (req, res, next) => {
	try {
		// create new entry
		const username = req.body.username;
		const password = req.body.password;

		const user = await db
			.selectFrom('users')
			.selectAll()
			.where('username', '=', username)
			.where('password', '=', password)
			.executeTakeFirst();

		if (user) {
			req.session.username = username;
		}

		res.redirect('/');
	} catch (err) {
		next(err);
	}
});

// create a new cinghiale
app.get('/create', async (req, res, next) => {
	if (!req.session.username) {
		res.redirect('/');
		return;
	}

	try {
		req.session.pow = crypto.randomBytes(4).toString('hex');

		res.render('create', {
			username: req.session.username,
			pow: req.session.pow
		});
	} catch (err) {
		next(err);
	}
});

// create a new cinghiale
app.post('/create', async (req, res, next) => {
	if (!req.session.username) {
		res.redirect('/');
		return;
	}

	try {
		// create new entry
		let address = req.body.address;
		let image = req.body.image;
		let pow = req.body.pow;

		if (!address || !pow || !req.session.pow) {
			res.redirect('/create');
			return;
		}

		// no xss here!
		if (address) {
			address = address.replace('<', '').replace('>', '');
		}
		if (image) {
			image = image.replace('<', '').replace('>', '');
		}

		// verify pow
		if (!hashcash.check(pow, req.session.pow, 26) && pow !== process.env.CHECKER_TOKEN) {
			res.send('Invalid hashcash');
			return;
		}
		req.session.pow = crypto.randomBytes(4).toString('hex');

		const report_id = crypto.randomUUID();

		// insert into db
		await db
			.insertInto('entries')
			.values({
				id: report_id,
				owner: req.session.username,
				address: address,
				image: image
			})
			.execute();

		// trigger the headless admin to visit your page
		await fetch(`http://${process.env.HEADLESS_HOST}`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				'X-Auth': process.env.HEADLESS_AUTH!
			},
			body: JSON.stringify({
				actions: [
					{
						type: 'request',
						url: `${process.env.DOMAIN}/login`,
						method: 'POST',
						headers: {
							'Content-Type': 'application/x-www-form-urlencoded'
						},
						data: `username=${ADMIN_USERNAME}&password=${ADMIN_USERNAME}`
					},
					{
						type: 'request',
						url: `${process.env.DOMAIN}/report/${report_id}`,
						timeout: 5
					},
					{ type: 'sleep', time: 5 }
				]
			})
		});

		res.redirect(`/report/${report_id}`);
	} catch (err) {
		next(err);
	}
});

// see cinghiale
app.get('/report/:id', async (req, res, next) => {
	if (!req.session.username) {
		res.redirect('/');
		return;
	}

	try {
		const report_id = req.params.id;

		const report = await db.selectFrom('entries').selectAll().where('id', '=', report_id).executeTakeFirst();

		if (!report) {
			res.redirect('/');
			return;
		}

		// only the owner and the admin can see the cinghiale
		if (report.owner !== req.session.username && req.session.username !== ADMIN_USERNAME) {
			res.redirect('/');
			return;
		}

		res.render('report', {
			username: req.session.username,
			report,
			is_admin: req.session.username === ADMIN_USERNAME
		});
	} catch (err) {
		next(err);
	}
});

// if the admin accepts the report, then the flag is put inside the address
app.post('/report/:id/accept', async (req, res, next) => {
	if (!req.session.username) {
		res.redirect('/');
		return;
	}

	if (req.session.username !== ADMIN_USERNAME) {
		res.send('Solo gli admin possono approvare una segnalazione');
		return;
	}

	try {
		await db
			.updateTable('entries')
			.set({
				address: process.env.FLAG || 'flag{REDACTED}'
			})
			.where('id', '=', req.params.id)
			.execute();

		res.redirect('/');
	} catch (err) {
		next(err);
	}
});

app.listen(PORT, () => {
	console.log(`App listening on port ${PORT}`);
});
