import Koa from 'koa'
import parser from 'koa-bodyparser'
import logger from 'koa-logger'
import views from 'koa-views'
import path from 'path'
import session from 'koa-session'
import config from 'config'
import { fileURLToPath } from 'url'
import { viewRoutes, crawlerRoutes } from './routes/index.js'
// import errorHandler from './utils/errorHandler/index.js'

const __dirname = path.dirname(fileURLToPath(import.meta.url))

const app = new Koa()
app.keys = ['SECRET']

app
	.use(parser())
	.use(logger())
	.use(session(config.session, app))

const PORT = process.env.PORT || 3000

// app.use(errorHandler)
app.use(views( __dirname + '/views', { extension: 'ejs' }))
app.use(viewRoutes)
app.use(crawlerRoutes)

app.listen(PORT, () => console.log(`server is running on port ${PORT}`))
