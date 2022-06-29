import request from 'superagent'
import config from 'config'

const address = config.analyzer?.endpoint || 'localhost:3001'

const analyze = async (channels) => {
  // const t = request.post(`${address}/channels/get`)
  const t = request.post(`${address}/analyze`)

  try {
    // const result = await t.send({ ids })
    const result = await t.send(channels)
    return result?.body
  } catch (e) {
    throw e
  }
}

export default analyze
