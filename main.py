import webapp2
import blackscholes
import hestonmc

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/html'
    body = """<HTML><BODY>
    <A HREF=\"BlackScholes?S=2.8&K=2.9&T=0.083333333&r=0.01&v=0.2\">BlackScholes</A><BR>
    <A HREF=\"HestonMC?S=52&K=50&r=0.02&t=30&v=0.09&rho=0.5&kappa=2&theta=0.01&vol=0.12&paths=1000\">HestonMC</A></BR>
    </BODY></HTML>"""
    self.response.write(body)

class TestPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    for i in self.request.arguments():
            self.response.write(i + ':' + self.request.get(i) + '\n')

class BsPage(webapp2.RequestHandler):
  def get(self):
    args = ['S','K','T','r','v']
    S = float(self.request.get('S'))
    K = float(self.request.get('K'))
    T = float(self.request.get('T'))
    r = float(self.request.get('r'))
    v = float(self.request.get('v',0.2))

    bs = blackscholes.BlackScholes('c', S, K, T, r, v)

    self.response.headers['Content-Type'] = 'text/html'
    self.response.write('<HTML><BODY>')
    self.response.write('<H1>Black Scholes</H1>')
    self.response.write('<TABLE>')
    
    for i in args:
      self.response.write('<TR><TD>' + i + '</TD><TD>' + self.request.get(i,'N/A') + '</TD></TR>')

    self.response.write('<TR><TD>Black Scholes</TD><TD>' + str(bs) + '</TD></TR>')
    self.response.write('</TABLE>')
    self.response.write('</BODY></HTML>')

class HestonMCPage(webapp2.RequestHandler):
  def get(self):
    args = ['S','K','r','t','v','rho','kappa','theta','vol','paths']
    S = float(self.request.get('S'))
    K = float(self.request.get('K'))
    r = float(self.request.get('r'))
    t = int(self.request.get('t'))
    v = float(self.request.get('v'))
    rho = float(self.request.get('rho'))
    kappa = float(self.request.get('kappa'))
    theta = float(self.request.get('theta'))
    vol = float(self.request.get('vol'))
    paths = int(self.request.get('paths'))

    hstn = hestonmc.HestonMC(S,K,r,t,v,rho,kappa,theta,vol,paths)

    self.response.headers['Content-Type'] = 'text/html'
    self.response.write('<HTML><BODY>')
    self.response.write('<H1>HestonMC</H1>')

    self.response.write('<TABLE>')
    for i in args:
      self.response.write('<TR><TD>' + i + '</TD><TD>' + self.request.get(i,'N/A') + '</TD></TR>')
    self.response.write('<TR><TD>HestonMC</TD><TD>' + str(hstn) + '</TD></TR>')
    self.response.write('</TABLE>')

    self.response.write('</BODY></HTML>')

application = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/test', TestPage),
  ('/BlackScholes', BsPage),
  ('/HestonMC', HestonMCPage),
], debug=True)
