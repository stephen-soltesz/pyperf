#!/usr/bin/python


class Node(object):

  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.left = None
    self.right = None

  def insert(self, n, pprint=False):
    if n.key <= self.key:
      if self.left:
        self.left.insert(n)
      else:
        self.left = n
    else:
      if self.right:
        self.right.insert(n)
      else:
        self.right = n

    if pprint:
      self.pprint()

  def delete(self, key):
    pass

  def find(self, key):
    pass

  # | 
  # +-
#  def _line(self, depth, left):
#    if depth == 0:
#      return ''
#
#    if depth == 1:
#      return ' +-'
#
#    r = ' '
#    for f in left[1:-1]:
#      if f:
#        r += '|  '
#      else:
#        r += '   '
#    r += '+-'
#    return r

  #def pprint(self, depth=0, left=(False,)):
  #  print '%s %s' % (self._line(depth, left), self.key)
#
#    if self.left:
#      self.left.pprint(depth + 1, left + (True,))
#
#    if self.right:
#      self.right.pprint(depth + 1, left + (False,))

  def _isleaf(self):
    return not bool(self.left or self.right)

  def pprint(self, depth=0, prefix=' ', suffix=''):
    print '%s%s%s' % (prefix, '+- ' if depth else '', self.key)

    if self.right:
      self.right.pprint(depth + 1, prefix + suffix, '|  ')

    if self.left:
      self.left.pprint(depth + 1, prefix + suffix, '   ')

  def pprint2(self, is_right=True, prefix=''):

    if self.right:
      self.right.pprint2(True, prefix + ('     ' if is_right else '|    '))

    print '%s%s%s' % (prefix, self.key, '' if self._isleaf() else ' --+')

    if self.left:
      self.left.pprint2(False, prefix + ('|    ' if is_right and prefix else '     '))

  def visit(self):
    pass


n = Node(50, '')
n.insert(Node(30, ''))

n.insert(Node(20, ''))
n.insert(Node(40, ''))

n.insert(Node(35, ''))
n.insert(Node(37, ''))
n.insert(Node(45, ''))
n.insert(Node(44, ''))
n.insert(Node(47, ''))
n.insert(Node(25, ''))
n.insert(Node(15, ''))

n.insert(Node(70, ''))

n.insert(Node(60, ''))
n.insert(Node(80, ''))

n.insert(Node(55, ''))
n.insert(Node(65, ''))
n.insert(Node(75, ''))
n.insert(Node(85, ''))

n.pprint()

print '  '
print '  '
print '  '

n.pprint2()
