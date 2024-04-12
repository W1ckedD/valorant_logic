from agents.base_agent import Agent
from roles.role import sentinel
from abilities.ability import Ability, Ultimate

def Sage():
  sage = Agent(
    name='Sage',
    nationality='China',
    gender='female',
    role=sentinel,
    description="Sage equips various orbs which can slow enemies, heal allies, or erect walls to control the battlefield. Her ultimate, Resurrection, can even bring dead allies back to life, swinging the balance of power in a match in seconds. Sage thrives when she's behind her team, hidden from enemy fire."
  )

  ultimate = Ultimate(
    name='Resurection',
    description='',
    orbs=8
  )

  sage.set_ultimate_ability(ultimate)

  signiture = Ability(
    name='Heal',
    description="",
    price=0,
    cooldown=40,
    max_allowed=1,
    min_allowed=1,
    current_value=1
  )

  sage.set_signiture_ability(signiture)

  q_ability = Ability(
    name='Slow Orb',
    description="",
    price=200,
    min_allowed=0,
    max_allowed=2,
    cooldown=0
  )

  sage.set_q_ability(q_ability)

  c_ability = Ability(
    name="Wall",
    description="",
    price=400,
    min_allowed=0,
    max_allowed=1,
    cooldown=0
  )

  sage.set_c_ability(c_ability)

  return sage