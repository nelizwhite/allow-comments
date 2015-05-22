import os
import urllib
import concepts

from google.appengine.ext import ndb

import jinja2
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir), )



DEFAULT_GUESTBOOK_NAME = 'default_guestbook'


def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    
    return ndb.Key('Guestbook', guestbook_name)



class Link(ndb.Model):
    
    name = ndb.StringProperty(indexed=False)
    linkurl = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)






class MainPage(webapp2.RequestHandler):
	
    def get(self):
    	guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
    	links_query = Link.query(
            ancestor=guestbook_key(guestbook_name)).order(Link.date)
    	links = links_query.fetch(10)

    	#concepts = concepts.concepts
    	
    	template_values = {

			'links': links,
            
            'guestbook_name': urllib.quote_plus(guestbook_name),

            'concepts1': concepts.concepts1,

            'concepts2': concepts.concepts2,

            'concepts3': concepts.concepts3,

            'concepts4': concepts.concepts4,

            'concepts5': concepts.concepts5,

            'concepts6': concepts.concepts6,

            'concepts7': concepts.concepts7,

            'concepts8': concepts.concepts8,

            'concepts9': concepts.concepts9,

            'concepts10': concepts.concepts10
        


         }


            
    
    		

	template = JINJA_ENVIRONMENT.get_template('index.html')
	self.response.write(template.render(template_values))


class Guestbook(webapp2.RequestHandler):
    def post(self):
        
        guestbook_name = self.request.get('guestbook_name',
                                          DEFAULT_GUESTBOOK_NAME)
        link = Link(parent=guestbook_key(guestbook_name))

        link.name = self.request.get('name')
        
        if type(link.name) != unicode:
            link.name = unicode(self.request.get('name'),'utf-8')
        else:
            link.name = self.request.get('name')
        
        link.linkurl = self.request.get('linkurl')
        
        if type(link.linkurl) != unicode:
            link.linkurl = unicode(self.request.get('linkurl'),'utf-8')
        else:
            link.linkurl = self.request.get('linkurl')
        
        link.put()

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/?' + urllib.urlencode(query_params))



			  
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
], debug=True)













