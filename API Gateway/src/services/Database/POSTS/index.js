import * as methods from '../methods.js'

const table = 'POSTS'
const ret = {}

const columns = {
  unique_id: 'UID',
  channel_id: 'CHANNEL_ID',
  channel_name: 'CHANNEL_NAME',
  id: 'ID',
  from_id: 'FROM_ID',
  text: 'TEXT',
  date: 'DATE',
  time: 'TIME',
  timezone: 'TIMEZONE',
  views: 'VIEWS',
  forwards: 'FORWARDS',
  edit_date: 'EDIT_DATE',
}

ret.select = conditions => methods.select({name: table, columns}, conditions)
ret.insert = values => methods.insert({name: table, columns}, values)

export default ret
