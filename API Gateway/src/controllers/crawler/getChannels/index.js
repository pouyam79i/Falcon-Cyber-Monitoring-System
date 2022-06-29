import { GetChannels, Analyze } from '../../../services/index.js'
import { Channels, Posts, Signals } from '../../../services/Database/index.js'

const getChannels = async (ctx) => {
  const { channels } = ctx.request.body
  let posts
  try {
    posts = await GetChannels({ids: channels})
    ctx.assert(posts, 404)
    await Posts.insert(posts)
  } catch (e) {
    console.log(e.message)
    throw e
  }
  try {
    const analyzeResults = await Analyze(posts)
    await Signals.insert(analyzeResults)
    ctx.body = {success: !!analyzeResults}
  } catch (e) {
    console.log(e.message)
    ctx.throw(e)
  }
}

const get_unique_uid = (posts_service, posts_db) => {

}

export default getChannels
