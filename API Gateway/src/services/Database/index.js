export { default as Channels } from './CHANNELS/index.js'
export { default as Posts } from './POSTS/index.js'
export { default as Signals } from './SIGNALS/index.js'

import config from 'config'
import knex from 'knex'

const client = config.database
const conn = config[client]

export default knex({
  client,
  connection: conn,
  // pool: conn.pool || { min: 10, max: 60 }
  // debug: true
})

