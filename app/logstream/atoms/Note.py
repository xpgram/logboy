from app.logstream.atoms.LogstreamAtom import LogstreamAtom
from app.enums.View import View

class Note(LogstreamAtom):
  logstreamType = 'note-atom'

  text: str

  @staticmethod
  def create(data):
    return Note(data)
  
  def __init__(self, text: str):
    self.text = text
  
  def save(self):
    return self.text

  def render(self, view):
    if view == View.Compact:
      return ''
    return f'{self.text}'
