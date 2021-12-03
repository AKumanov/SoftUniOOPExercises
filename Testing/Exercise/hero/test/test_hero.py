from unittest import TestCase, main

from project_hero_testig.hero import Hero


class HeroTest(TestCase):
    def setUp(self):
        self.hero = Hero("kumana", 29, 90.5, 90.5)

    def test_init_method(self):
        username = 'kumana'
        level = 29
        health = 90.5
        damage = 90.5
        self.assertEqual(username, self.hero.username)
        self.assertEqual(level, self.hero.level)
        self.assertEqual(health, self.hero.health)
        self.assertEqual(damage, self.hero.damage)

    def test_battle_attack_yourself_raises(self):
        enemy_hero = Hero("kumana", 29, 90.5, 90.6)
        expected = "You cannot fight yourself"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual(expected, str(ex.exception))

    def test_battle_low_health_raises(self):
        my_hero = Hero("kumana", 29, 0, 10)
        enemy_hero = Hero("test", 29, 90.5, 90.6)
        expected = "Your health is lower than or equal to 0. You need to rest"
        with self.assertRaises(Exception) as ex:
            my_hero.battle(enemy_hero)
        self.assertEqual(expected, str(ex.exception))

    def test_battle_enemy_low_health_raises(self):
        my_hero = Hero("kumana", 29, 10, 10)
        enemy_hero = Hero("test", 29, 0, 90.6)
        expected = f"You cannot fight {enemy_hero.username}. He needs to rest"
        with self.assertRaises(Exception) as ex:
            my_hero.battle(enemy_hero)
        self.assertEqual(expected, str(ex.exception))

    def test_battle_subtract_health_from_user_and_enemy_and_returns_lose_message(self):
        enemy_hero = Hero("test", 29, 30, 1)
        my_hero = Hero("kumana", 29, 30, 1)
        expected_message = "You lose"
        self.assertEqual(expected_message, my_hero.battle(enemy_hero))
        self.assertEqual(1, my_hero.health)
        self.assertEqual(6, enemy_hero.health)

    def test_battle_you_win_adds_health_and_power_and_level_to_hero(self):
        my_hero = Hero("test", 29, 30, 30)
        my_enemy = Hero("enemy", 29, 29, 1)
        prior_health = my_hero.health + 5
        prior_damage = my_hero.damage + 5
        prior_level = my_hero.level + 1
        my_hero.battle(my_enemy)
        self.assertEqual(prior_level, my_hero.level)
        self.assertEqual(prior_damage, my_hero.damage)
        self.assertEqual(prior_health - (my_enemy.damage * my_enemy.level), my_hero.health)

    def test_battle_enemy_wins_adds_health_and_power_and_level_to_enemy(self):
        my_hero = Hero("test", 29, 29, 1)
        my_enemy = Hero("enemy", 29, 30, 30)
        prior_health = my_enemy.health + 5
        prior_level = my_enemy.level + 1
        prior_damage = my_enemy.damage + 5
        my_hero.battle(my_enemy)
        self.assertEqual(prior_level, my_enemy.level)
        self.assertEqual(prior_damage, my_enemy.damage)
        self.assertEqual(prior_health, my_enemy.damage)


    def test_battle_you_win_message(self):
        enemy_hero = Hero("test", 29, 29, 1)
        my_hero = Hero("kumana", 29, 30, 1)
        expected_message = "You win"
        self.assertEqual(expected_message, my_hero.battle(enemy_hero))

    def test_battle_draw(self):
        enemy_hero = Hero("test", 29, 29, 1)
        my_hero = Hero("kumana", 29, 29, 1)
        expected_message = "Draw"
        self.assertEqual(expected_message, my_hero.battle(enemy_hero))

    def test_string_method(self):
        my_hero = Hero("kumana", 29, 29, 1)
        expected_message = f"Hero {my_hero.username}: {my_hero.level} lvl\n" \
                           f"Health: {my_hero.health}\n" \
                           f"Damage: {my_hero.damage}\n"
        self.assertEqual(expected_message, my_hero.__str__())


if __name__ == '__main__':
    main()
