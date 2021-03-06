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
        print("val: GET")
        template_values = {
#            'message': '',
#            'schema': '',
#            'schemacode': 'alert-success',
#            'msgcode': 'alert-warning',
#            'schemastatus': '<b>OK</b> - looks about right Skipper.',
#            'msgstatus': '<b>Ruh Roh</b> - something smells fishy!'
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


class Validate(webapp2.RequestHandler):

    def post(self):
        print("val: POST")
        message = self.request.get('messagetxt')
        schema = self.request.get('schematxt')
        status = jadn_val(message, schema)
        form_data = {'msg': message, 'schema': schema, 'status': status}

#        self.redirect('/?' + urllib.urlencode(query_params))

        template = JINJA_ENVIRONMENT.get_template('validate.html')
        self.response.write(template.render(form_data))


app = webapp2.WSGIApplication([
    ('/val', Validate),
    ('/.*', MainPage),
], debug=True)

