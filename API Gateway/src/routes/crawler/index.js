import Router from 'koa-router'

import { getChannels, searchChannels } from '../../controllers/index.js'

const router = new Router()

router.post('/crawler/get/channels', getChannels)
router.post('/crawler/find/channels', searchChannels)
// router.get('/crawler/get/channel/:channel/info', getChannelInfo)

export default router.routes()
