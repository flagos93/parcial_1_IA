class Node:

  def __init__(self, data, level=0, parent=None):
    self.data = data
    self.level = level
    self.parent = parent
    self.childs = []


  def add_child(self, data, point=None):

    if not point:
      child = Node(data=data, level=self.level+1, parent=self)
      self.childs.append(child)

    else:
      if point == self.data:
        child = Node(data, level=self.level+1, parent=self)
        self.childs.append(child)
      else:
        for child in self.childs:
          child.add_child(data, point=point)

  def print_path(self):
    path = [self.data]
    aux = self.parent

    while aux:
      path.append(aux.data)
      aux = aux.parent

    return path

  def fullprint(self):
    print('  '*self.level + str(self.data))

    if self.childs:
      for child in self.childs:
        child.fullprint()

  def __str__(self):
    fullprint()