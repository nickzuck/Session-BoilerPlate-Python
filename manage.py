from sessions.Session import SessionManager

def application(env, start_response):
    print "\n\n----$$$$$$$$----------\n", env
    if 'HTTP_COOKIE' in env:
        cookie = env['HTTP_COOKIE']
    else:
        print 'ELSE CASE'
        cookie = SessionManager().set_session(3)

    start_response('200 OK', [('Set-Cookie', cookie)])
    return ["Hello!"]
