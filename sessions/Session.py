from models import SessionModel

class SessionManager:


    def __init__(self):
        self.sessionModel = SessionModel()

    # Function to get the session value from the database
    def get_session(self, key):
        if key:
            return self.sessionModel.get_by_key(key)

    # Function to set the session value 
    #   1. Insert into database
    #   2. Return the value of session
    def set_session(self, user_id):
        session_key = create_session()
        import json
        session_value = json.dumps({'user': user_id})
        self.sessionModel.insert_session(session_key, session_value)

    # Function to create a unique session key
    def create_session(self):
        import uuid
        return uuid.uuid1().hex

    # Function to check if the session exists for a given key
    def check_session(self, key = None):
        if key is None:
            return False
        else:
            return bool(self.sessionModel.get_by_key(key))


if __name__ == '__main__':
    SessionManager.check_session()