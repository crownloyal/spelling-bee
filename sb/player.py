import uuid4 from uuid
from sb_game import get_session 

class Player:

    def __init__(self):
        self.id = uuid4()
        self.name = 'name'
        self.session = get_session(self)

