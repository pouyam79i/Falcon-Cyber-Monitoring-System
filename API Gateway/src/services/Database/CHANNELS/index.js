import * as methods from '../methods.js'

const table = 'CHANNELS'
const ret = {}

const columns = {
  name: 'CHANNEL_NAME',
  id: 'CHANNEL_ID'
}

ret.select = conditions => methods.select({name: table, columns}, conditions)
ret.insert = values => methods.insert({name: table, columns}, values)

export default ret
