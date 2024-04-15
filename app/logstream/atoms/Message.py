from app.logstream.atoms.LogStreamAtom import LogStreamAtom
from app.enums.View import View

class Message(LogStreamAtom):
  logstreamType = 'message-atom'

  text: str

  @staticmethod
  def create(data):
    return Message(data)
  
  def __init__(self, text: str):
    self.text = text
  
  def save(self):
    return self.text

  def render(self, view):
    if view == View.Compact:
      return ''
    return f' - {self.text}'
