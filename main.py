from agents.sage import Sage
from roles.role import Role

def main():
  sage = Sage()

  sage.purchase_c()
  # sage.sell_c()
  sage.use_signiture()
  sage.kill()
  sage.kill()
  sage.die()
  sage.spawn()
  sage.plant_spike()

  sage.status_report()

if __name__ == '__main__':
  main()