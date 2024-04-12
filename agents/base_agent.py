class Agent:
  def __init__(self, name, nationality, role, gender, description=""):
    self.name = name
    self.nationality = nationality
    self.role = role
    self.gender = gender
    self.description = description

    self.balance = 800

    self.primary = None
    # self.secondary = Classic()
    self.secondary = 'Classic'

    self.health = 100
    self.shield = None

    self.current_orbs = 0
    self.current_plants = 0
    self.current_defuses = 0

  def _get_pronoun(self):
    if self.gender == 'male':
      return 'he', 'him'
    elif self.gender == 'female':
      return 'she', 'her'
    else:
      return 'they', 'them'
    
  def set_signiture_ability(self, ability):
    self.signiture_ability = ability

  def set_ultimate_ability(self, ultimate):
    self.ultimate_ability = ultimate

  def set_q_ability(self, ability):
    self.q_ability = ability

  def set_c_ability(self, ability):
    self.c_ability = ability

  def purchase_primary(self, weapon):
    if (self.primary == None or self.primary.used) and self.balance < weapon.price:
      raise ValueError("Not enough balance")
    elif self.balance + self.primary.price < weapon.price:
      raise ValueError("Not enough balance")
    else:
      self.primary = weapon
      self.balance -= weapon.price

  def sell_primary(self):
    if (self.primary == None or self.primary.used):
      raise ValueError('Cannot set primary weapon')
    else:
      self.balance += self.primary.price
      self.primary = None

  def drop_primary(self):
    self.primary = None

  def pickup_primary(self, weapon):
    self.primary = weapon

  def purchase_secondary(self, weapon):
    if (self.secondary == None or self.secondary.used) and self.balance < weapon.price:
      raise ValueError("Not enough balance")
    elif self.balance + self.secondary.price < weapon.price:
      raise ValueError("Not enough balance")
    else:
      self.secondary = weapon
      self.balance -= weapon.price

  def sell_secondary(self):
    if (self.secondary == None or self.secondary.used):
      raise ValueError('Cannot set secondary weapon')
    else:
      self.balance += self.secondary.price
      self.secondary = None

  def drop_secondary(self):
    self.secondary = None

  def pickup_secondary(self, weapon):
    self.secondary = weapon

  def use_signiture(self):
    if self.signiture_ability.on_cooldown:
      raise ValueError("Ability on Cooldown")
    elif self.signiture_ability.current_value == 0:
      raise ValueError("No charges left")
    else:
      print(f"Signiture ability used")
      self.signiture_ability.current_value -= 1
      self.signiture_ability.on_cooldown = True

  def purchase_signiture(self):
    if self.signiture_ability.max_allowed <= self.signiture_ability.current_value:
      raise ValueError("Maximum amount of ability purchased")
    elif self.balance < self.signiture_ability.price:
      raise ValueError("Not enough balance")
    else:
      self.signiture_ability.current_value += 1
      self.balance -= self.signiture_ability.price

  def sell_signiture(self):
    if self.signiture_ability.min_allowed >= self.signiture_ability.current_value:
      raise ValueError(f"Minimum amount of ability required: {self.signiture_ability.min_allowed}")
    elif self.signiture_ability.used:
      raise ValueError("Cannot sell ability")
    else:
      self.signiture_ability.current_value -= 1
      self.balance += self.signiture_ability.price

  def use_q(self):
    if self.q_ability.current_value == 0:
      raise ValueError("No charges left")
    else:
      print('Q ability used')
      self.q_ability.current_value -= 1

  def purchase_q(self):
    if self.q_ability.max_allowed <= self.q_ability.current_value:
      raise ValueError("Maximum amount of ability purchased")
    elif self.balance < self.q_ability.price:
      raise ValueError("Not enough balance")
    else:
      self.q_ability.current_value += 1
      self.balance -= self.q_ability.price

  def sell_q(self):
    if self.q_ability.min_allowed >= self.q_ability.current_value:
      raise ValueError(f"Minimum amount of ability required: {self.q_ability.min_allowed}")
    elif self.q_ability.used:
      raise ValueError("Cannot sell ability")
    else:
      self.q_ability.current_value -= 1
      self.balance += self.q_ability.price

  def use_c(self):
    if self.c_ability.current_value == 0:
      raise ValueError("No charges left")
    else:
      print('C ability used')
      self.c_ability.current_value -= 1

  def purchase_c(self):
    if self.c_ability.max_allowed <= self.c_ability.current_value:
      raise ValueError("Maximum amount of ability purchased")
    elif self.balance < self.c_ability.price:
      raise ValueError("Not enough balance")
    else:
      self.c_ability.current_value += 1
      self.balance -= self.c_ability.price

  def sell_c(self):
    if self.c_ability.min_allowed >= self.c_ability.current_value:
      raise ValueError(f"Minimum amount of ability required: {self.c_ability.min_allowed}")
    elif self.c_ability.used:
      raise ValueError("Cannot sell ability")
    else:
      self.c_ability.current_value -= 1
      self.balance += self.c_ability.price

  def use_ultimate(self):
    if self.ultimate_ability.orbs_required - self.current_orbs > 1:
      raise ValueError("Ultimate not ready")
    elif self.ultimate_ability.orbs_required - self.current_orbs == 1:
      raise ValueError("Ultimate almost ready")
    else:
      print("Ultimate used")
      self.current_orbs = 0

  def purchase_shield(self, shield):
    if self.shield.health == shield.max_health:
      raise ValueError("Current sheild has full health")
    elif self.balance < shield.price:
      raise ValueError("Not enough balance")
    else:
      self.prev_shield = self.shield
      self.shield = shield
      self.balance -= shield.price

  def sell_shield(self):
    if self.shield.used:
      raise ValueError('Cannot sell shield')
    else:
      self.balance += self.shield.price
      self.shield = self.prev_shield

  def plant_spike(self):
    self.current_plants += 1
    self.current_orbs += 1
  
  def defuse_spike(self):
    self.current_defuses += 1
    self.current_orbs += 1

  def kill(self):
    self.current_orbs += 1
    self.balance += 200

  def die(self):
    self.health = 0
    self.shield = None
    self.primary = None
    self.secondary = None
    self.current_orbs += 1

  def spawn(self):
    self.health = 100
    # self.secondary = Classic()
  
  def signiture_status(self):
    print(f"Signiture ability: {self.signiture_ability}")
    print(f"Amount left: {self.signiture_ability.current_value}")
    print(f"On cooldown: {self.signiture_ability.on_cooldown}")

  def q_status(self):
    print(f"Q ability: {self.q_ability}")
    print(f"Amount left: {self.q_ability.current_value}")

  def c_status(self):
    print(f"C ability: {self.c_ability}")
    print(f"Amount left: {self.c_ability.current_value}")

  def ultimate_status(self):
    print(f"Ultimate ability: {self.ultimate_ability}")
    status = 'Ready' if self.ultimate_ability.orbs_required == self.current_orbs else f"{self.current_orbs}/{self.ultimate_ability.orbs_required} orbs"
    print(f"Status: {status}")

  def status_report(self):
    print(f"Agent: {self.name}")
    print("=" * 20)
    print(f"Health: {self.health}")
    print(f"Sheild: {self.shield}")
    print(f"Primary: {self.primary}")
    print(f"Secondary: {self.secondary}")
    
    print('=' * 20)
    self.signiture_status()
    print('-' * 20)
    self.q_status()
    print('-' * 20)
    self.c_status()
    print('-' * 20)
    self.ultimate_status()

    print("=" * 20)
    print(f"Current balance: {self.balance}")
    print(f"Current orbs: {self.current_orbs}")
    print(f"Current plants: {self.current_plants}")
    print(f"Current defuses: {self.current_defuses}")

  def introduce(self):
    p1, p2 = self._get_pronoun()
    print(f"{self.name} is from {self.nationality} and {p1} plays the role of {self.role}")
    


