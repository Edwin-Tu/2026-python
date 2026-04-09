import unittest
import os
from collections import Counter
from chibi_battle import ChibiBattle, General


class TestDataLoading(unittest.TestCase):
    """Stage 1: 資料讀取測試"""
    
    def setUp(self):
        self.game = ChibiBattle()
        self.game.load_generals('generals.txt')
    
    def test_load_generals_from_file(self):
        """測試 1-1: 正確讀取 9 位武將"""
        self.assertEqual(len(self.game.generals), 9)
        self.assertIn('劉備', self.game.generals)
        self.assertIn('曹操', self.game.generals)
    
    def test_parse_general_attributes(self):
        """測試 1-2: 正確解析武將屬性"""
        general = self.game.generals['關羽']
        self.assertEqual(general.name, '關羽')
        self.assertEqual(general.atk, 28)
        self.assertEqual(general.def_, 14)
        self.assertEqual(general.spd, 85)
        self.assertEqual(general.faction, '蜀')
    
    def test_faction_distribution(self):
        """測試 1-3: 三國分布正確"""
        factions = Counter(g.faction for g in self.game.generals.values())
        
        self.assertEqual(factions['蜀'], 3)
        self.assertEqual(factions['吳'], 3)
        self.assertEqual(factions['魏'], 3)
    
    def test_eof_parsing(self):
        """測試 1-4: 正確識別 EOF 結尾"""
        self.assertEqual(len(self.game.generals), 9)
    
    def test_leader_identification(self):
        """測試 1-5: 正確識別軍師"""
        self.assertTrue(self.game.generals['諸葛亮'].is_leader)
        self.assertFalse(self.game.generals['關羽'].is_leader)

    def test_load_battles_from_file(self):
        """測試 1-6: 正確讀取 battles.txt 戰役配置"""
        battle_config = self.game.load_battles('battles.txt')
        self.assertEqual(battle_config['attacker_factions'], ['蜀', '吳'])
        self.assertEqual(battle_config['defender_faction'], '魏')
        self.assertEqual(battle_config['campaign'], '赤壁')
        self.assertEqual(battle_config['waves'], 3)


class TestBattleLogic(unittest.TestCase):
    """Stage 2: 戰鬥模擬與統計測試"""
    
    def setUp(self):
        self.game = ChibiBattle()
        self.game.load_generals('generals.txt')
        self.game.load_battles('battles.txt')
    
    def test_battle_order_by_speed(self):
        """測試 2-1: 根據速度排序戰鬥順序"""
        battle_order = self.game.get_battle_order()
        
        self.assertEqual(battle_order[0].spd, 85)
        self.assertEqual(battle_order[-1].spd, 60)
    
    def test_calculate_damage(self):
        """測試 2-2: 正確計算傷害 (攻擊 - 防禦)"""
        damage = self.game.calculate_damage('關羽', '夏侯惇')
        
        self.assertEqual(damage, 28 - 14)
    
    def test_damage_counter_accumulation(self):
        """測試 2-3: Counter 自動累加傷害"""
        self.game.calculate_damage('關羽', '曹操')
        self.game.calculate_damage('關羽', '曹操')
        
        self.assertEqual(self.game.stats['damage']['關羽'], 24)
    
    def test_simulate_one_wave(self):
        """測試 2-4: 模擬一波戰鬥"""
        self.game.simulate_wave(1)
        
        total_damage = sum(self.game.stats['damage'].values())
        self.assertGreater(total_damage, 0)
    
    def test_simulate_three_waves(self):
        """測試 2-5: 模擬三波完整戰役"""
        self.game.simulate_battle()
        
        shu_wu_damage = sum(
            dmg for name, dmg in self.game.stats['damage'].items()
            if self.game.generals[name].faction in ['蜀', '吳']
        )
        wei_damage = sum(
            dmg for name, dmg in self.game.stats['damage'].items()
            if self.game.generals[name].faction == '魏'
        )
        
        self.assertGreater(shu_wu_damage, wei_damage)
    
    def test_troop_loss_tracking(self):
        """測試 2-6: defaultdict 追蹤兵力損失"""
        self.game.simulate_battle()
        
        self.assertGreater(self.game.stats['losses']['曹操'], 0)
    
    def test_damage_ranking_most_common(self):
        """測試 2-7: most_common() 傷害排名"""
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        
        damages = [dmg for _, dmg in ranking]
        self.assertEqual(damages, sorted(damages, reverse=True))
    
    def test_faction_damage_stats(self):
        """測試 2-8: 按勢力統計傷害"""
        self.game.simulate_battle()
        faction_stats = self.game.get_faction_stats()
        
        self.assertGreater(faction_stats.get('蜀', 0), 0)
        self.assertGreater(faction_stats.get('吳', 0), 0)
    
    def test_defeated_generals(self):
        """測試 2-9: 正確識別戰敗將領"""
        self.game.simulate_battle()
        defeated = self.game.get_defeated_generals()
        
        self.assertIsInstance(defeated, list)


class TestRefactoring(unittest.TestCase):
    """Stage 3: 重構測試"""
    
    def setUp(self):
        self.game = ChibiBattle()
        self.game.load_generals('generals.txt')
    
    def test_stats_unchanged_after_refactor(self):
        """測試 3-1: 重構後統計結果不變"""
        self.game.simulate_battle()
        
        damage_before = dict(self.game.stats['damage'])
        losses_before = dict(self.game.stats['losses'])
        
        self.assertEqual(dict(self.game.stats['damage']), damage_before)
        self.assertEqual(dict(self.game.stats['losses']), losses_before)
    
    def test_all_stage1_tests_still_pass(self):
        """測試 3-2: Stage 1 測試仍通過"""
        self.game.load_generals('generals.txt')
        self.assertEqual(len(self.game.generals), 9)
    
    def test_all_stage2_tests_still_pass(self):
        """測試 3-3: Stage 2 測試仍通過"""
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        self.assertEqual(len(ranking), 5)


if __name__ == '__main__':
    unittest.main()
