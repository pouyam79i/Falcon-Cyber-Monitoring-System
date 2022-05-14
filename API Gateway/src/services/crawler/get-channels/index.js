import request from 'superagent'
import config from 'config'

const address = config.crawler?.endpoint || 'localhost:3001'

const getChannels = async ({ ids }) => {
  const t = request.post(`${address}/channels/get`)

  try {
    const result = await t.send({ ids })
    return result?.body || false
  } catch (e) {
    throw e
  }
}

export default getChannels
