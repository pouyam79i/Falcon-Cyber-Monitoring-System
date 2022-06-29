import * as methods from '../methods.js'

const table = 'SIGNALS'
const ret = {}

const columns = {
  // date: 'DATE',
  // time: 'TIME',
  info: 'INFO',
  polarity: 'POLARITY',
  symbols: 'SYMBOLS',
  text: 'TEXT',
  uid: 'UID',
}

ret.select = conditions => methods.select({name: table, columns}, conditions)
ret.insert = values => methods.insert({name: table, columns}, values)

export default ret
