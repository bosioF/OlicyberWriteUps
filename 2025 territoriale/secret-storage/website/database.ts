import { createPool } from 'mysql2' // do not use 'mysql2/promises'!
import { Kysely, MysqlDialect } from 'kysely'
import { DB } from './db'

const dialect = new MysqlDialect({
  pool: createPool({
    database: process.env.DB_NAME,
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    port: 3306,
    connectionLimit: 10,
  })
})

// Database interface is passed to Kysely's constructor, and from now on, Kysely 
// knows your database structure.
// Dialect is passed to Kysely's constructor, and from now on, Kysely knows how 
// to communicate with your database.
export const db = new Kysely<DB>({
  dialect,
})