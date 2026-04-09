from collections import namedtuple, Counter, defaultdict

General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])

class ChibiBattleEasy:
    def __init__(self):
        self.generals = {}
        self.battle_config = {}
        self.stats = {'damage': Counter(), 'losses': defaultdict(int)}
    
    def load_generals(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line == 'EOF':
                    break
                if not line:
                    continue
                parts = line.split()
                faction, name, hp, atk, def_, spd, is_leader = parts
                general = General(faction, name, int(hp), int(atk), int(def_), int(spd), is_leader == 'True')
                self.generals[name] = general
    
    def load_battles(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line == 'EOF':
                    break
                if not line:
                    continue
                parts = line.split()
                if len(parts) < 5 or parts[1] != 'vs':
                    raise ValueError('Invalid battle configuration format')
                attacker_factions = list(parts[0])
                defender_faction = parts[2]
                campaign = parts[3]
                waves = int(parts[4])

                self.battle_config = {
                    'attacker_factions': attacker_factions,
                    'defender_faction': defender_faction,
                    'campaign': campaign,
                    'waves': waves
                }
                return self.battle_config
        return None
    
    def get_battle_order(self):
        return sorted(self.generals.values(), key=lambda g: g.spd, reverse=True)
    
    def calculate_damage(self, attacker_name, defender_name):
        attacker = self.generals[attacker_name]
        defender = self.generals[defender_name]
        damage = max(1, attacker.atk - defender.def_)
        self.stats['damage'][attacker_name] += damage
        self.stats['losses'][defender_name] += damage
        return damage
    
    def simulate_battle(self):
        battle = self.battle_config or {'attacker_factions': ['蜀', '吳'], 'defender_faction': '魏', 'waves': 3}
        attackers = [g for g in self.generals.values() if g.faction in battle['attacker_factions']]
        defenders = [g for g in self.generals.values() if g.faction == battle['defender_faction']]
        attackers = sorted(attackers, key=lambda g: g.spd, reverse=True)
        defenders = sorted(defenders, key=lambda g: g.spd, reverse=True)
        
        for wave in range(battle['waves']):
            for idx, attacker in enumerate(attackers):
                if idx < len(defenders):
                    self.calculate_damage(attacker.name, defenders[idx].name)
    
    def get_damage_ranking(self, top_n=5):
        return self.stats['damage'].most_common(top_n)
    
    def get_faction_stats(self):
        faction_damage = defaultdict(int)
        for name, damage in self.stats['damage'].items():
            faction = self.generals[name].faction
            faction_damage[faction] += damage
        return dict(faction_damage)
    
    def print_report(self):
        print("=== 赤壁戰役 - 傷害報告 ===")
        for i, (name, dmg) in enumerate(self.get_damage_ranking(), 1):
            print(f"{i}. {name}: {dmg} HP")
        
        print("\n=== 勢力統計 ===")
        for faction, total in self.get_faction_stats().items():
            print(f"{faction}: {total} HP")


if __name__ == '__main__':
    game = ChibiBattleEasy()
    game.load_generals('generals.txt')
    game.load_battles('battles.txt')
    game.simulate_battle()
    game.print_report()
