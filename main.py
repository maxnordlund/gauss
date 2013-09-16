#!/usr/bin/env python3

class RowMethod:
  "This represents a method on a row"
  __slots__ = ("name")

  def __init__(this, name):
    this.name = name

  def __call__(this, self, other):
    "This is this method object, self is the row this method is being called"
    "on and other is the second parameter to this overloaded method."
    if isinstance(other, Row):
      if len(self) == len(other):
        for index, value in enumerate(other):
          # self.data[index] += value
          getattr(self.data[index], this.name)(value)
        else:
          raise TypeError("Rows must be of equal length to add")
      else:
        for index, value in enumerate(self):
          # self.data[index] += other
          getattr(self.data[index], this.name)(other)

class MetaRow(type):
  "Metaclass for matrix rows"
  def __init__(cls, name, bases, dict):
    super(MetaRow, cls).__init__(name, bases, dict)
    methods = ("add", "sub", "mul", "truediv")
    for name in methods:
      for modifier in ("__%s__", "__r%s__", "__i%s__"):
        method = RowMethod(modifier % name)
        setattr(cls, method.name, method)

class Row(list):
  "This represents a single row of a matrix"
  __metaclass__ = MetaRow
  __slots__ = ("data")

  def __init__(self, data):
    self.data = data

