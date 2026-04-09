from collections import namedtuple, Counter, defaultdict

General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])

class ChibiBattle:
    def __init__(self):
        self.generals = {}
        self.battle_config = {}
        self.stats = {
            'damage': Counter(),
            'losses': defaultdict(int)
        }
    
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
                
                general = General(
                    faction=faction,
                    name=name,
                    hp=int(hp),
                    atk=int(atk),
                    def_=int(def_),
                    spd=int(spd),
                    is_leader=(is_leader == 'True')
                )
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
    
    def simulate_wave(self, wave_num, battle_config=None):
        battle = battle_config or self.battle_config or {
            'attacker_factions': ['蜀', '吳'],
            'defender_faction': '魏',
            'campaign': '赤壁',
            'waves': 3
        }

        attackers = [g for g in self.generals.values() if g.faction in battle['attacker_factions']]
        defenders = [g for g in self.generals.values() if g.faction == battle['defender_faction']]

        attackers = sorted(attackers, key=lambda g: g.spd, reverse=True)
        defenders = sorted(defenders, key=lambda g: g.spd, reverse=True)

        for i in range(wave_num):
            for idx, attacker in enumerate(attackers):
                if not defenders:
                    break
                defender = defenders[idx % len(defenders)]
                self.calculate_damage(attacker.name, defender.name)
    
    def simulate_battle(self):
        waves = self.battle_config.get('waves', 3)
        for wave in range(1, waves + 1):
            self.simulate_wave(wave)
    
    def get_damage_ranking(self, top_n=5):
        return self.stats['damage'].most_common(top_n)
    
    def get_faction_stats(self):
        faction_damage = defaultdict(int)
        for name, damage in self.stats['damage'].items():
            faction = self.generals[name].faction
            faction_damage[faction] += damage
        return dict(faction_damage)
    
    def get_defeated_generals(self):
        return [name for name, loss in self.stats['losses'].items() 
                if loss >= self.generals[name].hp]
    
    def print_battle_start(self):
        campaign = self.battle_config.get('campaign', '赤壁戰役')
        attacker = ''.join(self.battle_config.get('attacker_factions', ['蜀', '吳']))
        defender = self.battle_config.get('defender_faction', '魏')

        print("╔═══════════════════════════════════════════════════════╗")
        print(f"║        吞食天地 - {campaign} │ {attacker} vs {defender}        ║")
        print("╚═══════════════════════════════════════════════════════╝\n")
        
        for faction in ['蜀', '吳', '魏']:
            print(f"【{faction}軍】")
            generals = [g for g in self.generals.values() if g.faction == faction]
            for g in sorted(generals, key=lambda x: x.spd, reverse=True):
                bar = '█' * (g.hp // 10) + '░' * (10 - g.hp // 10)
                leader = " (軍師)" if g.is_leader else ""
                print(f"  ⚔ {g.name:8} {bar} 攻{g.atk:2} 防{g.def_:2} 速{g.spd:2}{leader}")
            print()
    
    def print_damage_report(self):
        campaign = self.battle_config.get('campaign', '赤壁戰役')
        print("╔═══════════════════════════════════════════════════════╗")
        print(f"║              【{campaign} - 傷害統計報告】                ║")
        print("╚═══════════════════════════════════════════════════════╝\n")
        
        print("【傷害輸出排名 Top 5】")
        for i, (name, dmg) in enumerate(self.get_damage_ranking(), 1):
            bar = '█' * (dmg // 5) + '░' * (20 - dmg // 5)
            print(f"  {i}. {name:8} {bar} {dmg:3} HP")
        
        print("\n【兵力損失統計】")
        for name in sorted(self.stats['losses'].keys(), 
                          key=lambda x: self.stats['losses'][x], reverse=True)[:5]:
            loss = self.stats['losses'][name]
            defeated = "✓" if loss >= self.generals[name].hp else " "
            print(f"  {defeated} {name:8} → 損失 {loss:3} 兵力")
        
        print("\n【勢力傷害統計】")
        faction_stats = self.get_faction_stats()
        max_damage = max(faction_stats.values()) if faction_stats else 1
        for faction in ['蜀', '吳', '魏']:
            total = faction_stats.get(faction, 0)
            ratio = int(total / max_damage * 20) if max_damage else 0
            bar = '█' * ratio + '░' * (20 - ratio)
            percentage = (total / sum(faction_stats.values()) * 100) if faction_stats else 0
            print(f"  {faction} {bar} {total:3} HP ({percentage:5.1f}%)")
        
        print("\n" + "═" * 57)
    
    def run_full_battle(self):
        self.print_battle_start()
        print("【開始三波戰鬥...】\n")
        
        self.simulate_battle()
        
        print("\n【戰役完成】\n")
        self.print_damage_report()


if __name__ == '__main__':
    game = ChibiBattle()
    game.load_generals('generals.txt')
    game.load_battles('battles.txt')
    game.run_full_battle()
