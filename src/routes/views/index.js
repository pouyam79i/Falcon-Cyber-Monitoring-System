import Router from 'koa-router'
import config from 'config';

const router = new Router()

router.get('/', async ctx => {
  ctx.redirect('/login')
})

router.get('/login', async ctx => {
  if (ctx.session.isAuthenticated) {
    return (ctx.redirect('/panel'))
  }
  await ctx.render('login.ejs')
})

router.get('/panel', async ctx => {
  if (ctx.session.isAuthenticated) {
    return (await ctx.render('panel', {
      name: ctx.session.name,
      res: 'results appear here'
    }))
  }
  ctx.redirect('/')
})

router.post('/login', async ctx => {
  const { auth } = config
  const { username, password } = ctx.request.body
  if (auth?.[username] === password) {
    ctx.session = {
      name: username,
      isAuthenticated: true
    }
  }
  ctx.redirect('/')
})

export default router.routes()
