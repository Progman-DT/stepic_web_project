#!/usr/bin/python

def wsgi_app(env, start_response):
  start_response('200 OK', [('Content-Type', 'text/plain')])
  
