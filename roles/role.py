class Role:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def introduce(self):
    print(f"The {self.name} role:\n")
    print(self.description)

  def __str__(self):
    return self.name
  

sentinel = Role(
  name='Sentinel',
  description=''
)