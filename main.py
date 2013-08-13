#!/usr/bin/env python3

class MetaPickler(type):
  "Metaclass for gnosis.xml.pickle serialization"
  def __init__(cls, name, bases, dict):
    from gnosis.xml.pickle import dumps
    super(MetaPickler, cls).__init__(name, bases, dict)
    setattr(cls, 'dumps', dumps)


class Row(list):
  __slots__ = ("data")

  def __init__(self, data):
    self.data = data
  # TODO: Add metaclass to tidy up arithmetic methods,
  # maybe us inheritance from list for common stuff

  def __iadd__(self, other):
    if isinstance(other, Row):
      if len(self) == len(other):
        for index, value in enumerate(other):
          # self.data[index].__iadd__(value)
          self.data[index] += value
        else:
          raise TypeError("Rows must be of equal length to add")
      else:
        for index, value in enumerate(self):
          # self.data[index].__iadd__(other)
          self.data[index] += other

