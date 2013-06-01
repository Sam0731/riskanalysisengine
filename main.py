import webapp2

class MainPage(webapp2.RequestHandler):

  def get(self):
    param = self.request.get('param')
    ttt = self.request.get('ttt')

    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('param=' + param + '\n')
    self.response.write('ttt=' + ttt + '\n')

class TestPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('hogehoge')

application = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/test', TestPage),
], debug=True)
