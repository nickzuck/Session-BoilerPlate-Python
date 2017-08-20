from sessions.Session import SessionManager
obj = SessionManager()
obj.check_session(key = 'abc')
# print obj.get_session(key = 'abc')
# print obj.load('abc')
print obj.set_session(2)
