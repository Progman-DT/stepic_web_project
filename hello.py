
def application(environ, start_response):
  start_response('200 OK', [('Content-Type', 'text/plain')])
  qs = environ['QUERY_STRING']
  ls = qs.split('&');
  return ls
