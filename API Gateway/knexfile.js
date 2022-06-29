import config from 'config'

const client = config.database

export default {
  production: {
    client,
    connection: config[client],
    migrations: {
      tableName: 'MIGRATIONS'
    }
  },
  development: {
    client: 'mysql',
    connection: config[client],
    migrations: {
      tableName: 'MIGRATIONS'
    }
  }
}
