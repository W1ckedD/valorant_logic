class Ability:
  def __init__(self, name, description, price=200, min_allowed=0, max_allowed=1, cooldown=40, current_value=0):
    self.name = name
    self.description = description
    self.price = price
    self.min_allowed = min_allowed
    self.max_allowed = max_allowed
    self.cooldown = cooldown
    self.on_cooldown = False
    self.current_value = current_value
    self.used = False

  def __str__(self):
    return self.name

class Ultimate:
  def __init__(self, name, description, orbs=7):
    self.name = name
    self.description = description
    self.orbs_required = orbs

  def __str__(self):
    return self.name