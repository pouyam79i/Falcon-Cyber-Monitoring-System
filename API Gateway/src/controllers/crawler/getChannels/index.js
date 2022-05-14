import { GetChannels } from '../../../services/index.js'

const getChannels = async (ctx) => {
  const { channels } = ctx.request.body
  try {
    const result = await GetChannels({ ids: channels })
    ctx.assert(result, 500)
    ctx.body = result
  } catch (e) {
    console.log(e)
    ctx.throw(e)
  }
}

export default getChannels
