#!/usr/bin/python

bind = "0.0.0.0:8080"

def wsgi_app(environ, start_response):
  start_response('200 OK', [('Content-Type', 'text/plain')])
  qs = environ['QUERY_STRING']
  ls = qs.split('&');
  return ls
