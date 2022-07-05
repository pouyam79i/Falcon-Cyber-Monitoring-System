import request from 'superagent'
import config from 'config'

const address = config.crawler?.endpoint || 'localhost:3001'

const getChannels = async ({ ids }) => {
  // const t = request.post(`${address}/channels/get`)
  const t = request.get(`${address}/crawl`)

  try {
    // const result = await t.send({ ids })
    const result = await t
    return result?.body
  } catch (e) {
    throw e
  }
}

export default getChannels
