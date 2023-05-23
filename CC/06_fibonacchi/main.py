import webapp2
class Main(webapp2.RequestHandler):
    def get(self):
        prev = 0
        curr = 1
        for i in range (9):
            self.response.write(prev)
            self.response.write(" ")
            temp = prev
            prev = curr
            curr += temp
app = webapp2.WSGIApplication([('/',Main)],debug = True)  







          























