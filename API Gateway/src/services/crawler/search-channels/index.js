import request from 'superagent'
import config from 'config'

const address = config.crawler?.endpoint || 'localhost:3001'

const searchChannels = async ({ names }) => {
  const t = request.post(`${address}/channels/search`)

  try {
    const result = await t.send({ names })
    return result?.body || false
  } catch (e) {
    throw e
  }
}

export default searchChannels
