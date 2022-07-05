export const up = function (knex) {
  const changes = []
  changes.push(knex.schema.hasTable('CHANNELS').then(exists => {
    if (!exists) {
      return knex.schema.createTable('CHANNELS', function (table) {
        table.string('CHANNEL_NAME', 128).primary()
        table.string('CHANNEL_ID', 128)
        table.collate('utf8mb4_general_ci')
      })
    }
  }))

  changes.push(knex.schema.hasTable('POSTS').then(exists => {
    if (!exists) {
      return knex.schema.createTable('POSTS', function (table) {
        table.string('UID', 256).index()
        table.string('CHANNEL_ID', 128).notNullable()
        table.string('CHANNEL_NAME', 128).notNullable()
        table.bigInteger('ID').notNullable()
        table.string('FROM_ID', 128)
        table.text('TEXT')
        table.string('DATE', 30)
        table.string('TIME', 30)
        table.string('TIMEZONE', 30)
        table.integer('VIEWS')
        table.integer('FORWARDS')
        table.string('EDIT_DATE', 30)
        table.timestamp('TIMESTAMP')
        table.collate('utf8mb4_general_ci')
      })
    }
  }))

  changes.push(knex.schema.hasTable('SIGNALS').then(exists => {
    if (!exists) {
      return knex.schema.createTable('SIGNALS', function (table) {
        table.string('UID', 256).primary()
        table.string('SYMBOLS', 256)
        table.integer('POLARITY')
        // table.string('DATE', 30)
        // table.string('TIME', 30)
        table.text('INFO')
        table.text('TEXT')
        table.foreign('UID').references('UID').inTable('POSTS')
        table.timestamp('TIMESTAMP')
        table.collate('utf8mb4_general_ci')
      })
      }
    }))

  return Promise.all(changes)

}

export const down = () => {

}
