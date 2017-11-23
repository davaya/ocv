#!/usr/bin/env python

import os
import urllib
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def jadn_val(a, b):
    print(a, b)
    return 'Say wah?'

class MainPage(webapp2.RequestHandler):

    def get(self):
        template_values = {
            'message': '{"action":"deny"}',
            'schema': '{ "meta": {},\n  "types": []\n}',
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class Validate(webapp2.RequestHandler):

    def post(self):

        message = self.request.get('message')
        schema = self.request.get('schema')
        status = jadn_val(message, schema)

        values = {'msg': message, 'schema': schema, 'status': status}

#        query_params = {'message': message}
#        self.redirect('/?' + urllib.urlencode(query_params))

        template = JINJA_ENVIRONMENT.get_template('validate.html')
        self.response.write(template.render(values))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/val', Validate),
], debug=True)

