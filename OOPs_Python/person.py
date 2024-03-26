class person(object):

  def __init__(self, pname, gender, passion):
    self.name = pname
    self.gender = gender
    self.passion = passion

  def display(self):
    return "Person Name: ", self.name, " Gender: ", self.gender, " Passion: ", self.passion

'''
  name = ""
  gender = ""
  passion = ""
'''

p = person(pname = "Pratham",gender = "Male",passion = "Music")
print(p.name, 'is a', p.gender, 'and is a follower of', p.passion)
