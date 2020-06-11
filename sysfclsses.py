imgs_dir = ''
numberclass_status = 'fwln00266387742973'


class aez_the_vagabond_ex:
    name = 'Aez the Vagabond Ex'
    guild = 'Avalonians'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['Crit', 'Shield', 'Noble']
    image_path = imgs_dir + 'aez_the_vagabond_ex.png'
    turns_texts = ['RB:  Shield 600 & all Avalonians Shield 300', 'RY:  Noble Shield 600 & Crit 1', 'R:  Shield Bash 500']
    turn1_d = {'cost': 'RB', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Shield', 'operator': '+', 'value': 600, 'sign': None}, 'sp': {'number': 1, 'target': {'all': True, 'opp': False, 'allspec': 'Avalonians'}, 'ability': 'Shield', 'operator': '+', 'value': 300, 'sign': None}}
    turn2_d = {'cost': 'RY', 'fp': {'number': 1, 'attribute': 'Noble', 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Shield', 'operator': '+', 'value': 600, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Crit', 'operator': '+', 'value': 1, 'sign': None}}
    turn3_d = {'cost': 'R', 'fp': {'number': 1, 'ability': 'Shield Bash', 'value': 500, 'sign': None}, 'sp': None}

class aez_king_of_avalonia:
    name = 'Aez, king of Avalonia'
    guild = 'Avalonians'
    class_ = 'Warrior'
    strength = '125'
    race = 'Human'
    tags = ['+STR', 'Brave', 'Noble', 'Riposte']
    image_path = imgs_dir + 'aez_king_of_avalonia.png'
    turns_texts = ['RB:  Brave Hit 400, +150 x Avalonians ally', 'R:  all Avalonians Riposte 2 & All R->S', 'Y:  STR +100 & Noble Hit 200']
    turn1_d = {'cost': 'RB', 'fp': {'number': 1, 'attribute': 'Brave', 'ability': 'Hit', 'value': 400, 'sign': '+', 'addvalue': 150, 'incr_opp': False, 'addability': 'Avalonians'}, 'sp': None}
    turn2_d = {'cost': 'R', 'fp': {'number': 1, 'target': {'all': True, 'opp': False, 'allspec': 'Avalonians'}, 'ability': 'Riposte', 'operator': '+', 'value': 2, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'R->S', 'value': 'All', 'sign': None}}
    turn3_d = {'cost': 'Y', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'STR', 'operator': '+', 'value': 100, 'sign': None}, 'sp': {'number': 1, 'attribute': 'Noble', 'ability': 'Hit', 'value': 200, 'sign': None}}

class announ_tho:
    name = 'Announ Tho'
    guild = 'Avalonians'
    class_ = 'Priest'
    strength = '80'
    race = 'Human'
    tags = ['+DMG', 'Fireball', 'Noble', 'Purify', 'Shock']
    image_path = imgs_dir + 'announ_tho.png'
    turns_texts = ['Y:  Shock 400 & Purify 1', 'RB:  Noble Fireball 500', 'RR:  Noble Hit 500 & DMG +250']
    turn1_d = {'cost': 'Y', 'fp': {'number': 1, 'ability': 'Shock', 'value': 400, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Purify', 'value': 1, 'sign': None}}
    turn2_d = {'cost': 'RB', 'fp': {'number': 1, 'attribute': 'Noble', 'ability': 'Fireball', 'value': 500, 'sign': None}, 'sp': None}
    turn3_d = {'cost': 'RR', 'fp': {'number': 1, 'attribute': 'Noble', 'ability': 'Hit', 'value': 500, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': '+DMG', 'operator': ':', 'value': 250, 'sign': None}}

class boyl_ex:
    name = 'Boyl Ex'
    guild = 'Avalonians'
    class_ = 'Warrior'
    race = 'Human'
    strength = '100'
    tags = ['+STR', 'Crit', 'Noble']
    image_path = imgs_dir + 'boyl_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class deirf_geis:
    name = 'Deirf Geis'
    guild = 'Avalonians'
    class_ = 'Marauder'
    race = 'Human'
    strength = '170'
    tags = ['Crit', 'Scarab', 'Brave']
    image_path = imgs_dir + 'deirf_geis.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class eludeselle_ex:
    name = 'Eludeselle Ex'
    guild = 'Avalonians'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Shield', 'Frostbite', 'Noble', 'Riposte']
    image_path = imgs_dir + 'eludeselle_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class enguerrand:
    name = 'Enguerrand'
    guild = 'Avalonians'
    class_ = 'Warrior'
    strength = '115'
    race = 'Human'
    tags = ['+STR', 'Brave', 'Shock']
    image_path = imgs_dir + 'enguerrand.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class general_sineid_ex:
    name = 'General Sineid Ex'
    guild = 'Avalonians'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['+DMG', 'Noble', 'Shock', 'Spellbreaker']
    image_path = imgs_dir + 'general_sineid_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class great_duke:
    name = 'Great Duke'
    guild = 'Avalonians'
    class_ = 'Priest'
    race = 'Human'
    strength = '150'
    tags = ['+STR', 'Noble', 'Purify', 'Shock', 'Smite']
    image_path = imgs_dir + 'great_duke.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class johan_of_avalonia:
    name = 'Johan of Avalonia'
    guild = 'Avalonians'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Shield', 'Brave']
    image_path = imgs_dir + 'johan_of_avalonia.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kaes_the_heroic_ex:
    name = 'Kaes the Heroic Ex'
    guild = 'Avalonians'
    class_ = 'Warrior'
    race = 'Human'
    strength = '125'
    tags = ['+DMG', 'Dodge', 'Brave', 'Shock', 'Spellbreaker']
    image_path = imgs_dir + 'kaes_the_heroic_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class knight_oscar:
    name = 'Knight Oscar'
    guild = 'Avalonians'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['+STR', 'Shield', 'Noble', 'Riposte']
    image_path = imgs_dir + 'knight_oscar.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class konis:
    name = 'Konis'
    guild = 'Avalonians'
    class_ = 'Warrior'
    race = 'Human'
    strength = '125'
    tags = ['+STR', 'Brave']
    image_path = imgs_dir + 'konis.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lady_jane_ex:
    name = 'Lady Jane Ex'
    guild = 'Avalonians'
    class_ = 'Priest'
    race = 'Human'
    strength = '150'
    tags = ['Shield', 'Heal', 'Noble', 'Purify', 'Shock']
    image_path = imgs_dir + 'lady_jane_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class merlin_of_avalonia:
    name = 'Merlin of Avalonia'
    guild = 'Avalonians'
    class_ = 'Mage'
    race = 'Human'
    strength = '110'
    tags = ['+DMG', 'Crit', 'Brave', 'Fireball']
    image_path = imgs_dir + 'merlin_of_avalonia.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class myria_of_avalonia:
    name = 'Myria of Avalonia'
    guild = 'Avalonians'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['Shield', 'Heal', 'Noble', 'Spellbreaker', 'Fireball']
    image_path = imgs_dir + 'myria_of_avalonia.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class nalen_ex:
    name = 'Nalen Ex'
    guild = 'Avalonians'
    class_ = 'Marauder'
    race = 'Dais'
    strength = '150'
    tags = ['Thorn', 'Heal', 'Noble', 'Backstab']
    image_path = imgs_dir + 'nalen_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ogmios_sv:
    name = 'Ogmios Sv'
    guild = 'Avalonians'
    class_ = 'Colossus'
    race = 'Unknown(R)'
    strength = '300'
    tags = ['+DMG', '+STR', 'Noble']
    image_path = imgs_dir + 'ogmios_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class panturien_sv:
    name = 'Panturien Sv'
    guild = 'Avalonians'
    class_ = 'Colossus'
    race = 'Beast'
    strength = '200'
    tags = ['+STR', 'Shield', 'Noble']
    image_path = imgs_dir + 'panturien_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class princess_deliah_ex:
    name = 'Princess Deliah Ex'
    guild = 'Avalonians'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['Dodge', 'Brave', 'Riposte']
    image_path = imgs_dir + 'princess_deliah_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class psalm_the_poet:
    name = 'Psalm, the Poet'
    guild = 'Avalonians'
    class_ = 'Bard'
    race = 'Human'
    strength = '0'
    tags = ['+DMG', 'Noble', 'Shock']
    image_path = imgs_dir + 'psalm_the_poet.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class queen_aelide:
    name = 'Queen Aelide'
    guild = 'Avalonians'
    class_ = 'Priest'
    strength = '120'
    race = 'Human'
    tags = ['+STR', 'Crit', 'Heal', 'Noble', 'Purify', 'Smite', 'Buffer']
    image_path = imgs_dir + 'queen_aelide.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class saethwir:
    name = 'Saethwir'
    guild = 'Avalonians'
    class_ = 'Marauder'
    race = 'Undead'
    strength = '155'
    tags = ['Dodge', 'Life Drain', 'Noble', 'Backstab']
    image_path = imgs_dir + 'saethwir.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sevylath:
    name = 'Sevylath'
    guild = 'Avalonians'
    class_ = 'Priest'
    race = 'Human'
    strength = '150'
    tags = ['+STR', 'Blessing', 'Noble', 'Shock', 'Smite']
    image_path = imgs_dir + 'sevylath.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sorcerer_erein_ex:
    name = 'Sorcerer Erein Ex'
    guild = 'Avalonians'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['Brave', 'Lightning']
    image_path = imgs_dir + 'sorcerer_erein_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class thunder_king:
    name = 'Thunder King'
    guild = 'Avalonians'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '135'
    tags = ['Brave', 'Lightning']
    image_path = imgs_dir + 'thunder_king.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ysild:
    name = 'Ysild'
    guild = 'Avalonians'
    class_ = 'Warrior'
    race = 'Human'
    strength = '110'
    tags = ['+STR', 'Brave', 'Lightning']
    image_path = imgs_dir + 'ysild.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class aleshane:
    name = 'Aleshane'
    guild = 'Sap Hearts'
    class_ = 'Marauder'
    race = 'Elfine'
    strength = '155'
    tags = ['+STR', 'Thorn', 'Backstab']
    image_path = imgs_dir + 'aleshane.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class apagori:
    name = 'Apagori'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = "Hom'Chai"
    strength = '120'
    tags = ['+STR', 'Shield']
    image_path = imgs_dir + 'apagori.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class arakna:
    name = 'Arakna'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = 'Undead'
    strength = '110'
    tags = ['+DMG', 'Dodge', 'Life Drain', 'Shock']
    image_path = imgs_dir + 'arakna.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class baligu_diga_ex:
    name = "Baligu'Diga Ex"
    guild = 'Sap Hearts'
    class_ = 'Marauder'
    race = 'Undead'
    strength = '150'
    tags = ['Rage', 'Dodge', 'Life Drain', 'Shock', 'Strength Drain']
    image_path = imgs_dir + 'baligu_diga_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class bearcupine:
    name = 'Bearcupine'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '130'
    tags = ['+STR', 'Thorn']
    image_path = imgs_dir + 'bearcupine.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class belladone:
    name = 'Belladone'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Elfine'
    strength = '130'
    tags = ['+DMG', 'Thorn', 'Crit']
    image_path = imgs_dir + 'belladone.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class beltania_ex:
    name = 'Beltania Ex'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = 'Dais'
    strength = '100'
    tags = ['Thorn', 'Heal', 'Spellbreaker']
    image_path = imgs_dir + 'beltania_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class bulu_baga_ex:
    name = "Bulu'Baga Ex"
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = 'Undead'
    strength = '100'
    tags = ['Life Drain', 'Fireball', 'Strength Drain']
    image_path = imgs_dir + 'bulu_baga_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class camo_sv:
    name = 'Camo Sv'
    guild = 'Sap Hearts'
    class_ = 'Colossus'
    race = 'Unknown(R)'
    strength = '250'
    tags = ['Thorn']
    image_path = imgs_dir + 'camo_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class cervus:
    name = 'Cervus'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Dais'
    strength = '130'
    tags = ['Thorn', 'Crit', 'Heal']
    image_path = imgs_dir + 'cervus.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class chestnut:
    name = 'Chestnut'
    guild = 'Sap Hearts'
    class_ = 'Marauder'
    race = 'Elfine'
    strength = '165'
    tags = ['+STR', 'Dodge', 'Shock']
    image_path = imgs_dir + 'chestnut.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class dandy:
    name = 'Dandy'
    guild = 'Sap Hearts'
    class_ = 'Priest'
    race = 'Elfine'
    strength = '130'
    tags = ['+STR', 'Heal', 'Purify', 'Shock']
    image_path = imgs_dir + 'dandy.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class dionaea:
    name = 'Dionaea'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Dais'
    strength = '130'
    tags = ['Thorn', 'Heal']
    image_path = imgs_dir + 'dionaea.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ebony_ex:
    name = 'Ebony Ex'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = 'Dais'
    strength = '100'
    tags = ['+STR', 'Heal', 'Fireball']
    image_path = imgs_dir + 'ebony_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class eikytan_ex:
    name = 'Eikytan Ex'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = 'Dais'
    strength = '90'
    tags = ['Thorn', 'Frostbite', 'Heal', 'Ice']
    image_path = imgs_dir + 'eikytan_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class elder_mailandar_ex:
    name = 'Elder Mailandar Ex'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = "Hom'Chai"
    strength = '120'
    tags = ['Rage', 'Spellbreaker']
    image_path = imgs_dir + 'elder_mailandar_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class elteris_ex:
    name = 'Elteris Ex'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Dais'
    strength = '130'
    tags = ['+STR', 'Thorn', 'Heal']
    image_path = imgs_dir + 'elteris_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class eskar_ex:
    name = 'Eskar Ex'
    guild = 'Sap Hearts'
    class_ = 'Bard'
    race = "Hom'Chai"
    strength = '0'
    tags = ['Shield', 'Heal']
    image_path = imgs_dir + 'eskar_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class fe_y_ex:
    name = "Fe'y Ex"
    guild = 'Sap Hearts'
    class_ = 'Mage'
    strength = '135'
    race = 'Dais'
    tags = ['Death Stare', 'Fireball', 'Heal']
    image_path = imgs_dir + 'fe_y_ex.png'
    turns_texts = ['RRY:  Fireball 2000 & Heal 2000', 'RB:  Hit 750 x R & opp STR / 2', 'R:  Death Stare 250 x R']
    turn1_d = {'cost': 'RRY', 'fp': {'number': 1, 'ability': 'Fireball', 'value': 2000, 'sign': None}, 'sp': {'number': 1, 'ability': 'Heal', 'value': 2000, 'sign': None}}
    turn2_d = {'cost': 'RB', 'fp': {'number': 1, 'ability': 'Hit', 'value': 750, 'mult_opp': False, 'mult': 'R', 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': True, 'allspec': ''}, 'ability': 'STR', 'operator': '/', 'value': 2, 'sign': None}}
    turn3_d = {'cost': 'R', 'fp': {'number': 1, 'ability': 'Death Stare', 'value': 250, 'mult_opp': False, 'mult': 'R', 'sign': None}, 'sp': None}

class gaal_ex:
    name = 'Gaal Ex'
    guild = 'Sap Hearts'
    class_ = 'Bard'
    race = "Hom'Chai"
    strength = '0'
    tags = ['+DMG', 'Thorn']
    image_path = imgs_dir + 'gaal_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class gaya:
    name = 'Gaya'
    guild = 'Sap Hearts'
    class_ = 'Priest'
    race = 'Elfine'
    strength = '90'
    tags = ['Thorn', 'Heal', 'Shock', 'Smite']
    image_path = imgs_dir + 'gaya.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class grand_deer_ex:
    name = 'Grand Deer Ex'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = 'Beast'
    strength = '10'
    tags = ['Heal', 'Blessing']
    image_path = imgs_dir + 'grand_deer_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class grandao_ex:
    name = 'Grandao Ex'
    guild = 'Sap Hearts'
    class_ = 'Marauder'
    race = "Hom'Chai"
    strength = '150'
    tags = ['Rage', 'Dodge', 'Crit']
    image_path = imgs_dir + 'grandao_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class hundawa_ex:
    name = 'Hundawa Ex'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '120'
    tags = ['Thorn', 'Heal']
    image_path = imgs_dir + 'hundawa_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kabra_kan_ex:
    name = "Kabra'Kan Ex"
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = "Hom'Chai"
    strength = '130'
    tags = ['Shield']
    image_path = imgs_dir + 'kabra_kan_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kachu_taoa_sv:
    name = "Kachu'Taoa Sv"
    guild = 'Sap Hearts'
    class_ = 'Colossus'
    race = 'Beast'
    strength = '200'
    tags = ['Thorn', 'Heal']
    image_path = imgs_dir + 'kachu_taoa_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class katla_ex:
    name = 'Katla Ex'
    guild = 'Sap Hearts'
    class_ = 'Marauder'
    race = 'Elfine'
    strength = '155'
    tags = ['+STR', 'Shock']
    image_path = imgs_dir + 'katla_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class keep_the_totems_ex:
    name = 'Keep-the-totems Ex'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = "Hom'Chai"
    strength = '150'
    tags = ['+DMG', '+STR', 'Heal', 'Smite']
    image_path = imgs_dir + 'keep_the_totems_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kei_zan:
    name = "Kei'zan"
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = 'Dais'
    strength = '75'
    tags = ['+STR', 'Heal', 'Fireball']
    image_path = imgs_dir + 'kei_zan.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class koria_ex:
    name = 'Koria Ex'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = 'Beast'
    strength = '90'
    tags = ['Thorn', 'Shield', 'Heal', 'Fireball']
    image_path = imgs_dir + 'koria_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kyr_ieden:
    name = "Kyr'ieden"
    guild = 'Sap Hearts'
    class_ = 'Marauder'
    race = 'Dais'
    strength = '160'
    tags = ['Thorn', 'Heal']
    image_path = imgs_dir + 'kyr_ieden.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lafresnaya_ex:
    name = 'Lafresnaya Ex'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '120'
    tags = ['+STR', 'Thorn', 'Shield']
    image_path = imgs_dir + 'lafresnaya_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class loremie:
    name = 'Loremie'
    guild = 'Sap Hearts'
    class_ = 'Bard'
    race = 'Elfine'
    strength = '0'
    tags = ['Dodge', 'Heal']
    image_path = imgs_dir + 'loremie.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class manascale_ex:
    name = 'Manascale Ex'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    strength = '125'
    race = 'Beast'
    tags = ['+DMG', 'Fireball', 'Heal', 'Spellbreaker', 'Thorn']
    image_path = imgs_dir + 'manascale_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class matoskah_ex:
    name = 'Matoskah Ex'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    strength = '120'
    race = "Hom'Chai"
    tags = ['+STR', 'Crit']
    image_path = imgs_dir + 'matoskah_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class melissandre:
    name = 'Melissandre'
    guild = 'Sap Hearts'
    class_ = 'Marauder'
    strength = '175'
    race = 'Elfine'
    tags = ['Dodge', 'Rage', 'Buffer']
    image_path = imgs_dir + 'melissandre.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class moarg:
    name = 'Moarg'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = "Hom'Chai"
    strength = '120'
    tags = ['+STR', 'Crit', 'Shock']
    image_path = imgs_dir + 'moarg.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mush_ex:
    name = 'Mush Ex'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '130'
    tags = ['+STR', 'Dodge', 'Shock', 'Spellbreaker']
    image_path = imgs_dir + 'mush_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class nahima:
    name = 'Nahima'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = 'Elfine'
    strength = '100'
    tags = ['Heal', 'Spellbreaker', 'Fireball']
    image_path = imgs_dir + 'nahima.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class odonata_ex:
    name = 'Odonata Ex'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Elfine'
    strength = '125'
    tags = ['Shield', 'Scarab']
    image_path = imgs_dir + 'odonata_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class olbat:
    name = 'Olbat'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '120'
    tags = ['Berserk']
    image_path = imgs_dir + 'olbat.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ourenos_ex:
    name = 'Ourenos Ex'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Eltarite'
    strength = '200'
    tags = ['+STR', 'Thorn', 'Rage', 'Heal']
    image_path = imgs_dir + 'ourenos_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class pilferess:
    name = 'Pilferess'
    guild = 'Sap Hearts'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '150'
    tags = ['Crit']
    image_path = imgs_dir + 'pilferess.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class quercus_ex:
    name = 'Quercus Ex'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Dais'
    strength = '120'
    tags = ['+STR', 'Thorn', 'Heal', 'Riposte']
    image_path = imgs_dir + 'quercus_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class rahal_ex:
    name = 'Rahal Ex'
    guild = 'Sap Hearts'
    class_ = 'Berserker'
    race = 'Human'
    strength = '160'
    tags = ['+DMG', '+STR', 'Rage', 'Fireball']
    image_path = imgs_dir + 'rahal_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class rargnor:
    name = 'Rargnor'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = "Hom'Chai"
    strength = '130'
    tags = ['+STR', 'Berserk']
    image_path = imgs_dir + 'rargnor.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class red_mark_ex:
    name = 'Red-Mark Ex'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = "Hom'Chai"
    strength = '90'
    tags = ['Shield', 'Shock']
    image_path = imgs_dir + 'red_mark_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class rockspeaker:
    name = 'Rockspeaker'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = "Hom'Chai"
    strength = '150'
    tags = ['+STR', 'Shield', 'Fireball']
    image_path = imgs_dir + 'rockspeaker.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class row_ya_ex:
    name = "Row'ya Ex"
    guild = 'Sap Hearts'
    class_ = 'Marauder'
    race = 'Dais'
    strength = '150'
    tags = ['+STR', 'Thorn']
    image_path = imgs_dir + 'row_ya_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sanrokl_ex:
    name = 'Sanrokl Ex'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = 'Beast'
    strength = '75'
    tags = ['Fireball', 'Shield', 'Shock']
    image_path = imgs_dir + 'sanrokl_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class saronor:
    name = 'Saronor'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Elfine'
    strength = '130'
    tags = ['Berserk', 'Backstab']
    image_path = imgs_dir + 'saronor.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class shroom_ex:
    name = 'Shroom Ex'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '80'
    tags = ['Crit', 'Shock', 'Fireball', 'Strength Drain']
    image_path = imgs_dir + 'shroom_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class silikat_ex:
    name = 'Silikat Ex'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Elfine'
    strength = '120'
    tags = ['+STR', 'Scarab', 'Shock']
    image_path = imgs_dir + 'silikat_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class spiritspeaker:
    name = 'Spiritspeaker'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = 'Dais'
    strength = '100'
    tags = ['Heal', 'Fireball']
    image_path = imgs_dir + 'spiritspeaker.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class taraxa_ex:
    name = 'Taraxa Ex'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    strength = '100'
    race = 'Dais'
    tags = ['-STR', 'Dodge', 'Heal', 'Shock', 'Thorn']
    image_path = imgs_dir + 'taraxa_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class teheiura:
    name = 'Teheiura'
    guild = 'Sap Hearts'
    class_ = 'Bard'
    race = 'Human'
    strength = '0'
    tags = ['Shield', 'Shock']
    image_path = imgs_dir + 'teheiura.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_burrower:
    name = 'The Burrower'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = "Hom'Chai"
    strength = '120'
    tags = ['+STR', 'Shield']
    image_path = imgs_dir + 'the_burrower.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_claw_ex:
    name = 'The Claw Ex'
    guild = 'Sap Hearts'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '150'
    tags = ['Dodge', 'Shield', 'Shock']
    image_path = imgs_dir + 'the_claw_ex.png'
    turns_texts = ['R:  Shield 150 & Dodge 2', 'Y:  Shock 2 x Shield', 'RRB:  2 x Shock 700']
    turn1_d = {'cost': 'R', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Shield', 'operator': '+', 'value': 150, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Dodge', 'operator': '+', 'value': 2, 'sign': None}}
    turn2_d = {'cost': 'Y', 'fp': {'number': 1, 'ability': 'Shock', 'value': 2, 'mult_opp': False, 'mult': 'Shield', 'sign': None}, 'sp': None}
    turn3_d = {'cost': 'RRB', 'fp': {'number': 2, 'ability': 'Shock', 'value': 700, 'sign': None}, 'sp': None}

class the_hailwalker:
    name = 'The Hailwalker'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Dais'
    strength = '130'
    tags = ['Thorn', 'Rage']
    image_path = imgs_dir + 'the_hailwalker.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_sachem:
    name = 'The Sachem'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = 'Elfine'
    strength = '130'
    tags = ['+STR', 'Shield', 'Heal']
    image_path = imgs_dir + 'the_sachem.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class wreckwood:
    name = 'Wreckwood'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Golem'
    strength = '110'
    tags = ['+STR', 'Thorn', 'Fireball']
    image_path = imgs_dir + 'wreckwood.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class yaz_ex:
    name = 'Yaz Ex'
    guild = 'Sap Hearts'
    class_ = 'Berserker'
    race = "Hom'Chai"
    strength = '150'
    tags = ['Rage', 'Berserk', 'Riposte']
    image_path = imgs_dir + 'yaz_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ydiane:
    name = 'Ydiane'
    guild = 'Sap Hearts'
    class_ = 'Warrior'
    race = 'Elfine'
    strength = '125'
    tags = ['+STR', 'Crit']
    image_path = imgs_dir + 'ydiane.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class yumad:
    name = 'Yumad'
    guild = 'Sap Hearts'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '150'
    tags = ['Death Stare']
    image_path = imgs_dir + 'yumad.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class akujin_ex:
    name = 'Akujin Ex'
    guild = 'Kotobas'
    class_ = 'Marauder'
    strength = '100'
    race = 'Guemelite'
    tags = ['+STR', 'Berserk']
    image_path = imgs_dir + 'akujin_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class amaya_ex:
    name = 'Amaya Ex'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Human'
    strength = '140'
    tags = ['+STR', 'Dodge', 'Shock', 'Backstab']
    image_path = imgs_dir + 'amaya_ex.png'
    turns_texts = ['RRR:  Backstab 1200 & Dodge 2', 'Y:  Shock 1000 x Dodge', 'B:  STR +500 & R->S']
    turn1_d = {'cost': 'RRR', 'fp': {'number': 1, 'ability': 'Backstab', 'value': 1200, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Dodge', 'operator': '+', 'value': 2, 'sign': None}}
    turn2_d = {'cost': 'Y', 'fp': {'number': 1, 'ability': 'Shock', 'value': 1000, 'mult_opp': False, 'mult': 'Dodge', 'sign': None}, 'sp': None}
    turn3_d = {'cost': 'B', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'STR', 'operator': '+', 'value': 500, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'R->S', 'value': 1, 'sign': None}}

class asajiro_the_vagabond:
    name = 'Asajiro the vagabond'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Shield']
    image_path = imgs_dir + 'asajiro_the_vagabond.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ayako_ex:
    name = 'Ayako Ex'
    guild = 'Kotobas'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '110'
    tags = ['+STR', 'Shield', 'Ice']
    image_path = imgs_dir + 'ayako_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ban_kuan:
    name = 'Ban Kuan'
    guild = 'Kotobas'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['+STR', 'Heal', 'Spellbreaker', 'Fireball']
    image_path = imgs_dir + 'ban_kuan.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class chawsane_ex:
    name = 'Chawsane Ex'
    guild = 'Kotobas'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['Shield', 'Shock', 'Fireball']
    image_path = imgs_dir + 'chawsane_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class chidori:
    name = 'Chidori'
    guild = 'Kotobas'
    class_ = 'Marauder'
    strength = '150'
    race = 'Guemelite'
    tags = ['+STR', 'Backstab', 'Dodge', 'Shock', 'Buffer']
    image_path = imgs_dir + 'chidori.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class dabhu_ex:
    name = 'Dabhu Ex'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '125'
    tags = ['+STR', 'Shield']
    image_path = imgs_dir + 'dabhu_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class daijin_the_crow_ex:
    name = 'Daijin the Crow Ex'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Undead'
    strength = '170'
    tags = ['+STR', 'Dodge', 'Life Drain', 'Shock', 'Backstab']
    image_path = imgs_dir + 'daijin_the_crow_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class dakeza:
    name = 'Dakeza'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '150'
    tags = ['+STR', 'Dodge', 'Crit', 'Shock']
    image_path = imgs_dir + 'dakeza.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class fu_long_sv:
    name = 'Fu-Long Sv'
    guild = 'Kotobas'
    class_ = 'Colossus'
    strength = '200'
    race = 'Dragon'
    tags = ['+STR', 'Fireball', 'Shield']
    image_path = imgs_dir + 'fu_long_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class furagu:
    name = 'Furagu'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['Shield']
    image_path = imgs_dir + 'furagu.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class gakyusha:
    name = 'Gakyusha'
    guild = 'Kotobas'
    class_ = 'Warrior'
    strength = '130'
    race = 'Human'
    tags = ['+STR', 'Riposte', 'Buffer']
    image_path = imgs_dir + 'gakyusha.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class gan_so:
    name = "Gan'So"
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Undead'
    strength = '125'
    tags = ['+STR', 'Shock', 'Strength Drain']
    image_path = imgs_dir + 'gan_so.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class hime:
    name = 'Hime'
    guild = 'Kotobas'
    class_ = 'Marauder'
    strength = '150'
    race = 'Human'
    tags = ['+DMG', 'Crit', 'Dodge', 'Buffer']
    image_path = imgs_dir + 'hime.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class hisomu:
    name = 'Hisomu'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '160'
    tags = ['Dodge', 'Shock', 'Backstab']
    image_path = imgs_dir + 'hisomu.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ijin_shisei_ex:
    name = 'Ijin Shisei Ex'
    guild = 'Kotobas'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['+STR', 'Dodge', 'Fireball']
    image_path = imgs_dir + 'ijin_shisei_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class iro_the_champion_ex:
    name = 'Iro the Champion Ex'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Shield', 'Shock', 'Spellbreaker']
    image_path = imgs_dir + 'iro_the_champion_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class iro_the_duelist_ex:
    name = 'Iro the Duelist Ex'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Human'
    strength = '70'
    tags = ['+STR', 'Shield']
    image_path = imgs_dir + 'iro_the_duelist_ex.png'
    turns_texts = ['RB:  Shield 500 & Hit 500', 'BY:  all +STR = STR', 'Y:  STR +500 & 2 R->S']
    turn1_d = {'cost': 'RB', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Shield', 'operator': '+', 'value': 500, 'sign': None}, 'sp': {'number': 1, 'ability': 'Hit', 'value': 500, 'sign': None}}
    turn2_d = {'cost': 'BY', 'fp': {'number': 1, 'target': {'all': True, 'opp': False, 'allspec': ''}, 'ability': 'STR', 'operator': '+', 'value': 1, 'mult_opp': False, 'mult': 'STR', 'sign': None}, 'sp': None}
    turn3_d = {'cost': 'Y', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'STR', 'operator': '+', 'value': 500, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'R->S', 'value': 2, 'sign': None}}

class jian_qiao:
    name = 'Jian Qiao'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['+STR', 'Dodge', 'Riposte']
    image_path = imgs_dir + 'jian_qiao.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class jubey:
    name = 'Jubey'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '150'
    tags = ['+DMG', 'Shock']
    image_path = imgs_dir + 'jubey.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class karasu_kage_ex:
    name = 'Karasu Kage Ex'
    guild = 'Kotobas'
    class_ = 'Marauder'
    strength = '150'
    race = 'Human'
    tags = ['+STR', 'Backstab', 'Dodge', 'Shock']
    image_path = imgs_dir + 'karasu_kage_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kasai_ex:
    name = 'Kasai Ex'
    guild = 'Kotobas'
    class_ = 'Warrior'
    strength = '130'
    race = 'Human'
    tags = ['+DMG', '+STR', 'Dodge', 'Fireball']
    image_path = imgs_dir + 'kasai_ex.png'
    turns_texts = ['B:  STR +230 & Dodge 1', 'RR:  Fireball 5 x STR', 'Y:  DMG +600 & R->S']
    turn1_d = {'cost': 'B', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'STR', 'operator': '+', 'value': 230, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Dodge', 'operator': '+', 'value': 1, 'sign': None}}
    turn2_d = {'cost': 'RR', 'fp': {'number': 1, 'ability': 'Fireball', 'value': 5, 'mult_opp': False, 'mult': 'STR', 'sign': None}, 'sp': None}
    turn3_d = {'cost': 'Y', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': '+DMG', 'operator': ':', 'value': 600, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'R->S', 'value': 1, 'sign': None}}

class kimiko_ex:
    name = 'Kimiko Ex'
    guild = 'Kotobas'
    class_ = 'Bard'
    race = 'Human'
    strength = '0'
    tags = ['Dodge', 'Shield', 'Shock']
    image_path = imgs_dir + 'kimiko_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kitsana_ex:
    name = 'Kitsana Ex'
    guild = 'Kotobas'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['+STR', 'Dodge', 'Shock', 'Fireball']
    image_path = imgs_dir + 'kitsana_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kotori_kage_ex:
    name = 'Kotori Kage Ex'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '150'
    tags = ['Dodge', 'Shock', 'Backstab']
    image_path = imgs_dir + 'kotori_kage_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kuro_kage:
    name = 'Kuro Kage'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '170'
    tags = ['+STR', 'Dodge', 'Shock']
    image_path = imgs_dir + 'kuro_kage.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kyoshiro_ex:
    name = 'Kyoshiro Ex'
    guild = 'Kotobas'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['+STR', 'Spellbreaker', 'Fireball']
    image_path = imgs_dir + 'kyoshiro_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class li_lan:
    name = 'Li Lan'
    guild = 'Kotobas'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['+STR', 'Shield', 'Fireball']
    image_path = imgs_dir + 'li_lan.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class malyss_ex:
    name = 'Malyss Ex'
    guild = 'Kotobas'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['Dodge', 'Shock', 'Fireball']
    image_path = imgs_dir + 'malyss_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class masamune:
    name = 'Masamune'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Human'
    strength = '100'
    tags = ['+DMG', '+STR', 'Riposte']
    image_path = imgs_dir + 'masamune.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class master_ma:
    name = 'Master Ma'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['+STR', 'Shield']
    image_path = imgs_dir + 'master_ma.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class megami_ex:
    name = 'Megami Ex'
    guild = 'Kotobas'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['Crit', 'Shield', 'Heal', 'Fireball']
    image_path = imgs_dir + 'megami_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mei_li:
    name = 'Mei-Li'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Human'
    strength = '140'
    tags = ['+STR']
    image_path = imgs_dir + 'mei_li.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class nashi:
    name = 'Nashi'
    guild = 'Kotobas'
    class_ = 'Mage'
    race = 'Undead'
    strength = '95'
    tags = ['+DMG', 'Life Drain', 'Fireball']
    image_path = imgs_dir + 'nashi.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class nin_zashi_ex:
    name = 'Nin Zashi Ex'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '125'
    tags = ['+STR', 'Spellbreaker', 'Fireball']
    image_path = imgs_dir + 'nin_zashi_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class odaiko:
    name = 'Odaiko'
    guild = 'Kotobas'
    class_ = 'Bard'
    race = 'Guemelite'
    strength = '0'
    tags = ['Shield']
    image_path = imgs_dir + 'odaiko.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class okooni:
    name = 'Okooni'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '130'
    tags = ['+STR', 'Shock']
    image_path = imgs_dir + 'okooni.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class oogoe_kage:
    name = 'Oogoe Kage'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Human'
    strength = '70'
    tags = ['Dodge', 'Shock', 'Terror']
    image_path = imgs_dir + 'oogoe_kage.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class popoki_ex:
    name = 'Popoki Ex'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '170'
    tags = ['Crit']
    image_path = imgs_dir + 'popoki_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ramen_ex:
    name = 'Ramen Ex'
    guild = 'Kotobas'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['Shield', 'Heal', 'Fireball']
    image_path = imgs_dir + 'ramen_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ryouken:
    name = 'Ryouken'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '150'
    tags = ['+STR', 'Shield', 'Shock', 'Fireball']
    image_path = imgs_dir + 'ryouken.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class samurai_asajiro_ex:
    name = 'Samurai Asajiro Ex'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['Shock', 'Spellbreaker', 'Riposte']
    image_path = imgs_dir + 'samurai_asajiro_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class satsume_ex:
    name = 'Satsume Ex'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Humanh'
    strength = '160'
    tags = ['+STR', 'Crit', 'Backstab']
    image_path = imgs_dir + 'satsume_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sen_ryaku_ex:
    name = "Sen'Ryaku Ex"
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Shock', 'Riposte']
    image_path = imgs_dir + 'sen_ryaku_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class shengdi_ex:
    name = 'Shengdi Ex'
    guild = 'Kotobas'
    class_ = 'Marauder'
    strength = '165'
    race = 'Human'
    tags = ['+DMG', 'Backstab', 'Dodge']
    image_path = imgs_dir + 'shengdi_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class shi_sv:
    name = 'Shi Sv'
    guild = 'Kotobas'
    class_ = 'Colossus'
    race = 'Unknown(R)'
    strength = '300'
    tags = ['Fireball']
    image_path = imgs_dir + 'shi_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class shori_ex:
    name = 'Shori Ex'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Human'
    strength = '125'
    tags = ['+STR', 'Shield']
    image_path = imgs_dir + 'shori_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class shui_khan_ex:
    name = 'Shui Khan Ex'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '150'
    tags = ['+STR', 'Dodge']
    image_path = imgs_dir + 'shui_khan_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sinfire_ex:
    name = 'Sinfire Ex'
    guild = 'Kotobas'
    class_ = 'Berserker'
    strength = '150'
    race = 'Beast'
    tags = ['+STR', 'Dodge', 'Fireball', 'Shock']
    image_path = imgs_dir + 'sinfire_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class soeko_ex:
    name = 'Soeko Ex'
    guild = 'Kotobas'
    class_ = 'Mage'
    race = 'Dais '
    strength = '110'
    tags = ['+STR', 'Thorn', 'Heal', 'Fireball']
    image_path = imgs_dir + 'soeko_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sun_tsu_ex:
    name = 'Sun Tsu Ex'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['Riposte']
    image_path = imgs_dir + 'sun_tsu_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class tessai_ex:
    name = 'Tessai Ex'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Shield', 'Riposte']
    image_path = imgs_dir + 'tessai_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class toran_the_regent:
    name = 'Toran the Regent'
    guild = 'Kotobas'
    class_ = 'Mage'
    race = 'Human'
    strength = '120'
    tags = ['Rage', 'Shock', 'Fireball']
    image_path = imgs_dir + 'toran_the_regent.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class tsuro:
    name = 'Tsuro'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['+DMG', 'Spellbreaker']
    image_path = imgs_dir + 'tsuro.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class uinata_ex:
    name = 'Uinata Ex'
    guild = 'Kotobas'
    class_ = 'Marauder'
    strength = '150'
    race = 'Human'
    tags = ['+STR', 'Dodge', 'Frostbite', 'Ice']
    image_path = imgs_dir + 'uinata_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class wing_chun_ex:
    name = 'Wing Chun Ex'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '150'
    tags = ['Dodge', 'Shield', 'Shock']
    image_path = imgs_dir + 'wing_chun_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class xianren_ex:
    name = 'Xianren Ex'
    guild = 'Kotobas'
    class_ = 'Mage'
    race = 'Beast'
    strength = '130'
    tags = ['+STR', 'Fireball']
    image_path = imgs_dir + 'xianren_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class xin_ex:
    name = 'Xin Ex'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Human'
    strength = '100'
    tags = ['+STR', 'Shield', 'Shock', 'Stench']
    image_path = imgs_dir + 'xin_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class yakiba_qiao:
    name = 'Yakiba Qiao'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Human'
    strength = '125'
    tags = ['Dodge']
    image_path = imgs_dir + 'yakiba_qiao.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class yu_ling:
    name = 'Yu Ling'
    guild = 'Kotobas'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['Heal', 'Shock', 'Fireball']
    image_path = imgs_dir + 'yu_ling.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class zatochi_kage_ex:
    name = 'Zatochi Kage Ex'
    guild = 'Kotobas'
    class_ = 'Warrior'
    race = 'Undead'
    strength = '120'
    tags = ['Life Drain', 'Death Stare', 'Strength Drain']
    image_path = imgs_dir + 'zatochi_kage_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ziya_ex:
    name = 'Ziya Ex'
    guild = 'Kotobas'
    class_ = 'Mage'
    strength = '90'
    race = 'Guemelite'
    tags = ['+DMG', '+STR', 'Fireball', 'Heal', 'Smite']
    image_path = imgs_dir + 'ziya_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class atkanda_ex:
    name = 'Atkanda Ex'
    guild = 'Winter Tribes'
    class_ = 'Mage'
    race = 'Ice Elf'
    strength = '100'
    tags = ['Blizzard', 'Frostbite', 'Spellbreaker', 'Ice']
    image_path = imgs_dir + 'atkanda_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ayir:
    name = 'Ayir'
    guild = 'Winter Tribes'
    class_ = 'Berserker'
    race = 'Ice Elf'
    strength = '150'
    tags = ['Berserk', 'Dodge', 'Ice']
    image_path = imgs_dir + 'ayir.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class comet_ex:
    name = 'Comet Ex'
    guild = 'Winter Tribes'
    class_ = 'Mage'
    race = 'Beast'
    strength = '90'
    tags = ['Frostbite', 'Heal', 'Shock', 'Ice']
    image_path = imgs_dir + 'comet_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class crystocat:
    name = 'Crystocat'
    guild = 'Winter Tribes'
    class_ = 'Berserker'
    race = 'Beast'
    strength = '150'
    tags = ['+STR', 'Dodge', 'Frostbite', 'Ice']
    image_path = imgs_dir + 'crystocat.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class cygnaea_ex:
    name = 'Cygnaea Ex'
    guild = 'Winter Tribes'
    class_ = 'Bard'
    race = 'Ice Elf'
    strength = '0'
    tags = ['Ice', 'Shock']
    image_path = imgs_dir + 'cygnaea_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class fyrnir_the_ancient_ex:
    name = 'Fyrnir the ancient Ex'
    guild = 'Winter Tribes'
    class_ = 'Berserker'
    race = 'Ice Elf'
    strength = '150'
    tags = ['+STR', 'Ice', 'Frostbite']
    image_path = imgs_dir + 'fyrnir_the_ancient_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class king_hrimnir:
    name = 'King Hrimnir'
    guild = 'Winter Tribes'
    class_ = 'Berserker'
    strength = '170'
    race = 'Undead'
    tags = ['Ice', 'Stench']
    image_path = imgs_dir + 'king_hrimnir.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kokrem:
    name = 'Kokrem'
    guild = 'Winter Tribes'
    class_ = 'Berserker'
    strength = '140'
    race = 'Ice Elf'
    tags = ['+STR', 'Blizzard', 'Frostbite', 'Ice', 'Buffer']
    image_path = imgs_dir + 'kokrem.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lady_beenle:
    name = 'Lady Beenle'
    guild = 'Winter Tribes'
    class_ = 'Priest'
    race = 'Ice Elf'
    strength = '125'
    tags = ['Dodge', 'Shield', 'Shock', 'Smite', 'Ice']
    image_path = imgs_dir + 'lady_beenle.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lady_yilith:
    name = 'Lady Yilith'
    guild = 'Winter Tribes'
    class_ = 'Priest'
    race = 'Ice Elf'
    strength = '135'
    tags = ['Heal', 'Blessing', 'Purify', 'Shock', 'Ice']
    image_path = imgs_dir + 'lady_yilith.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class laelyse:
    name = 'Laelyse'
    guild = 'Winter Tribes'
    class_ = 'Mage'
    race = 'Ice Elf'
    strength = '110'
    tags = ['Heal', 'Shock', 'Spellbreaker', 'Ice']
    image_path = imgs_dir + 'laelyse.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mad_claus_ex:
    name = 'Mad Claus Ex'
    guild = 'Winter Tribes'
    class_ = 'Berserker'
    race = 'Human'
    strength = '200'
    tags = ['+STR', 'Shock']
    image_path = imgs_dir + 'mad_claus_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class meh_teh_sv:
    name = 'Meh-Teh Sv'
    guild = 'Winter Tribes'
    class_ = 'Colossus'
    race = 'Unknown(R)'
    strength = '280'
    tags = ['+STR', 'Ice']
    image_path = imgs_dir + 'meh_teh_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class prancer_ex:
    name = 'Prancer Ex'
    guild = 'Winter Tribes'
    class_ = 'Priest'
    race = 'Beast'
    strength = '105'
    tags = ['Blizzard', 'Purify', 'Smite', 'Ice']
    image_path = imgs_dir + 'prancer_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class rudolf_ex:
    name = 'Rudolf Ex'
    guild = 'Winter Tribes'
    class_ = 'Berserker'
    race = 'Beast'
    strength = '150'
    tags = ['Rage', 'Frostbite', 'Ice']
    image_path = imgs_dir + 'rudolf_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class santa_ex:
    name = 'Santa Ex'
    guild = 'Winter Tribes'
    class_ = 'Berserker'
    race = 'Human'
    strength = '150'
    tags = ['+STR', 'Dodge', 'Ice']
    image_path = imgs_dir + 'santa_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class shulong_sv:
    name = 'Shulong Sv'
    guild = 'Winter Tribes'
    class_ = 'Colossus'
    race = 'Guemelite'
    strength = '200'
    tags = ['+STR', 'Dodge', 'Shock', 'Lightning', 'Ice']
    image_path = imgs_dir + 'shulong_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class skelfrost_ex:
    name = 'Skelfrost Ex'
    guild = 'Winter Tribes'
    class_ = 'Berserker'
    race = 'Undead'
    strength = '170'
    tags = ['+STR', 'Life Drain', 'Death Stare', 'Ice']
    image_path = imgs_dir + 'skelfrost_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ursyd:
    name = 'Ursyd'
    guild = 'Winter Tribes'
    class_ = 'Berserker'
    strength = '150'
    race = 'Ice Elf'
    tags = ['Berserk', 'Ice', 'Rage', 'Buffer']
    image_path = imgs_dir + 'ursyd.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class vixen_ex:
    name = 'Vixen Ex'
    guild = 'Winter Tribes'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '150'
    tags = ['+STR', 'Crit', 'Shock', 'Ice']
    image_path = imgs_dir + 'vixen_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class xineohp_ex:
    name = 'Xineohp Ex'
    guild = 'Winter Tribes'
    class_ = 'Berserker'
    race = 'Beast'
    strength = '150'
    tags = ['+DMG', 'Berserk', 'Blizzard', 'Shock', 'Ice']
    image_path = imgs_dir + 'xineohp_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class yulven:
    name = 'Yulven'
    guild = 'Winter Tribes'
    class_ = 'Berserker'
    race = 'Icy Elf'
    strength = '150'
    tags = ['Rage', 'Dodge', 'Riposte', 'Ice']
    image_path = imgs_dir + 'yulven.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class adhikara_ex:
    name = 'Adhikara Ex'
    guild = 'Mercenaries'
    class_ = 'Priest'
    race = 'Guemelite'
    strength = '140'
    tags = ['Heal', 'Purify', 'Shock', 'Spellbreaker']
    image_path = imgs_dir + 'adhikara_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class admiral_rabbit_ex:
    name = 'Admiral Rabbit Ex'
    guild = 'Mercenaries'
    class_ = 'Warrior'
    race = 'Golem'
    strength = '50'
    tags = ['+DMG', 'Shock', 'Spellbreaker']
    image_path = imgs_dir + 'admiral_rabbit_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class akra_ex:
    name = 'Akra Ex'
    guild = 'Mercenaries'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '100'
    tags = ['Death Stare', 'Stench']
    image_path = imgs_dir + 'akra_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class amnezy_ex:
    name = 'Amnezy Ex'
    guild = 'Mercenaries'
    class_ = 'Marauder'
    race = 'Unknown(R)'
    strength = '170'
    tags = ['Dodge', 'Backstab']
    image_path = imgs_dir + 'amnezy_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ateb_ex:
    name = 'Ateb Ex'
    guild = 'Mercenaries'
    class_ = 'Marauder'
    race = 'Undead'
    strength = '150'
    tags = ['Heal', 'Fireball', 'Backstab']
    image_path = imgs_dir + 'ateb_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class chantelain_ex:
    name = 'Chantelain Ex'
    guild = 'Mercenaries'
    class_ = 'Marauder'
    race = 'Unknown(R)'
    strength = '170'
    tags = ['Dodge', 'Backstab', 'Death Stare']
    image_path = imgs_dir + 'chantelain_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class cherub_ex:
    name = 'Cherub Ex'
    guild = 'Mercenaries'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['+STR', 'Dodge', 'Shock']
    image_path = imgs_dir + 'cherub_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ciramor:
    name = 'Ciramor'
    guild = 'Mercenaries'
    class_ = 'Priest'
    race = 'Unknown(R)'
    strength = '115'
    tags = ['Berserk', 'Shock', 'Fireball', '-DMG']
    image_path = imgs_dir + 'ciramor.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class cornan:
    name = 'Cornan'
    guild = 'Mercenaries'
    class_ = 'Berserker'
    race = 'Guemelite'
    strength = '140'
    tags = ['Berserk', 'Heal']
    image_path = imgs_dir + 'cornan.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class councillor_ishaia:
    name = 'Councillor Ishaia'
    guild = 'Mercenaries'
    class_ = 'Mage'
    strength = '100'
    race = 'Human'
    tags = ['+DMG', '+STR', 'Blessing', 'Shock', 'Buffer']
    image_path = imgs_dir + 'councillor_ishaia.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class doyen_verace:
    name = 'Doyen Verace'
    guild = 'Mercenaries'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['Resil', 'Dodge', 'Heal', 'Lightning', 'Fireball']
    image_path = imgs_dir + 'doyen_verace.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class dumpty_ex:
    name = 'Dumpty Ex'
    guild = 'Mercenaries'
    class_ = 'Berserker'
    race = 'Golem'
    strength = '50'
    tags = ['Death Stare', 'Stench']
    image_path = imgs_dir + 'dumpty_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class elhoradana_ex:
    name = 'Elhoradana Ex'
    guild = 'Mercenaries'
    class_ = 'Mage'
    race = 'Unknown(R)'
    strength = '80'
    tags = ['Dodge', 'Shield', 'Purify', 'Shock', 'Spellbreaker']
    image_path = imgs_dir + 'elhoradana_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class farookh:
    name = 'Farookh'
    guild = 'Mercenaries'
    class_ = 'Bard'
    race = 'Human'
    strength = '0'
    tags = ['Shield', 'Stench']
    image_path = imgs_dir + 'farookh.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class fog_hydra_sv:
    name = 'Fog Hydra Sv'
    guild = 'Mercenaries'
    class_ = 'Colossus'
    race = 'Undead'
    strength = '175'
    tags = ['+STR', 'Dodge', 'Life Drain', 'Shock']
    image_path = imgs_dir + 'fog_hydra_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class galmi_sv:
    name = 'Galmi Sv'
    guild = 'Mercenaries'
    class_ = 'Colossus'
    race = 'Unknown(R)'
    strength = '290'
    tags = ['Shield', 'Shock']
    image_path = imgs_dir + 'galmi_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class gou_ex:
    name = 'Gou Ex'
    guild = 'Mercenaries'
    class_ = 'Bard'
    race = 'Beast'
    strength = '0'
    tags = ['Shield', 'Spellbreaker']
    image_path = imgs_dir + 'gou_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class jack_al_azred_ex:
    name = "Jack Al'Azred Ex"
    guild = 'Mercenaries'
    class_ = 'Mage'
    race = 'Undead'
    strength = '125'
    tags = ['+DMG', 'Life Drain', 'Shock', 'Terror']
    image_path = imgs_dir + 'jack_al_azred_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class jayane:
    name = 'Jayane'
    guild = 'Mercenaries'
    class_ = 'Mage'
    race = 'Human'
    strength = '80'
    tags = ['Crit', 'Heal']
    image_path = imgs_dir + 'jayane.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kup_id_ex:
    name = "Kup'id Ex"
    guild = 'Mercenaries'
    class_ = 'Priest'
    race = 'Solarian'
    strength = '185'
    tags = ['Blessing', 'Shock', 'Death Stare']
    image_path = imgs_dir + 'kup_id_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lana_ex:
    name = 'Lana Ex'
    guild = 'Mercenaries'
    class_ = 'Berserker'
    race = 'Human'
    strength = '150'
    tags = ['+DMG', 'Crit', 'Shock']
    image_path = imgs_dir + 'lana_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lord_xeneelk:
    name = 'Lord Xeneelk'
    guild = 'Mercenaries'
    class_ = 'Unknown(C)'
    race = 'Unknown(R)'
    strength = '0'
    tags = ['+DMG', 'Shield', 'Shock', 'Spellbreaker']
    image_path = imgs_dir + 'lord_xeneelk.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lucyan_ex:
    name = 'Lucyan Ex'
    guild = 'Mercenaries'
    class_ = 'Unknown(C)'
    strength = '150'
    race = 'Human'
    tags = ['+DMG', 'Fireball', 'Spellbreaker']
    image_path = imgs_dir + 'lucyan_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class master_mystic_slayer:
    name = 'Master Mystic-Slayer'
    guild = 'Mercenaries'
    class_ = 'Marauder'
    race = 'Unknown(R)'
    strength = '170'
    tags = ['Shock']
    image_path = imgs_dir + 'master_mystic_slayer.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class noth:
    name = 'Noth'
    guild = 'Mercenaries'
    class_ = 'Berserker'
    strength = '140'
    race = 'Beast'
    tags = ['+DMG', 'Backstab', 'Dodge']
    image_path = imgs_dir + 'noth.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class quilingo_ex:
    name = 'Quilingo Ex'
    guild = 'Mercenaries'
    class_ = 'Warrior'
    strength = '120'
    race = 'Beast'
    tags = ['+STR', 'Shield', 'Shock']
    image_path = imgs_dir + 'quilingo_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class roaster_ex:
    name = 'Roaster Ex'
    guild = 'Mercenaries'
    class_ = 'Berserker'
    race = 'Beast'
    strength = '170'
    tags = ['Fireball']
    image_path = imgs_dir + 'roaster_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class scarlet:
    name = 'Scarlet'
    guild = 'Mercenaries'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '125'
    tags = ['+STR', 'Riposte']
    image_path = imgs_dir + 'scarlet.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class shana:
    name = 'Shana'
    guild = 'Mercenaries'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['+STR']
    image_path = imgs_dir + 'shana.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class stone_king_ex:
    name = 'Stone King Ex'
    guild = 'Mercenaries'
    class_ = 'Warrior'
    race = 'Unknown(R)'
    strength = '125'
    tags = ['Resil', 'Shield']
    image_path = imgs_dir + 'stone_king_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class stoneeater:
    name = 'StoneEater'
    guild = 'Mercenaries'
    class_ = 'Priest'
    race = 'Guemelite'
    strength = '125'
    tags = ['Shield', 'Spellbreaker', 'Smite']
    image_path = imgs_dir + 'stoneeater.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_champion_ex:
    name = 'The Champion Ex'
    guild = 'Mercenaries'
    class_ = 'Warrior'
    race = 'Human'
    strength = '160'
    tags = ['Dodge', 'Shield']
    image_path = imgs_dir + 'the_champion_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_phoenix:
    name = 'The Phoenix'
    guild = 'Mercenaries'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '150'
    tags = ['Blessing', 'Fireball']
    image_path = imgs_dir + 'the_phoenix.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_stranger_ex:
    name = 'The Stranger Ex'
    guild = 'Mercenaries'
    class_ = 'Warrior'
    race = 'Unknown(R)'
    strength = '0'
    tags = ['+STR', 'Resil', 'Shock']
    image_path = imgs_dir + 'the_stranger_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class toran_the_godless:
    name = 'Toran the Godless'
    guild = 'Mercenaries'
    class_ = 'Mage'
    race = 'Human'
    strength = '120'
    tags = ['Rage', 'Shield', 'Shock']
    image_path = imgs_dir + 'toran_the_godless.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class trauma_ex:
    name = 'Trauma Ex'
    guild = 'Mercenaries'
    class_ = 'Marauder'
    race = 'Unknown(R)'
    strength = '160'
    tags = ['Life Drain', 'Backstab', 'Death Stare', 'Terror']
    image_path = imgs_dir + 'trauma_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class valentyne_ex:
    name = 'Valentyne Ex'
    guild = 'Mercenaries'
    class_ = 'Priest'
    race = 'Human'
    strength = '125'
    tags = ['Shield', 'Blessing', 'Purify']
    image_path = imgs_dir + 'valentyne_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class vile_kinpump_ex:
    name = 'Vile Kinpump Ex'
    guild = 'Mercenaries'
    class_ = 'Unknown(C)'
    race = 'Demon'
    strength = '100'
    tags = ['Thorn', 'Fireball', 'Death Stare', 'Terror']
    image_path = imgs_dir + 'vile_kinpump_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class wayna_ex:
    name = 'Wayna Ex'
    guild = 'Mercenaries'
    class_ = 'Priest'
    race = 'Undead'
    strength = '80'
    tags = ['+DMG', 'Life Drain', 'Death Stare']
    image_path = imgs_dir + 'wayna_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ahkmosis_ex:
    name = 'Ahkmosis Ex'
    guild = 'Desert Nomads'
    class_ = 'Marauder'
    strength = '150'
    race = 'Undead'
    tags = ['Dodge', 'Eclipse', 'Life Drain']
    image_path = imgs_dir + 'ahkmosis_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ahlem:
    name = 'Ahlem'
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Solarian'
    strength = '145'
    tags = ['Resil', 'Blessing', 'Shock', 'Smite']
    image_path = imgs_dir + 'ahlem.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ahzred_ex:
    name = 'Ahzred Ex'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    race = 'Human'
    strength = '125'
    tags = ['Resil', 'Blessing', 'Shock']
    image_path = imgs_dir + 'ahzred_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class akhet_ex:
    name = 'Akhet Ex'
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Solarian'
    strength = '160'
    tags = ['Blessing', 'Purify']
    image_path = imgs_dir + 'akhet_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class aksenoun_ex:
    name = 'Aksenoun Ex'
    guild = 'Desert Nomads'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '170'
    tags = ['Dodge', 'Blessing', 'Backstab']
    image_path = imgs_dir + 'aksenoun_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class amhid:
    name = 'Amhid'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    race = 'Undead'
    strength = '125'
    tags = ['+STR', 'Resil', 'Scarab', 'Life Drain']
    image_path = imgs_dir + 'amhid.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ank_serah_ex:
    name = 'Ank Serah Ex'
    guild = 'Desert Nomads'
    class_ = 'Marauder'
    race = 'Solarian'
    strength = '170'
    tags = ['Spellbreaker', 'Backstab', 'Eclipse']
    image_path = imgs_dir + 'ank_serah_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ankhou:
    name = 'Ankhou'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Resil', 'Riposte']
    image_path = imgs_dir + 'ankhou.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ayept_ex:
    name = 'Ayept Ex'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    race = 'Undead'
    strength = '130'
    tags = ['+STR', 'Resil', 'Dodge', 'Life Drain', 'Spellbreaker']
    image_path = imgs_dir + 'ayept_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class aziz_the_sphinx:
    name = 'Aziz, the Sphinx'
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Solarian'
    strength = '150'
    tags = ['+STR', 'Resil', 'Smite']
    image_path = imgs_dir + 'aziz_the_sphinx.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ba_sthet_ex:
    name = 'Ba-Sthet Ex'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Resil', 'Blessing', 'Shock']
    image_path = imgs_dir + 'ba_sthet_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class bes_sv:
    name = 'Bes Sv'
    guild = 'Desert Nomads'
    class_ = 'Colossus'
    race = 'Unknown(R)'
    strength = '300'
    tags = ['Blessing', 'Shock']
    image_path = imgs_dir + 'bes_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class dahre_ma_sv:
    name = "Dahre'ma Sv"
    guild = 'Desert Nomads'
    class_ = 'Colossus'
    strength = '200'
    race = 'Dragon'
    tags = ['Blessing', 'Fireball', 'Resil', 'Shock', 'Smite']
    image_path = imgs_dir + 'dahre_ma_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class djamena:
    name = 'Djamena'
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Solarian'
    strength = '150'
    tags = ['Blessing', 'Purify', 'Smite']
    image_path = imgs_dir + 'djamena.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class djehutoth_ex:
    name = 'Djehutoth Ex'
    guild = 'Desert Nomads'
    class_ = 'Marauder'
    race = 'Solarian'
    strength = '140'
    tags = ['Resil', 'Blessing', 'Eclipse']
    image_path = imgs_dir + 'djehutoth_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class djeser:
    name = 'Djeser'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    race = 'Golem'
    strength = '125'
    tags = ['Resil']
    image_path = imgs_dir + 'djeser.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class djoha_ex:
    name = 'Djoha Ex'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    race = 'Undead'
    strength = '135'
    tags = ['Life Drain', 'Eclipse', 'Strength Drain']
    image_path = imgs_dir + 'djoha_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class hakim:
    name = 'Hakim'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['+STR', 'Blessing', 'Riposte']
    image_path = imgs_dir + 'hakim.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class hasna_ex:
    name = 'Hasna Ex'
    guild = 'Desert Nomads'
    class_ = 'Marauder'
    race = 'Solarian'
    strength = '140'
    tags = ['Resil', 'Life Drain', 'Shock']
    image_path = imgs_dir + 'hasna_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class hiba_mu:
    name = "Hiba'mu"
    guild = 'Desert Nomads'
    class_ = 'Bard'
    race = 'Solarian'
    strength = '0'
    tags = ['Resil', 'Shock']
    image_path = imgs_dir + 'hiba_mu.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class idriss_ex:
    name = 'Idriss Ex'
    guild = 'Desert Nomads'
    class_ = 'Marauder'
    strength = '150'
    race = 'Human'
    tags = ['+STR', 'Backstab', 'Dodge', 'Eclipse', 'Shock']
    image_path = imgs_dir + 'idriss_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class inatka:
    name = 'Inatka'
    guild = 'Desert Nomads'
    class_ = 'Marauder'
    race = 'human'
    strength = '160'
    tags = ['Dodge', 'Crit', 'Eclipse']
    image_path = imgs_dir + 'inatka.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class iolmarek_ex:
    name = 'Iolmarek Ex'
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Solarian'
    strength = '70'
    tags = ['Shock', 'Fireball', 'Eclipse']
    image_path = imgs_dir + 'iolmarek_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kahlel:
    name = 'Kahlel'
    guild = 'Desert Nomads'
    class_ = 'Marauder'
    race = 'Solarian'
    strength = '175'
    tags = ['Crit', 'Eclipse']
    image_path = imgs_dir + 'kahlel.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kamenwati_ex:
    name = 'Kamenwati Ex'
    guild = 'Desert Nomads'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['+STR', 'Dodge', 'Blessing', 'Eclipse']
    image_path = imgs_dir + 'kamenwati_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kararine_ex:
    name = 'Kararine Ex'
    guild = 'Desert Nomads'
    class_ = 'Marauder'
    race = 'Solarian'
    strength = '150'
    tags = ['Crit', 'Scarab', 'Eclipse']
    image_path = imgs_dir + 'kararine_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kebek:
    name = 'Kebek'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    strength = '120'
    race = 'Beast'
    tags = ['+STR', 'Resil', 'Shield', 'Shock', 'Buffer']
    image_path = imgs_dir + 'kebek.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class khmun_ex:
    name = 'Khmun Ex'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    race = 'Solarian'
    strength = '110'
    tags = ['+STR', 'Resil', 'Scarab']
    image_path = imgs_dir + 'khmun_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kroub_ex:
    name = 'Kroub Ex'
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Solarian'
    strength = '105'
    tags = ['Blessing', 'Shock', 'Smite', 'Eclipse']
    image_path = imgs_dir + 'kroub_ex.png'
    turns_texts = ['RRB:  Hit 1200 & opp Eclipse 2', 'R:  Shock 450 & Blessing 20', 'RY:  Smite Blessing/10']
    turn1_d = {'cost': 'RRB', 'fp': {'number': 1, 'ability': 'Hit', 'value': 1200, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': True, 'allspec': ''}, 'ability': 'Eclipse', 'operator': '+', 'value': 2, 'sign': None}}
    turn2_d = {'cost': 'R', 'fp': {'number': 1, 'ability': 'Shock', 'value': 450, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Blessing', 'operator': '+', 'value': 20, 'sign': None}}
    turn3_d = {'cost': 'RY', 'fp': {'number': 1, 'ability': 'Smite', 'value': '1/10', 'mult_opp': False, 'mult': 'Blessing', 'sign': None}, 'sp': None}

class lodir:
    name = 'Lodir'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Berserk']
    image_path = imgs_dir + 'lodir.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class malika_ex:
    name = 'Malika Ex'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['Berserk', 'Scarab', 'Shock']
    image_path = imgs_dir + 'malika_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mouktar:
    name = 'Mouktar'
    guild = 'Desert Nomads'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['Crit', 'Shock', 'Eclipse']
    image_path = imgs_dir + 'mouktar.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class namun_ex:
    name = 'Namun Ex'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    race = 'Solarian'
    strength = '120'
    tags = ['+STR', 'Resil']
    image_path = imgs_dir + 'namun_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class nebsen:
    name = 'Nebsen'
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Solarian'
    strength = '150'
    tags = ['Berserk', 'Blessing', 'Shock', 'Smite', 'Riposte']
    image_path = imgs_dir + 'nebsen.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class nehmetawy_ex:
    name = 'Nehmetawy Ex'
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Undead'
    strength = '75'
    tags = ['Shock', 'Death Stare', 'Eclipse']
    image_path = imgs_dir + 'nehmetawy_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class netjhim:
    name = 'Netjhim'
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Human'
    strength = '100'
    tags = ['Heal', 'Purify', 'Fireball', 'Smite', 'Eclipse']
    image_path = imgs_dir + 'netjhim.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class neythiri:
    name = 'Neythiri'
    guild = 'Desert Nomads'
    class_ = 'Marauder'
    race = 'Human'
    strength = '155'
    tags = ['Crit', 'Backstab', 'Eclipse']
    image_path = imgs_dir + 'neythiri.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class obel_isc_ex:
    name = "Obel'isc Ex"
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Golem'
    strength = '160'
    tags = ['Blessing', 'Purify', 'Shock', 'Smite']
    image_path = imgs_dir + 'obel_isc_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class orzine:
    name = 'Orzine'
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Elfine'
    strength = '150'
    tags = ['Blessing', 'Purify', 'Shock', 'Smite']
    image_path = imgs_dir + 'orzine.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ozymandias_ex:
    name = 'Ozymandias Ex'
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Solarian'
    strength = '150'
    tags = ['Blessing', 'Purify', 'Shock', 'Smite']
    image_path = imgs_dir + 'ozymandias_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class prince_metchaf:
    name = 'Prince Metchaf'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    race = 'Solarian'
    strength = '125'
    tags = ['+STR', 'Dodge', 'Blessing', 'Shock']
    image_path = imgs_dir + 'prince_metchaf.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class radames_ex:
    name = 'Radames Ex'
    guild = 'Desert Nomads'
    class_ = 'Berserker'
    race = 'Undead'
    strength = '150'
    tags = ['+STR', 'Scarab', 'Strength Drain', 'Riposte']
    image_path = imgs_dir + 'radames_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ramil_ex:
    name = 'Ramil Ex'
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Human'
    strength = '100'
    tags = ['Shield', 'Shock', 'Smite']
    image_path = imgs_dir + 'ramil_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sael_ik_ex:
    name = "Sael'ik Ex"
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Solarian'
    strength = '80'
    tags = ['Blessing', 'Purify', 'Shock', 'Smite']
    image_path = imgs_dir + 'sael_ik_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sakina:
    name = 'Sakina'
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Human'
    strength = '100'
    tags = ['Resil', 'Heal', 'Purify', 'Shock']
    image_path = imgs_dir + 'sakina.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class shrikan_ex:
    name = 'Shrikan Ex'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    race = 'Solarian'
    strength = '130'
    tags = ['+STR', 'Blessing', 'Shock', 'Riposte']
    image_path = imgs_dir + 'shrikan_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class solaris_kararine_ex:
    name = 'Solaris Kararine Ex'
    guild = 'Desert Nomads'
    class_ = 'Marauder'
    race = 'Solarian'
    strength = '150'
    tags = ['+STR', 'Scarab', 'Heal', 'Shock']
    image_path = imgs_dir + 'solaris_kararine_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class soraya_ex:
    name = 'Soraya Ex'
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Solarian'
    strength = '110'
    tags = ['Scarab', 'Purify', 'Shock']
    image_path = imgs_dir + 'soraya_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class tawaret_ex:
    name = 'Tawaret Ex'
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Solarian'
    strength = '120'
    tags = ['+STR', 'Shield', 'Blessing', 'Shock']
    image_path = imgs_dir + 'tawaret_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class urakia:
    name = 'Urakia'
    guild = 'Desert Nomads'
    class_ = 'Marauder'
    race = 'Solarian'
    strength = '140'
    tags = ['Resil', 'Purify']
    image_path = imgs_dir + 'urakia.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class vizir_mahamoud:
    name = 'Vizir Mahamoud'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Resil', 'Shock', 'Eclipse']
    image_path = imgs_dir + 'vizir_mahamoud.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class youss:
    name = 'Youss'
    guild = 'Desert Nomads'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '150'
    tags = ['+STR', 'Blessing']
    image_path = imgs_dir + 'youss.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class zehanie_ex:
    name = 'Zehanie Ex'
    guild = 'Desert Nomads'
    class_ = 'Warrior'
    strength = '130'
    race = 'Human'
    tags = ['Blessing', 'Scarab', 'Shock']
    image_path = imgs_dir + 'zehanie_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class aberration:
    name = 'Aberration'
    guild = 'Zil Warriors'
    class_ = 'Warrior'
    strength = '130'
    race = 'Guemelite'
    tags = ['Shield', 'Smite']
    image_path = imgs_dir + 'aberration.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class aby_the_hungry_ex:
    name = 'Aby the Hungry Ex'
    guild = 'Zil Warriors'
    class_ = 'Mage'
    race = 'Human'
    strength = '80'
    tags = ['Life Drain', 'Shock', 'Mimic', 'Stench']
    image_path = imgs_dir + 'aby_the_hungry_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class abyssien_the_devourer:
    name = 'Abyssien the Devourer'
    guild = 'Zil Warriors'
    class_ = 'Mage'
    strength = '130'
    race = 'Guemelite'
    tags = ['+DMG', '+STR', 'Fireball', 'Mimic', 'Terror', 'Buffer']
    image_path = imgs_dir + 'abyssien_the_devourer.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class alude_ex:
    name = 'Alude Ex'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '145'
    tags = ['+DMG', 'Thorn', 'Scarab']
    image_path = imgs_dir + 'alude_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class alyce_ex:
    name = 'Alyce Ex'
    guild = 'Zil Warriors'
    class_ = 'Priest'
    strength = '110'
    race = 'Guemelite'
    tags = ['Crit', 'Fireball', 'Heal', 'Purify', 'Buffer']
    image_path = imgs_dir + 'alyce_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class amalgam_ex:
    name = 'Amalgam Ex'
    guild = 'Zil Warriors'
    class_ = 'Berserker'
    race = 'Guemelite'
    strength = '150'
    tags = ['Mimic', 'Terror']
    image_path = imgs_dir + 'amalgam_ex.png'
    turns_texts = ['BY:  3 x Mimic 400', 'R:  STR x 5 & All R->S', 'YY:  Hit 1000 & opp Terror 3000 VS Priest']
    turn1_d = {'cost': 'BY', 'fp': {'number': 3, 'ability': 'Mimic', 'value': 400, 'sign': None}, 'sp': None}
    turn2_d = {'cost': 'R', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'STR', 'operator': 'x', 'value': 5, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'R->S', 'value': 'All', 'sign': None}}
    turn3_d = {'cost': 'YY', 'fp': {'number': 1, 'ability': 'Hit', 'value': 1000, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': True, 'allspec': ''}, 'ability': 'Terror', 'operator': '+', 'value': 3000, 'sign': ',', 'condition': 'VS', 'addability': 'Priest'}}

class archmage_artrezil:
    name = 'Archmage Artrezil'
    guild = 'Zil Warriors'
    class_ = 'Mage'
    strength = '100'
    race = 'Guemelite'
    tags = ['Crit', 'Fireball', 'Spellbreaker', 'Terror']
    image_path = imgs_dir + 'archmage_artrezil.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class arckam:
    name = 'Arckam'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '175'
    tags = ['Dodge', 'Crit', 'Backstab']
    image_path = imgs_dir + 'arckam.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ashtra_ex:
    name = 'Ashtra Ex'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Human'
    strength = '140'
    tags = ['+STR', 'Crit', 'Backstab']
    image_path = imgs_dir + 'ashtra_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ashuu_lu:
    name = "Ashuu'lu"
    guild = 'Zil Warriors'
    class_ = 'Mage'
    race = 'Beast'
    strength = '100'
    tags = ['Rage', 'Crit', 'Fireball']
    image_path = imgs_dir + 'ashuu_lu.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class bazinga:
    name = 'Bazinga'
    guild = 'Zil Warriors'
    class_ = 'Berserker'
    race = 'Ice Elf'
    strength = '150'
    tags = ['+STR', 'Frostbite', 'Terror', 'Ice']
    image_path = imgs_dir + 'bazinga.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class bigrage:
    name = 'Bigrage'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '150'
    tags = ['Rage', 'Dodge', 'Backstab']
    image_path = imgs_dir + 'bigrage.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class bloodsword:
    name = 'BloodSword'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Elfine'
    strength = '160'
    tags = ['+DMG', 'Rage', 'Dodge', 'Riposte']
    image_path = imgs_dir + 'bloodsword.png'
    turns_texts = ['RB:  all DMG +40, 80 if Marauder', 'R:  Rage 30 & Riposte 1', 'RY:  3 x Physical Attack & Dodge 1']
    turn1_d = {'cost': 'RB', 'fp': {'number': 1, 'target': {'all': True, 'opp': False, 'allspec': ''}, 'ability': '+DMG', 'operator': ':', 'value': 40, 'sign': ',', 'condition': 'if', 'addvalue': 80, 'addability': 'Marauder'}, 'sp': None}
    turn2_d = {'cost': 'R', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Rage', 'operator': '+', 'value': 30, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Riposte', 'operator': '+', 'value': 1, 'sign': None}}
    turn3_d = {'cost': 'RY', 'fp': {'number': 3, 'ability': 'Physical Attack', 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Dodge', 'operator': '+', 'value': 1, 'sign': None}}

class brutus:
    name = 'Brutus'
    guild = 'Zil Warriors'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['Rage', 'Berserk']
    image_path = imgs_dir + 'brutus.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class bubblelize_ex:
    name = 'Bubblelize Ex'
    guild = 'Zil Warriors'
    class_ = 'Priest'
    race = 'Guemelite'
    strength = '105'
    tags = ['Purify', 'Mimic', 'Terror']
    image_path = imgs_dir + 'bubblelize_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class cigue_ex:
    name = 'Cigue Ex'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '150'
    tags = ['+DMG', 'Berserk', 'Shock']
    image_path = imgs_dir + 'cigue_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class dancing_blade_ex:
    name = 'Dancing-Blade Ex'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['Dodge', 'Crit']
    image_path = imgs_dir + 'dancing_blade_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class dark_ex:
    name = 'Dark Ex'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['+DMG', 'Crit', 'Shock', 'Mimic']
    image_path = imgs_dir + 'dark_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class faceless:
    name = 'Faceless'
    guild = 'Zil Warriors'
    class_ = 'Warrior'
    race = "Hom'Chai"
    strength = '125'
    tags = ['+STR', 'Shield']
    image_path = imgs_dir + 'faceless.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class fenrath:
    name = 'Fenrath'
    guild = 'Zil Warriors'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '125'
    tags = ['Rage', 'Berserk']
    image_path = imgs_dir + 'fenrath.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class golemarlok_ex:
    name = 'Golemarlok Ex'
    guild = 'Zil Warriors'
    class_ = 'Mage'
    race = 'Golem'
    strength = '100'
    tags = ['Blizzard', 'Fireball', 'Mimic', 'Ice']
    image_path = imgs_dir + 'golemarlok_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class grognon:
    name = 'Grognon'
    guild = 'Zil Warriors'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+DMG', '+STR']
    image_path = imgs_dir + 'grognon.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class iron_mask:
    name = 'Iron Mask'
    guild = 'Zil Warriors'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['Fireball', 'Backstab', '-DMG']
    image_path = imgs_dir + 'iron_mask.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class karavan_sv:
    name = 'Karavan Sv'
    guild = 'Zil Warriors'
    class_ = 'Colossus'
    race = 'Unknown(R)'
    strength = '280'
    tags = ['Fireball', 'Backstab', 'Mimic']
    image_path = imgs_dir + 'karavan_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kriss_ex:
    name = 'Kriss Ex'
    guild = 'Zil Warriors'
    class_ = 'Bard'
    race = 'Human'
    strength = '0'
    tags = ['+DMG', 'Smite', 'Terror']
    image_path = imgs_dir + 'kriss_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kuraying_ex:
    name = 'Kuraying Ex'
    guild = 'Zil Warriors'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '110'
    tags = ['Dodge', 'Fireball', 'Terror']
    image_path = imgs_dir + 'kuraying_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lunatik_ex:
    name = 'Lunatik Ex'
    guild = 'Zil Warriors'
    class_ = 'Priest'
    race = 'Human'
    strength = '150'
    tags = ['+DMG', 'Purify', 'Shock', 'Smite']
    image_path = imgs_dir + 'lunatik_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class malicia:
    name = 'Malicia'
    guild = 'Zil Warriors'
    class_ = 'Priest'
    race = 'Human'
    strength = '45'
    tags = ['Crit', 'Shock', 'Fireball', 'Smite', 'Terror']
    image_path = imgs_dir + 'malicia.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mallascaria:
    name = 'Mallascaria'
    guild = 'Zil Warriors'
    class_ = 'Bard'
    race = 'Guemelite'
    strength = '0'
    tags = ['Dodge', 'Fireball', 'Mimic']
    image_path = imgs_dir + 'mallascaria.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mandrak_ex:
    name = 'Mandrak Ex'
    guild = 'Zil Warriors'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['Rage', 'Powder', 'Fireball', 'Terror']
    image_path = imgs_dir + 'mandrak_ex.png'
    turns_texts = ['R:  opp Terror 60 & Rage 20', 'RB:  3 x Fireball 300 & B->S', 'RY:  Fireball 900 & opp Powder 3']
    turn1_d = {'cost': 'R', 'fp': {'number': 1, 'target': {'all': False, 'opp': True, 'allspec': ''}, 'ability': 'Terror', 'operator': '+', 'value': 60, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Rage', 'operator': '+', 'value': 20, 'sign': None}}
    turn2_d = {'cost': 'RB', 'fp': {'number': 3, 'ability': 'Fireball', 'value': 300, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'B->S', 'value': 1, 'sign': None}}
    turn3_d = {'cost': 'RY', 'fp': {'number': 1, 'ability': 'Fireball', 'value': 900, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': True, 'allspec': ''}, 'ability': 'Powder', 'operator': '+', 'value': 3, 'sign': None}}

class marlok_s_golem_ex:
    name = "Marlok's Golem Ex"
    guild = 'Zil Warriors'
    class_ = 'Warrior'
    race = 'Golem'
    strength = '120'
    tags = ['Riposte']
    image_path = imgs_dir + 'marlok_s_golem_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mashtok_ex:
    name = 'Mashtok Ex'
    guild = 'Zil Warriors'
    class_ = 'Berserker'
    race = 'Beast'
    strength = '150'
    tags = ['Berserk', 'Shock', 'Riposte']
    image_path = imgs_dir + 'mashtok_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class monozilk:
    name = 'Monozilk'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '165'
    tags = ['Dodge', 'Crit', 'Backstab']
    image_path = imgs_dir + 'monozilk.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mysticio_ex:
    name = 'Mysticio Ex'
    guild = 'Zil Warriors'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['+DMG', 'Fireball']
    image_path = imgs_dir + 'mysticio_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class n_taba_ex:
    name = "N'taba Ex"
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    strength = '170'
    race = 'Guemelite'
    tags = ['+DMG', 'Berserk', 'Crit', 'Shock', 'Smite']
    image_path = imgs_dir + 'n_taba_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class nard:
    name = 'Nard'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Human'
    strength = '160'
    tags = ['+STR', 'Dodge', 'Crit']
    image_path = imgs_dir + 'nard.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class oukandari_ex:
    name = 'Oukandari Ex'
    guild = 'Zil Warriors'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '125'
    tags = ['Rage']
    image_path = imgs_dir + 'oukandari_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class puppet_x_ex:
    name = 'Puppet X Ex'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Golem'
    strength = '150'
    tags = ['+DMG', 'Spellbreaker', 'Mimic']
    image_path = imgs_dir + 'puppet_x_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class salamalek_ex:
    name = 'Salamalek Ex'
    guild = 'Zil Warriors'
    class_ = 'Berserker'
    race = 'Beast'
    strength = '130'
    tags = ['Rage']
    image_path = imgs_dir + 'salamalek_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class salem:
    name = 'Salem'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '150'
    tags = ['+STR', 'Crit', 'Backstab', 'Terror']
    image_path = imgs_dir + 'salem.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class saphyra_the_zil_ex:
    name = 'Saphyra the Zil Ex'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['Fireball', 'Mimic']
    image_path = imgs_dir + 'saphyra_the_zil_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sciofoby_ex:
    name = 'Sciofoby Ex'
    guild = 'Zil Warriors'
    class_ = 'Mage'
    strength = '90'
    race = 'Guemelite'
    tags = ['Fireball', 'Heal', 'Terror']
    image_path = imgs_dir + 'sciofoby_ex.png'
    turns_texts = ['RB:  Fireball 1400 & 2 x Portal 300', 'RRY:  Heal 1500 & opp Terror 300', 'R:  2 x Hit = opp -DMG']
    turn1_d = {'cost': 'RB', 'fp': {'number': 1, 'ability': 'Fireball', 'value': 1400, 'sign': None}, 'sp': {'number': 2, 'ability': 'Portal', 'value': 300, 'sign': None}}
    turn2_d = {'cost': 'RRY', 'fp': {'number': 1, 'ability': 'Heal', 'value': 1500, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': True, 'allspec': ''}, 'ability': 'Terror', 'operator': '+', 'value': 300, 'sign': None}}
    turn3_d = {'cost': 'R', 'fp': {'number': 2, 'ability': 'Hit', 'value': 1, 'mult_opp': True, 'mult': '-DMG', 'sign': None}, 'sp': None}

class selene:
    name = 'Selene'
    guild = 'Zil Warriors'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '80'
    tags = ['Shield', 'Fireball', 'Terror']
    image_path = imgs_dir + 'selene.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class silene:
    name = 'Silene'
    guild = 'Zil Warriors'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '130'
    tags = ['+STR', 'Death Stare']
    image_path = imgs_dir + 'silene.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class skor_shi_sv:
    name = "Skor'Shi Sv"
    guild = 'Zil Warriors'
    class_ = 'Colossus'
    strength = '200'
    race = 'Dragon'
    tags = ['Crit', 'Shock', 'Terror']
    image_path = imgs_dir + 'skor_shi_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class skygatt:
    name = 'Skygatt'
    guild = 'Zil Warriors'
    class_ = 'Berserker'
    race = 'Ice Elf'
    strength = '150'
    tags = ['Berserk', 'Frostbite', 'Ice']
    image_path = imgs_dir + 'skygatt.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class soriek_ex:
    name = 'Soriek Ex'
    guild = 'Zil Warriors'
    class_ = 'Bard'
    race = 'Guemelite'
    strength = '0'
    tags = ['Crit']
    image_path = imgs_dir + 'soriek_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class spike_the_fool_ex:
    name = 'Spike the Fool Ex'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    strength = '175'
    race = 'Guemelite'
    tags = ['+DMG', 'Dodge', 'Mimic', 'Thorn']
    image_path = imgs_dir + 'spike_the_fool_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class terrifik_ex:
    name = 'Terrifik Ex'
    guild = 'Zil Warriors'
    class_ = 'Priest'
    race = 'Human'
    strength = '145'
    tags = ['Shock', 'Smite', 'Terror']
    image_path = imgs_dir + 'terrifik_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_juggler_ex:
    name = 'The Juggler Ex'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '160'
    tags = ['+DMG', 'Dodge', 'Shock']
    image_path = imgs_dir + 'the_juggler_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_liberated_telendar:
    name = 'The Liberated Telendar'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    strength = '190'
    race = 'Human'
    tags = ['Backstab', 'Crit', 'Rage', 'Buffer']
    image_path = imgs_dir + 'the_liberated_telendar.png'
    turns_texts = ['RB:  Rage 50 & all Zil Warriors Crit 2', 'RY:  Hit 1000, 1500 VS Mage', 'R:  Backstab 500, 750 VS Nehantists & R->S']
    turn1_d = {'cost': 'RB', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Rage', 'operator': '+', 'value': 50, 'sign': None}, 'sp': {'number': 1, 'target': {'all': True, 'opp': False, 'allspec': 'Zil Warriors'}, 'ability': 'Crit', 'operator': '+', 'value': 2, 'sign': None}}
    turn2_d = {'cost': 'RY', 'fp': {'number': 1, 'ability': 'Hit', 'value': 1000, 'sign': ',', 'condition': 'VS', 'addvalue': 1500, 'addability': 'Mage'}, 'sp': None}
    turn3_d = {'cost': 'R', 'fp': {'number': 1, 'ability': 'Backstab', 'value': 500, 'sign': ',', 'condition': 'VS', 'addvalue': 750, 'addability': 'Nehantists'}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'R->S', 'value': 1, 'sign': None}}

class the_psychurgist:
    name = 'The Psychurgist'
    guild = 'Zil Warriors'
    class_ = 'Priest'
    race = 'Guemelite'
    strength = '115'
    tags = ['Shock', 'Fireball', 'Smite']
    image_path = imgs_dir + 'the_psychurgist.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_rabid_telendar:
    name = 'The Rabid Telendar'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Human'
    strength = '175'
    tags = ['Berserk', 'Crit', 'Backstab']
    image_path = imgs_dir + 'the_rabid_telendar.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_shadow:
    name = 'The Shadow'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '150'
    tags = ['+STR', 'Crit', 'Backstab', 'Mimic']
    image_path = imgs_dir + 'the_shadow.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_spooker:
    name = 'The Spooker'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '130'
    tags = ['Crit', 'Shock', 'Terror']
    image_path = imgs_dir + 'the_spooker.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class vick_ticket_seller_ex:
    name = 'Vick, Ticket Seller Ex'
    guild = 'Zil Warriors'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '120'
    tags = ['Berserk']
    image_path = imgs_dir + 'vick_ticket_seller_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class videncia_ex:
    name = 'Videncia Ex'
    guild = 'Zil Warriors'
    class_ = 'Mage'
    race = 'Undead'
    strength = '100'
    tags = ['Life Drain', 'Shock', 'Mimic', 'Terror']
    image_path = imgs_dir + 'videncia_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class volkarius_ex:
    name = 'Volkarius Ex'
    guild = 'Zil Warriors'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '130'
    tags = ['Rage', 'Shock', 'Fireball']
    image_path = imgs_dir + 'volkarius_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class wakywak:
    name = 'Wakywak'
    guild = 'Zil Warriors'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '135'
    tags = ['Rage', 'Berserk']
    image_path = imgs_dir + 'wakywak.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class wild:
    name = 'Wild'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '150'
    tags = ['Berserk', 'Riposte']
    image_path = imgs_dir + 'wild.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class wolvos_ex:
    name = 'Wolvos Ex'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '175'
    tags = ['+DMG', 'Rage', 'Dodge', 'Mimic']
    image_path = imgs_dir + 'wolvos_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class zereshin:
    name = 'Zereshin'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '150'
    tags = ['Dodge', 'Backstab']
    image_path = imgs_dir + 'zereshin.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class zil_the_shadow_ex:
    name = 'Zil, the Shadow Ex'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '170'
    tags = ['Shock', 'Mimic', 'Terror']
    image_path = imgs_dir + 'zil_the_shadow_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class atugan_sv:
    name = 'Atugan Sv'
    guild = 'Stone Linkers'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['+STR', 'Dodge', 'Shock']
    image_path = imgs_dir + 'atugan_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class catalyna_sv:
    name = 'Catalyna Sv'
    guild = 'Stone Linkers'
    class_ = 'Warrior'
    race = 'Golem'
    strength = '130'
    tags = ['Resil', 'Shock']
    image_path = imgs_dir + 'catalyna_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class erguji_sv:
    name = 'Erguji Sv'
    guild = 'Stone Linkers'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '125'
    tags = ['+STR', 'Shield']
    image_path = imgs_dir + 'erguji_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class gatsu_sv:
    name = 'Gatsu Sv'
    guild = 'Stone Linkers'
    class_ = 'Berserker'
    race = 'Human'
    strength = '160'
    tags = ['Berserk', 'Riposte']
    image_path = imgs_dir + 'gatsu_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kalion_sv:
    name = 'Kalion Sv'
    guild = 'Stone Linkers'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '150'
    tags = ['+STR', 'Fireball']
    image_path = imgs_dir + 'kalion_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class karreg_sv:
    name = 'Karreg Sv'
    guild = 'Stone Linkers'
    class_ = 'Mage'
    race = 'Dais'
    strength = '50'
    tags = ['Thorn', 'Ice']
    image_path = imgs_dir + 'karreg_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kubilai_sv:
    name = 'Kubilai Sv'
    guild = 'Stone Linkers'
    class_ = 'Berserker'
    race = 'Human'
    strength = '150'
    tags = ['+STR']
    image_path = imgs_dir + 'kubilai_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lady_izandra_sv:
    name = 'Lady Izandra Sv'
    guild = 'Stone Linkers'
    class_ = 'Priest'
    race = 'Guemelite'
    strength = '85'
    tags = ['Heal', 'Shock', 'Smite']
    image_path = imgs_dir + 'lady_izandra_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class larzaen_sv:
    name = 'Larzaen Sv'
    guild = 'Stone Linkers'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['Dodge', 'Frostbite', 'Spellbreaker', 'Ice']
    image_path = imgs_dir + 'larzaen_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lazar_zackarov_sv:
    name = 'Lazar Zackarov Sv'
    guild = 'Stone Linkers'
    class_ = 'Priest'
    race = 'Guemelite'
    strength = '100'
    tags = ['Purify', 'Shock', 'Ice']
    image_path = imgs_dir + 'lazar_zackarov_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class master_maen_sv:
    name = 'Master Maen Sv'
    guild = 'Stone Linkers'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '60'
    tags = ['Lightning']
    image_path = imgs_dir + 'master_maen_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class nyaga_sv:
    name = 'Nyaga Sv'
    guild = 'Stone Linkers'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['Rage']
    image_path = imgs_dir + 'nyaga_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class temujin_sv:
    name = 'Temujin Sv'
    guild = 'Stone Linkers'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['+DMG']
    image_path = imgs_dir + 'temujin_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class abigor_sv:
    name = 'Abigor Sv'
    guild = 'Nehantists'
    class_ = 'Colossus'
    race = 'Unknown(R)'
    strength = '300'
    tags = ['Rage', 'Fireball']
    image_path = imgs_dir + 'abigor_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class abraxal_ex:
    name = 'Abraxal Ex'
    guild = 'Nehantists'
    class_ = 'Mage'
    race = 'Demon'
    strength = '120'
    tags = ['Shield', 'Life Drain', 'Fireball']
    image_path = imgs_dir + 'abraxal_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class aldoran_ex:
    name = 'Aldoran Ex'
    guild = 'Nehantists'
    class_ = 'Mage'
    race = 'Demon'
    strength = '0'
    tags = ['Shield', 'Fireball']
    image_path = imgs_dir + 'aldoran_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class almaria:
    name = 'Almaria'
    guild = 'Nehantists'
    class_ = 'Mage'
    race = 'Undead'
    strength = '130'
    tags = ['+STR', 'Dodge', 'Life Drain', 'Stench']
    image_path = imgs_dir + 'almaria.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class amidaraxar:
    name = 'Amidaraxar'
    guild = 'Nehantists'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['Fireball', '-DMG']
    image_path = imgs_dir + 'amidaraxar.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class anagram_ex:
    name = 'Anagram Ex'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '150'
    tags = ['+STR', 'Crit', 'Shock', 'Backstab']
    image_path = imgs_dir + 'anagram_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ardrakar_ex:
    name = 'Ardrakar Ex'
    guild = 'Nehantists'
    class_ = 'Warrior'
    strength = '130'
    race = 'Demon'
    tags = ['+DMG', '-DMG']
    image_path = imgs_dir + 'ardrakar_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ash:
    name = 'Ash'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Demon'
    strength = '165'
    tags = ['+STR', 'Dodge', 'Crit', '-DMG']
    image_path = imgs_dir + 'ash.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class asmoroth_sv:
    name = 'Asmoroth Sv'
    guild = 'Nehantists'
    class_ = 'Colossus'
    strength = '250'
    race = 'Dragon'
    tags = ['+STR', 'Fireball', 'Life Drain']
    image_path = imgs_dir + 'asmoroth_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class azaram:
    name = 'Azaram'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Demon'
    strength = '125'
    tags = ['+STR', 'Fireball', '-DMG']
    image_path = imgs_dir + 'azaram.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class big_daddy_ex:
    name = 'Big Daddy Ex'
    guild = 'Nehantists'
    class_ = 'Berserker'
    race = 'Demon'
    strength = '180'
    tags = ['Crit', 'Life Drain', 'Strength Drain']
    image_path = imgs_dir + 'big_daddy_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class calypse:
    name = 'Calypse'
    guild = 'Nehantists'
    class_ = 'Bard'
    race = 'Demon'
    strength = '0'
    tags = ['Life Drain', 'Fireball']
    image_path = imgs_dir + 'calypse.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class carfax_ex:
    name = 'Carfax Ex'
    guild = 'Nehantists'
    class_ = 'Mage'
    strength = '80'
    race = 'Guemelite'
    tags = ['Crit', 'Fireball']
    image_path = imgs_dir + 'carfax_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class carkasse:
    name = 'Carkasse'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '130'
    tags = ['Shield']
    image_path = imgs_dir + 'carkasse.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ceaches_ixef_ex:
    name = 'Ceaches Ixef Ex'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Undead'
    strength = '150'
    tags = ['Thorn', 'Life Drain']
    image_path = imgs_dir + 'ceaches_ixef_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class chalice:
    name = 'Chalice'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Demon'
    strength = '0'
    tags = ['+STR', 'Life Drain', 'Riposte']
    image_path = imgs_dir + 'chalice.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class cinderosa_ex:
    name = 'Cinderosa Ex'
    guild = 'Nehantists'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '0'
    tags = ['+STR', 'Life Drain', 'Powder', 'Fireball', '-DMG']
    image_path = imgs_dir + 'cinderosa_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class crost_ex:
    name = 'Crost Ex'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Demon'
    strength = '120'
    tags = ['Thorn', 'Life Drain']
    image_path = imgs_dir + 'crost_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class death_tree_ex:
    name = 'Death-Tree Ex'
    guild = 'Nehantists'
    class_ = 'Mage'
    strength = '120'
    race = 'Dais'
    tags = ['+DMG', 'Life Drain', 'Thorn', 'Buffer']
    image_path = imgs_dir + 'death_tree_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class deathblade_ex:
    name = 'DeathBlade Ex'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Demon'
    strength = '150'
    tags = ['+DMG', '+STR', 'Life Drain', 'Fireball']
    image_path = imgs_dir + 'deathblade_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class dimizar:
    name = 'Dimizar'
    guild = 'Nehantists'
    class_ = 'Mage'
    strength = '100'
    race = 'Demon'
    tags = ['+STR', '-DMG', 'Life Drain', 'Spellbreaker', 'Buffer']
    image_path = imgs_dir + 'dimizar.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class echios_ex:
    name = 'Echios Ex'
    guild = 'Nehantists'
    class_ = 'Warrior'
    strength = '130'
    race = 'Demon'
    tags = ['+STR', 'Fireball', 'Life Drain', 'Rune']
    image_path = imgs_dir + 'echios_ex.png'
    turns_texts = ['RR:  Fireball 1600 & All R->S', 'B:  STR +500 & Rune 1', 'BY:  Runic Life Drain 800']
    turn1_d = {'cost': 'RR', 'fp': {'number': 1, 'ability': 'Fireball', 'value': 1600, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'R->S', 'value': 'All', 'sign': None}}
    turn2_d = {'cost': 'B', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'STR', 'operator': '+', 'value': 500, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Rune', 'operator': '+', 'value': 1, 'sign': None}}
    turn3_d = {'cost': 'BY', 'fp': {'number': 1, 'attribute': 'Runic', 'ability': 'Life Drain', 'value': 800, 'sign': None}, 'sp': None}

class edrianne_ex:
    name = 'Edrianne Ex'
    guild = 'Nehantists'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['Dodge', 'Shield', 'Life Drain', 'Shock', 'Fireball']
    image_path = imgs_dir + 'edrianne_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class envy_ex:
    name = 'Envy Ex'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Demon'
    strength = '165'
    tags = ['Berserk']
    image_path = imgs_dir + 'envy_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class eval_ex:
    name = 'Eval Ex'
    guild = 'Nehantists'
    class_ = 'Priest'
    race = 'Demon'
    strength = '75'
    tags = ['Fireball', 'Death Stare']
    image_path = imgs_dir + 'eval_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class furnace:
    name = 'Furnace'
    guild = 'Nehantists'
    class_ = 'Mage'
    race = 'Demon'
    strength = '100'
    tags = ['+STR', 'Fireball']
    image_path = imgs_dir + 'furnace.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class gluttony_ex:
    name = 'Gluttony Ex'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Demon'
    strength = '130'
    tags = ['+DMG', 'Life Drain', 'Fireball']
    image_path = imgs_dir + 'gluttony_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class gnarl:
    name = 'Gnarl'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Demon'
    strength = '130'
    tags = ['Shield', 'Life Drain', 'Shock']
    image_path = imgs_dir + 'gnarl.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class gollyus_ex:
    name = 'Gollyus Ex'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Demon'
    strength = '130'
    tags = ['Berserk', 'Shock', 'Death Stare']
    image_path = imgs_dir + 'gollyus_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class grief:
    name = 'Grief'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Demon'
    strength = '150'
    tags = ['Berserk', 'Life Drain', 'Fireball', 'Backstab']
    image_path = imgs_dir + 'grief.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class hate_ex:
    name = 'Hate Ex'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Demon'
    strength = '140'
    tags = ['Crit', 'Fireball', 'Backstab', '-DMG']
    image_path = imgs_dir + 'hate_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class heliamphora_ex:
    name = 'Heliamphora Ex'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Elfine'
    strength = '140'
    tags = ['+DMG', 'Rage', 'Life Drain', 'Fireball']
    image_path = imgs_dir + 'heliamphora_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class herebus_ex:
    name = 'Herebus Ex'
    guild = 'Nehantists'
    class_ = 'Priest'
    race = 'Demon'
    strength = '150'
    tags = ['+DMG', 'Life Drain', 'Shock', 'Fireball', 'Smite']
    image_path = imgs_dir + 'herebus_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class inquisitor_ex:
    name = 'Inquisitor Ex'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Demon'
    strength = '125'
    tags = ['Shield', 'Shock', 'Spellbreaker', '-DMG']
    image_path = imgs_dir + 'inquisitor_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ishaia_of_the_dead:
    name = 'Ishaia of the Dead'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Undead'
    strength = '130'
    tags = ['Shock']
    image_path = imgs_dir + 'ishaia_of_the_dead.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kaes_the_malefic_ex:
    name = 'Kaes the Malefic Ex'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Demon'
    strength = '700'
    tags = ['Crit', 'Life Drain', 'Noble', 'Death Stare']
    image_path = imgs_dir + 'kaes_the_malefic_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class karrie:
    name = 'Karrie'
    guild = 'Nehantists'
    class_ = 'Priest'
    race = 'Undead'
    strength = '90'
    tags = ['Shield', 'Fireball']
    image_path = imgs_dir + 'karrie.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kimaera_ex:
    name = 'Kimaera Ex'
    guild = 'Nehantists'
    class_ = 'Mage'
    race = 'Demon'
    strength = '100'
    tags = ['Lightning', 'Fireball', 'Ice']
    image_path = imgs_dir + 'kimaera_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class korpus_ex:
    name = 'Korpus Ex'
    guild = 'Nehantists'
    class_ = 'Mage'
    race = 'Demon'
    strength = '100'
    tags = ['Shock', 'Fireball', 'Portal', '-DMG']
    image_path = imgs_dir + 'korpus_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lady_of_nehant:
    name = 'Lady of Nehant'
    guild = 'Nehantists'
    class_ = 'Warrior'
    strength = '130'
    race = 'Guemelite'
    tags = ['+STR', 'Backstab', 'Crit', 'Death Stare', 'Mimic', 'Buffer']
    image_path = imgs_dir + 'lady_of_nehant.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lily_ex:
    name = 'Lily Ex'
    guild = 'Nehantists'
    class_ = 'Mage'
    race = 'Demon'
    strength = '150'
    tags = ['Crit', 'Life Drain', 'Fireball', 'Death Stare']
    image_path = imgs_dir + 'lily_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lost_eglantyne_ex:
    name = 'Lost Eglantyne Ex'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Undead'
    strength = '160'
    tags = ['Life Drain', 'Fireball', 'Death Stare', 'Stench']
    image_path = imgs_dir + 'lost_eglantyne_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class nightmare_ex:
    name = 'Nightmare Ex'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Demon'
    strength = '120'
    tags = ['+STR', 'Life Drain', 'Fireball']
    image_path = imgs_dir + 'nightmare_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ouait_ka:
    name = 'Ouait Ka'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Undead'
    strength = '120'
    tags = ['Life Drain', 'Shock', 'Death Stare', 'Stench']
    image_path = imgs_dir + 'ouait_ka.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class pain:
    name = 'Pain'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Demon'
    strength = '150'
    tags = ['Thorn', 'Life Drain']
    image_path = imgs_dir + 'pain.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class rathamantis_ex:
    name = 'Rathamantis Ex'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Demon'
    strength = '155'
    tags = ['Life Drain', 'Backstab', '-DMG']
    image_path = imgs_dir + 'rathamantis_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ripper:
    name = 'Ripper'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Demon'
    strength = '120'
    tags = ['+STR', 'Thorn', 'Life Drain', 'Fireball']
    image_path = imgs_dir + 'ripper.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class scourge_of_souls:
    name = 'Scourge of Souls'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Demon'
    strength = '0'
    tags = ['Shock', 'Terror', 'Strength Drain']
    image_path = imgs_dir + 'scourge_of_souls.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sethan_arai:
    name = 'Sethan Arai'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Demon'
    strength = '165'
    tags = ['Life Drain', 'Backstab']
    image_path = imgs_dir + 'sethan_arai.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class silent_ex:
    name = 'Silent Ex'
    guild = 'Nehantists'
    class_ = 'Marauder'
    strength = '175'
    race = 'Demon'
    tags = ['Backstab', 'Rage']
    image_path = imgs_dir + 'silent_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class skeletik:
    name = 'Skeletik'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Undead'
    strength = '150'
    tags = ['+STR', 'Life Drain', 'Riposte']
    image_path = imgs_dir + 'skeletik.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sloth_ex:
    name = 'Sloth Ex'
    guild = 'Nehantists'
    class_ = 'Mage'
    race = 'Demon'
    strength = '80'
    tags = ['Thorn', 'Life Drain', 'Thunderstruck', 'Fireball']
    image_path = imgs_dir + 'sloth_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class soul_chewer:
    name = 'Soul Chewer'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Demon'
    strength = '160'
    tags = ['+DMG', 'Life Drain', 'Backstab']
    image_path = imgs_dir + 'soul_chewer.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sphatik_ex:
    name = 'Sphatik Ex'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Demon'
    strength = '100'
    tags = ['Shield', 'Life Drain', 'Shock']
    image_path = imgs_dir + 'sphatik_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class thanatissia:
    name = 'Thanatissia'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Undead'
    strength = '130'
    tags = ['Berserk', 'Life Drain', 'Shock']
    image_path = imgs_dir + 'thanatissia.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_fallen_ex:
    name = 'The Fallen Ex'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Demon'
    strength = '130'
    tags = ['+STR', 'Resil', 'Blessing', 'Life Drain', 'Fireball', '-DMG']
    image_path = imgs_dir + 'the_fallen_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_receptacle:
    name = 'The Receptacle'
    guild = 'Nehantists'
    class_ = 'Mage'
    race = 'Demon'
    strength = '50'
    tags = ['Shield', 'Shock', 'Fireball', '-DMG']
    image_path = imgs_dir + 'the_receptacle.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class torment:
    name = 'Torment'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Demon'
    strength = '160'
    tags = ['Dodge', 'Fireball', 'Backstab']
    image_path = imgs_dir + 'torment.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class utkin_the_spawn:
    name = 'Utkin the spawn'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Demon'
    strength = '170'
    tags = ['Dodge', 'Crit', '-DMG']
    image_path = imgs_dir + 'utkin_the_spawn.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class vordak_ex:
    name = 'Vordak Ex'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Demon'
    strength = '120'
    tags = ['+DMG', '+STR', 'Death Stare', 'Riposte']
    image_path = imgs_dir + 'vordak_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class zejabel:
    name = 'Zejabel'
    guild = 'Nehantists'
    class_ = 'Mage'
    race = 'Undead'
    strength = '90'
    tags = ['Life Drain', 'Fireball', '-DMG']
    image_path = imgs_dir + 'zejabel.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class absalon:
    name = 'Absalon'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '130'
    tags = ['+DMG', 'Shield']
    image_path = imgs_dir + 'absalon.png'
    turns_texts = ['B:  Shield 320, 480 VS Guemelite', 'RR:  Hit 500, +250 x B', 'Y:  Hit 200 x R & DMG +150']
    turn1_d = {'cost': 'B', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Shield', 'operator': '+', 'value': 320, 'sign': ',', 'condition': 'VS', 'addvalue': 480, 'addability': 'Guemelite'}, 'sp': None}
    turn2_d = {'cost': 'RR', 'fp': {'number': 1, 'ability': 'Hit', 'value': 500, 'sign': '+', 'addvalue': 250, 'incr_opp': False, 'addability': 'B'}, 'sp': None}
    turn3_d = {'cost': 'Y', 'fp': {'number': 1, 'ability': 'Hit', 'value': 200, 'mult_opp': False, 'mult': 'R', 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': '+DMG', 'operator': ':', 'value': 150, 'sign': None}}

class aerouant_ex:
    name = 'Aerouant Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Human'
    strength = '80'
    tags = ['Ice', 'Shock', 'Spellbreaker']
    image_path = imgs_dir + 'aerouant_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class anazra:
    name = 'Anazra'
    guild = 'Noz'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['Dodge', 'Spellbreaker', 'Ice']
    image_path = imgs_dir + 'anazra.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class angelica:
    name = 'Angelica'
    guild = 'Noz'
    class_ = 'Marauder'
    race = 'Human'
    strength = '140'
    tags = ['+DMG', 'Resil', 'Dodge', 'Backstab']
    image_path = imgs_dir + 'angelica.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class archmage_anryena:
    name = 'Archmage Anryena'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '125'
    tags = ['+DMG', 'Rage', 'Shock', 'Fireball']
    image_path = imgs_dir + 'archmage_anryena.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class arkalon:
    name = 'Arkalon'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Undead'
    strength = '130'
    tags = ['Berserk', 'Life Drain']
    image_path = imgs_dir + 'arkalon.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class blanche_of_arcania:
    name = 'Blanche of Arcania'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '110'
    tags = ['+DMG', 'Fireball']
    image_path = imgs_dir + 'blanche_of_arcania.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class bomzar:
    name = 'Bomzar'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Golem'
    strength = '110'
    tags = ['+STR', 'Shield', 'Fireball']
    image_path = imgs_dir + 'bomzar.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class breor_of_gwad:
    name = 'Breor of Gwad'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '130'
    tags = ['+STR', 'Shield']
    image_path = imgs_dir + 'breor_of_gwad.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class catherine_ex:
    name = 'Catherine Ex'
    guild = 'Noz'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['Dodge', 'Shock', 'Fireball']
    image_path = imgs_dir + 'catherine_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class delko_ex:
    name = 'Delko Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Human'
    strength = '110'
    tags = ['+DMG', 'Spellbreaker']
    image_path = imgs_dir + 'delko_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class dragast:
    name = 'Dragast'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Golem'
    strength = '120'
    tags = ['+DMG', 'Shield']
    image_path = imgs_dir + 'dragast.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class eglantyne:
    name = 'Eglantyne'
    guild = 'Noz'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['Backstab']
    image_path = imgs_dir + 'eglantyne.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class exhien_ex:
    name = 'Exhien Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['+DMG', 'Shock', 'Fireball']
    image_path = imgs_dir + 'exhien_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class freiyar_ex:
    name = 'Freiyar Ex'
    guild = 'Noz'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '150'
    tags = ['Spellbreaker', 'Backstab']
    image_path = imgs_dir + 'freiyar_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class hybrid_anryena:
    name = 'Hybrid Anryena'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '120'
    tags = ['+DMG', 'Rage', 'Spellbreaker']
    image_path = imgs_dir + 'hybrid_anryena.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class hyraleone_ex:
    name = 'Hyraleone Ex'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['Shield']
    image_path = imgs_dir + 'hyraleone_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class joltesk_ex:
    name = 'Joltesk Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Golem'
    strength = '50'
    tags = ['Shield', 'Thunderstruck', 'Shock', 'Lightning']
    image_path = imgs_dir + 'joltesk_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kelltaron:
    name = 'Kelltaron'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '125'
    tags = ['Shield', 'Spellbreaker']
    image_path = imgs_dir + 'kelltaron.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kerastasion_ex:
    name = 'Kerastasion Ex'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '120'
    tags = ['+DMG']
    image_path = imgs_dir + 'kerastasion_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ketanir_ex:
    name = 'Ketanir Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['Shield', 'Shock']
    image_path = imgs_dir + 'ketanir_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kombust_ex:
    name = 'Kombust Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Golem'
    strength = '100'
    tags = ['+DMG', 'Shock', 'Fireball']
    image_path = imgs_dir + 'kombust_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kounok:
    name = 'Kounok'
    guild = 'Noz'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '150'
    tags = ['Rage', 'Shock', 'Fireball']
    image_path = imgs_dir + 'kounok.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class krakos_sv:
    name = 'Krakos Sv'
    guild = 'Noz'
    class_ = 'Colossus'
    race = 'Unknown(R)'
    strength = '200'
    tags = ['+DMG', 'Shock']
    image_path = imgs_dir + 'krakos_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lady_ardrakar_ex:
    name = 'Lady Ardrakar Ex'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '130'
    tags = ['+DMG', 'Shock']
    image_path = imgs_dir + 'lady_ardrakar_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class loniz_ex:
    name = 'Loniz Ex'
    guild = 'Noz'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '170'
    tags = ['Fireball', 'Ice']
    image_path = imgs_dir + 'loniz_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lord_alishk_ex:
    name = 'Lord Alishk Ex'
    guild = 'Noz'
    class_ = 'Mage'
    strength = '120'
    race = 'Human'
    tags = ['Fireball', 'Resil']
    image_path = imgs_dir + 'lord_alishk_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lord_zahal_ex:
    name = 'Lord Zahal Ex'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '135'
    tags = ['+DMG']
    image_path = imgs_dir + 'lord_zahal_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class loryana_ex:
    name = 'Loryana Ex'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '130'
    tags = ['+STR', 'Spellbreaker', 'Fireball']
    image_path = imgs_dir + 'loryana_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mahawk:
    name = 'Mahawk'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['+DMG', 'Ice']
    image_path = imgs_dir + 'mahawk.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class marlok_the_repentant:
    name = 'Marlok the Repentant'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['Fireball']
    image_path = imgs_dir + 'marlok_the_repentant.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class master_mage_kire_ex:
    name = 'Master-Mage Kire Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['Lightning', 'Spellbreaker']
    image_path = imgs_dir + 'master_mage_kire_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class master_mage_marzhin:
    name = 'Master-Mage Marzhin'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['Lightning']
    image_path = imgs_dir + 'master_mage_marzhin.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class master_mage_pilkim:
    name = 'Master-Mage Pilkim'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['+DMG', 'Spellbreaker']
    image_path = imgs_dir + 'master_mage_pilkim.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class meline_ex:
    name = 'Meline Ex'
    guild = 'Noz'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['+DMG', 'Dodge', 'Shock']
    image_path = imgs_dir + 'meline_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mirval_ex:
    name = 'Mirval Ex'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '130'
    tags = ['+STR', 'Shield']
    image_path = imgs_dir + 'mirval_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class moira:
    name = 'Moira'
    guild = 'Noz'
    class_ = 'Marauder'
    race = 'Human'
    strength = '160'
    tags = ['+DMG', 'Dodge', 'Shock', 'Fireball']
    image_path = imgs_dir + 'moira.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class nadarya:
    name = 'Nadarya'
    guild = 'Noz'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['+DMG', 'Shock']
    image_path = imgs_dir + 'nadarya.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class naya_ex:
    name = 'Naya Ex'
    guild = 'Noz'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['+DMG', 'Dodge', 'Fireball']
    image_path = imgs_dir + 'naya_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class norya_ex:
    name = 'Norya Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '90'
    tags = ['Frostbite', 'Ice']
    image_path = imgs_dir + 'norya_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class octavia:
    name = 'Octavia'
    guild = 'Noz'
    class_ = 'Bard'
    race = 'Guemelite'
    strength = '0'
    tags = ['+DMG', 'Ice']
    image_path = imgs_dir + 'octavia.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ogmor_of_arcania_ex:
    name = 'Ogmor of Arcania Ex'
    guild = 'Noz'
    class_ = 'Mage'
    strength = '100'
    race = 'Human'
    tags = ['+DMG', 'Fireball', 'Lightning', 'Spellbreaker']
    image_path = imgs_dir + 'ogmor_of_arcania_ex.png'
    turns_texts = ['B:  Lightning 900 & DMG +90', 'Y:  2 x Spellbreaker 500 & DMG +100', 'RR:  +DMG x 2 & 3 x Fireball 500']
    turn1_d = {'cost': 'B', 'fp': {'number': 1, 'ability': 'Lightning', 'value': 900, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': '+DMG', 'operator': ':', 'value': 90, 'sign': None}}
    turn2_d = {'cost': 'Y', 'fp': {'number': 2, 'ability': 'Spellbreaker', 'value': 500, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': '+DMG', 'operator': ':', 'value': 100, 'sign': None}}
    turn3_d = {'cost': 'RR', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': '+DMG', 'operator': 'x', 'value': 2, 'sign': None}, 'sp': {'number': 3, 'ability': 'Fireball', 'value': 500, 'sign': None}}

class pamm_and_skar_ex:
    name = 'Pamm and Skar Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '40'
    tags = ['Shock', 'Ice']
    image_path = imgs_dir + 'pamm_and_skar_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class prophet_kounok:
    name = 'Prophet Kounok'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '130'
    tags = ['Rage']
    image_path = imgs_dir + 'prophet_kounok.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class selestyne_ex:
    name = 'Selestyne Ex'
    guild = 'Noz'
    class_ = 'Marauder'
    race = 'Human'
    strength = '140'
    tags = ['+STR', 'Dodge', 'Fireball']
    image_path = imgs_dir + 'selestyne_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class senya_ex:
    name = 'Senya Ex'
    guild = 'Noz'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['+DMG', 'Dodge', 'Shock']
    image_path = imgs_dir + 'senya_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class tanaer_of_arcania_ex:
    name = 'Tanaer of Arcania Ex'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Human'
    strength = '125'
    tags = ['+DMG', 'Shield', 'Shock']
    image_path = imgs_dir + 'tanaer_of_arcania_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class tel_menk:
    name = 'Tel-Menk'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '120'
    tags = ['Crit', 'Spellbreaker']
    image_path = imgs_dir + 'tel_menk.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_pythia:
    name = 'The Pythia'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['+DMG', 'Purify', 'Fireball']
    image_path = imgs_dir + 'the_pythia.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class thornroht_ex:
    name = 'Thornroht Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Golem'
    strength = '100'
    tags = ['+DMG', 'Thorn', 'Ice']
    image_path = imgs_dir + 'thornroht_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class thyonus_ex:
    name = 'Thyonus Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Human'
    strength = '90'
    tags = ['+DMG', 'Shock', 'Spellbreaker']
    image_path = imgs_dir + 'thyonus_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class vaerzar:
    name = 'Vaerzar'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Human'
    strength = '110'
    tags = ['+DMG', 'Fireball']
    image_path = imgs_dir + 'vaerzar.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class valentin_ex:
    name = 'Valentin Ex'
    guild = 'Noz'
    class_ = 'Warrior'
    strength = '140'
    race = 'Guemelite'
    tags = ['+DMG', 'Riposte', 'Shock', 'Spellbreaker']
    image_path = imgs_dir + 'valentin_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class valkyrion_ex:
    name = 'Valkyrion Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '50'
    tags = ['Dodge', 'Shock', 'Lightning']
    image_path = imgs_dir + 'valkyrion_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class vanalys_ex:
    name = 'Vanalys Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '70'
    tags = ['Fireball']
    image_path = imgs_dir + 'vanalys_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ylliana:
    name = 'Ylliana'
    guild = 'Noz'
    class_ = 'Marauder'
    race = 'Human'
    strength = '140'
    tags = ['Dodge', 'Shock', 'Fireball']
    image_path = imgs_dir + 'ylliana.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class young_pilkim_ex:
    name = 'Young Pilkim Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['Heal', 'Spellbreaker']
    image_path = imgs_dir + 'young_pilkim_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class zahal_ex:
    name = 'Zahal Ex'
    guild = 'Noz'
    class_ = 'Warrior'
    race = 'Guemelite'
    strength = '120'
    tags = ['+STR', 'Spellbreaker', 'Riposte']
    image_path = imgs_dir + 'zahal_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class zeranax_sv:
    name = 'Zeranax Sv'
    guild = 'Noz'
    class_ = 'Colossus'
    strength = '190'
    race = 'Dragon'
    tags = ['Fireball', 'Spellbreaker']
    image_path = imgs_dir + 'zeranax_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class zion_ex:
    name = 'Zion Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '120'
    tags = ['+DMG', 'Dodge', 'Ice', 'Fireball']
    image_path = imgs_dir + 'zion_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class agillian:
    name = 'Agillian'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Human'
    strength = '125'
    tags = ['Dodge', 'Shield', 'Rune']
    image_path = imgs_dir + 'agillian.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class apophe:
    name = 'Apophe'
    guild = 'Runic Legion'
    class_ = 'Bard'
    race = 'Human'
    strength = '0'
    tags = ['Heal', 'Rune', 'Spellbreaker']
    image_path = imgs_dir + 'apophe.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class astria:
    name = 'Astria'
    guild = 'Runic Legion'
    class_ = 'Priest'
    race = 'Human'
    strength = '115'
    tags = ['+DMG', 'Purify', 'Rune']
    image_path = imgs_dir + 'astria.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class bellerophus_ex:
    name = 'Bellerophus Ex'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['Shield', 'Shock', 'Bulwark', 'Rune']
    image_path = imgs_dir + 'bellerophus_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class boadicea_ex:
    name = 'Boadicea Ex'
    guild = 'Runic Legion'
    class_ = 'Priest'
    race = 'Human'
    strength = '150'
    tags = ['Shield', 'Rune', 'Smite']
    image_path = imgs_dir + 'boadicea_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class centaurus_ex:
    name = 'Centaurus Ex'
    guild = 'Runic Legion'
    class_ = 'Priest'
    race = 'Beast'
    strength = '160'
    tags = ['+STR', 'Blessing', 'Shock', 'Bulwark', 'Rune']
    image_path = imgs_dir + 'centaurus_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class centorium_aurius_ex:
    name = 'Centorium Aurius Ex'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Shield', 'Rune', 'Riposte']
    image_path = imgs_dir + 'centorium_aurius_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class coranthia_ex:
    name = 'Coranthia Ex'
    guild = 'Runic Legion'
    class_ = 'Priest'
    race = 'Human'
    strength = '170'
    tags = ['+STR', 'Rune', 'Shock', 'Bulwark']
    image_path = imgs_dir + 'coranthia_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class dalus:
    name = 'Dalus'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '100'
    tags = ['+STR', 'Crit', 'Rune', 'Riposte']
    image_path = imgs_dir + 'dalus.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class delphea_ex:
    name = 'Delphea Ex'
    guild = 'Runic Legion'
    class_ = 'Priest'
    race = 'Human'
    strength = '105'
    tags = ['Heal', 'Rune', 'Shock', 'Smite']
    image_path = imgs_dir + 'delphea_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class diktatus_ex:
    name = 'Diktatus Ex'
    guild = 'Runic Legion'
    class_ = 'Priest'
    race = 'Beast'
    strength = '160'
    tags = ['+STR', 'Rune', 'Smite']
    image_path = imgs_dir + 'diktatus_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class erine_ex:
    name = 'Erine Ex'
    guild = 'Runic Legion'
    class_ = 'Priest'
    strength = '95'
    race = 'Human'
    tags = ['Blessing', 'Bulwark', 'Purify', 'Rune', 'Shock', 'Buffer']
    image_path = imgs_dir + 'erine_ex.png'
    turns_texts = ['RY:  Bulwark := 390 & Rune 3', 'RR:  Runic Shock 1000 & all Purify 2', 'RB:  Blessing 80 & Rune 5']
    turn1_d = {'cost': 'RY', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Bulwark', 'operator': '=', 'value': 390, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Rune', 'operator': '+', 'value': 3, 'sign': None}}
    turn2_d = {'cost': 'RR', 'fp': {'number': 1, 'attribute': 'Runic', 'ability': 'Shock', 'value': 1000, 'sign': None}, 'sp': {'number': 1, 'target': {'all': True, 'opp': False, 'allspec': ''}, 'ability': 'Purify', 'value': 2, 'sign': None}}
    turn3_d = {'cost': 'RB', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Blessing', 'operator': '+', 'value': 80, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Rune', 'operator': '+', 'value': 5, 'sign': None}}

class exymos_sv:
    name = 'Exymos Sv'
    guild = 'Runic Legion'
    class_ = 'Colossus'
    race = 'Beast'
    strength = '250'
    tags = ['Rune', 'Bulwark', 'Fireball']
    image_path = imgs_dir + 'exymos_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class gorgonea_ex:
    name = 'Gorgonea Ex'
    guild = 'Runic Legion'
    class_ = 'Priest'
    race = 'Beast'
    strength = '140'
    tags = ['Dodge', 'Rune', 'Death Stare']
    image_path = imgs_dir + 'gorgonea_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class hephestos_ex:
    name = 'Hephestos Ex'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['Shield', 'Rune', 'Fireball']
    image_path = imgs_dir + 'hephestos_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class isorropia_ex:
    name = 'Isorropia Ex'
    guild = 'Runic Legion'
    class_ = 'Priest'
    race = 'Human'
    strength = '100'
    tags = ['Rune', 'Shock', 'Smite']
    image_path = imgs_dir + 'isorropia_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ixor:
    name = 'Ixor'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '120'
    tags = ['Rune', 'Shock', 'Death Stare', 'Stench']
    image_path = imgs_dir + 'ixor.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kataigidos_ex:
    name = 'Kataigidos Ex'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '130'
    tags = ['+STR', 'Rune', 'Lightning', 'Bulwark']
    image_path = imgs_dir + 'kataigidos_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kiria_of_andelerya:
    name = 'Kiria of Andelerya'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Elfine'
    strength = '110'
    tags = ['+STR', 'Lightning', 'Rune']
    image_path = imgs_dir + 'kiria_of_andelerya.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class klyklos_sv:
    name = 'Klyklos Sv'
    guild = 'Runic Legion'
    class_ = 'Colossus'
    race = 'Unknown '
    strength = '300'
    tags = ['Rune', 'Bulwark']
    image_path = imgs_dir + 'klyklos_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class korius_and_dalla_ex:
    name = 'Korius & Dalla Ex'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '120'
    tags = ['Shield', 'Rune', 'Bulwark']
    image_path = imgs_dir + 'korius_and_dalla_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class korosea_ex:
    name = 'Korosea Ex'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['Shield', 'Brave', 'Noble', 'Rune', 'Shock']
    image_path = imgs_dir + 'korosea_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lania_of_thyrs:
    name = 'Lania of Thyrs'
    guild = 'Runic Legion'
    class_ = 'Priest'
    race = 'Human'
    strength = '80'
    tags = ['Blessing', 'Purify', 'Rune', 'Shock']
    image_path = imgs_dir + 'lania_of_thyrs.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class leira_ex:
    name = 'Leira Ex'
    guild = 'Runic Legion'
    class_ = 'Priest'
    race = 'Beast'
    strength = '105'
    tags = ['Frostbite', 'Heal', 'Bulwark', 'Ice', 'Rune']
    image_path = imgs_dir + 'leira_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class leorius_ex:
    name = 'Leorius Ex'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    strength = '130'
    race = 'Human'
    tags = ['Dodge', 'Rune', 'Shock']
    image_path = imgs_dir + 'leorius_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class loquitus:
    name = 'Loquitus'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '130'
    tags = ['+STR', 'Rune', 'Bulwark']
    image_path = imgs_dir + 'loquitus.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lord_eilos:
    name = 'Lord Eilos'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['+STR', 'Rune', 'Shock']
    image_path = imgs_dir + 'lord_eilos.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lord_hares_ex:
    name = 'Lord Hares Ex'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['Berserk', 'Rune', 'Shock']
    image_path = imgs_dir + 'lord_hares_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lord_xenophon_ex:
    name = 'Lord Xenophon Ex'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '130'
    tags = ['Rage', 'Rune', 'Shock']
    image_path = imgs_dir + 'lord_xenophon_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class neixiram_ex:
    name = 'Neixiram Ex'
    guild = 'Runic Legion'
    class_ = 'Priest'
    race = 'Beast'
    strength = '145'
    tags = ['Shield', 'Smite', 'Rune']
    image_path = imgs_dir + 'neixiram_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class neptunos_ex:
    name = 'Neptunos Ex'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['Shield', 'Frostbite', 'Ice', 'Rune']
    image_path = imgs_dir + 'neptunos_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class okulus:
    name = 'Okulus'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Shield', 'Rune', 'Bulwark']
    image_path = imgs_dir + 'okulus.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class pervitine_ex:
    name = 'Pervitine Ex'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+DMG', 'Bulwark', 'Rune']
    image_path = imgs_dir + 'pervitine_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class privus:
    name = 'Privus'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '135'
    tags = ['+STR', 'Rune']
    image_path = imgs_dir + 'privus.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class pyromaque:
    name = 'Pyromaque'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '130'
    tags = ['+STR', 'Rune', 'Fireball', 'Riposte']
    image_path = imgs_dir + 'pyromaque.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sanquinam:
    name = 'Sanquinam'
    guild = 'Runic Legion'
    class_ = 'Priest'
    race = 'Human'
    strength = '170'
    tags = ['+STR', 'Purify', 'Rune', 'Smite']
    image_path = imgs_dir + 'sanquinam.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sapient:
    name = 'Sapient'
    guild = 'Runic Legion'
    class_ = 'Priest'
    race = 'Human'
    strength = '90'
    tags = ['Blessing', 'Rune', 'Shock']
    image_path = imgs_dir + 'sapient.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class thena_ex:
    name = 'Thena Ex'
    guild = 'Runic Legion'
    class_ = 'Priest'
    race = 'Guemelite'
    strength = '90'
    tags = ['+DMG', 'Purify', 'Rune', 'Spellbreaker']
    image_path = imgs_dir + 'thena_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class thorbios_ex:
    name = 'Thorbios Ex'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['+STR', 'Dodge', 'Crit', 'Shield', 'Rune', 'Shock']
    image_path = imgs_dir + 'thorbios_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class tristam:
    name = 'Tristam'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Dodge', 'Shock', 'Rune']
    image_path = imgs_dir + 'tristam.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class tuskos_ex:
    name = 'Tuskos Ex'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['+STR', 'Thorn', 'Rune']
    image_path = imgs_dir + 'tuskos_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class valerius:
    name = 'Valerius'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    strength = '130'
    race = 'Guemelite'
    tags = ['+STR', 'Riposte', 'Rune', 'Buffer']
    image_path = imgs_dir + 'valerius.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class warrior_anenka_ex:
    name = 'Warrior Anenka Ex'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Human'
    strength = '110'
    tags = ['Shield', 'Rune', 'Bulwark']
    image_path = imgs_dir + 'warrior_anenka_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class warrior_myrina:
    name = 'Warrior Myrina'
    guild = 'Runic Legion'
    class_ = 'Warrior Myrina'
    race = 'Human'
    strength = '120'
    tags = ['Shield', 'Rune']
    image_path = imgs_dir + 'warrior_myrina.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class admiral_al_kilicrew:
    name = 'Admiral Al Kilicrew'
    guild = 'Pirates'
    class_ = 'Warrior'
    strength = '130'
    race = 'Guemelite'
    tags = ['+STR', 'Blessing', 'Fireball', 'Powder']
    image_path = imgs_dir + 'admiral_al_kilicrew.png'
    turns_texts = ['RB:  Fireball 2000', 'Y:  STR +230 & opp Powder 2', 'RR:  Blessing 500 & All R->S']
    turn1_d = {'cost': 'RB', 'fp': {'number': 1, 'ability': 'Fireball', 'value': 2000, 'sign': None}, 'sp': None}
    turn2_d = {'cost': 'Y', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'STR', 'operator': '+', 'value': 230, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': True, 'allspec': ''}, 'ability': 'Powder', 'operator': '+', 'value': 2, 'sign': None}}
    turn3_d = {'cost': 'RR', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Blessing', 'operator': '+', 'value': 500, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'R->S', 'value': 'All', 'sign': None}}

class ardranis:
    name = 'Ardranis'
    guild = 'Pirates'
    class_ = 'Mage'
    race = 'Elfine'
    strength = '120'
    tags = ['Lightning']
    image_path = imgs_dir + 'ardranis.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class armada:
    name = 'Armada'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Human'
    strength = '0'
    tags = ['+STR', 'Powder']
    image_path = imgs_dir + 'armada.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class automata:
    name = 'Automata'
    guild = 'Pirates'
    class_ = 'Marauder'
    race = 'Golem'
    strength = '140'
    tags = ['+STR', 'Shock', 'Lightning', 'Powder', 'Backstab']
    image_path = imgs_dir + 'automata.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class azalys_the_widow_ex:
    name = 'Azalys the Widow Ex'
    guild = 'Pirates'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['Crit', 'Shock', 'Powder']
    image_path = imgs_dir + 'azalys_the_widow_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class balastar_ex:
    name = 'Balastar Ex'
    guild = 'Pirates'
    class_ = 'Warrior'
    strength = '130'
    race = 'Human'
    tags = ['+DMG', 'Dodge', 'Powder', 'Shield', 'Shock']
    image_path = imgs_dir + 'balastar_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class behem:
    name = 'Behem'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Golem'
    strength = '100'
    tags = ['+STR', 'Shock', 'Powder']
    image_path = imgs_dir + 'behem.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class boardatron_ex:
    name = 'Boardatron Ex'
    guild = 'Pirates'
    class_ = 'Marauder'
    race = 'Golem'
    strength = '150'
    tags = ['+STR', 'Dodge', 'Powder']
    image_path = imgs_dir + 'boardatron_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class boucan_ex:
    name = 'Boucan Ex'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '130'
    tags = ['+STR', 'Shock', 'Powder']
    image_path = imgs_dir + 'boucan_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class bragan:
    name = 'Bragan'
    guild = 'Pirates'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['Dodge', 'Powder', 'Fireball']
    image_path = imgs_dir + 'bragan.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class bramamir_ex:
    name = 'Bramamir Ex'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['Rage', 'Shock', 'Powder']
    image_path = imgs_dir + 'bramamir_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class briscar:
    name = 'Briscar'
    guild = 'Pirates'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['Berserk', 'Crit', 'Powder']
    image_path = imgs_dir + 'briscar.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class captain_al_killicrew:
    name = 'Captain Al Killicrew'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Shock', 'Powder']
    image_path = imgs_dir + 'captain_al_killicrew.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class captain_le_min_ex:
    name = 'Captain Le Min Ex'
    guild = 'Pirates'
    class_ = 'Mage'
    race = 'Human'
    strength = '50'
    tags = ['Thunderstruck', 'Lightning', 'Spellbreaker']
    image_path = imgs_dir + 'captain_le_min_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class captain_hell_ex:
    name = 'Captain Hell Ex'
    guild = 'Pirates'
    class_ = 'Marauder'
    race = 'Demon'
    strength = '150'
    tags = ['Life Drain', 'Fireball', 'Powder', '+DMG']
    image_path = imgs_dir + 'captain_hell_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class captain_olaho:
    name = 'Captain Olaho'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['+STR', 'Powder']
    image_path = imgs_dir + 'captain_olaho.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class clover_ex:
    name = 'Clover Ex'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['Shield', 'Powder', 'Rage', 'Shock']
    image_path = imgs_dir + 'clover_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class cuirassier_ex:
    name = 'Cuirassier Ex'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Golem'
    strength = '130'
    tags = ['Shield', 'Powder']
    image_path = imgs_dir + 'cuirassier_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class flammara_ex:
    name = 'Flammara Ex'
    guild = 'Pirates'
    class_ = 'Mage'
    strength = '0'
    race = 'Guemelite'
    tags = ['+DMG', 'Blessing', 'Fireball', 'Purify']
    image_path = imgs_dir + 'flammara_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class galmara_the_thief_ex:
    name = 'Galmara, the Thief Ex'
    guild = 'Pirates'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '150'
    tags = ['+STR', 'Powder', 'Backstab']
    image_path = imgs_dir + 'galmara_the_thief_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class gemineye:
    name = 'Gemineye'
    guild = 'Pirates'
    class_ = 'Marauder'
    strength = '160'
    race = 'Guemelite'
    tags = ['Backstab', 'Dodge', 'Lightning', 'Rage', 'Shock', 'Buffer']
    image_path = imgs_dir + 'gemineye.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class haidao_ex:
    name = 'Haidao Ex'
    guild = 'Pirates'
    class_ = 'Marauder'
    race = 'Human'
    strength = '160'
    tags = ['Powder', 'Fireball', '+STR']
    image_path = imgs_dir + 'haidao_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class hammerhead_ex:
    name = 'Hammerhead Ex'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '150'
    tags = ['Crit', 'Powder']
    image_path = imgs_dir + 'hammerhead_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class helena_ex:
    name = 'Helena Ex'
    guild = 'Pirates'
    class_ = 'Marauder'
    strength = '150'
    race = 'Human'
    tags = ['Backstab', 'Ice', 'Powder']
    image_path = imgs_dir + 'helena_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class hook:
    name = 'Hook'
    guild = 'Pirates'
    class_ = 'Marauder'
    strength = '170'
    race = 'Human'
    tags = ['+STR', 'Backstab', 'Powder', 'Buffer']
    image_path = imgs_dir + 'hook.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ica_rusty:
    name = 'Ica-Rusty'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Golem'
    strength = '130'
    tags = ['Lightning', '+STR', 'Shield']
    image_path = imgs_dir + 'ica_rusty.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class igni_the_filibuster_ex:
    name = 'Igni the Filibuster Ex'
    guild = 'Pirates'
    class_ = 'Marauder'
    race = 'Undead'
    strength = '160'
    tags = ['Powder', 'Fireball', '+STR']
    image_path = imgs_dir + 'igni_the_filibuster_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class jon_the_filibuster:
    name = 'Jon the Filibuster'
    guild = 'Pirates'
    class_ = 'Marauder'
    race = 'Undead'
    strength = '150'
    tags = ['+STR', 'Backstab', 'Powder']
    image_path = imgs_dir + 'jon_the_filibuster.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class josephine_ex:
    name = 'Josephine Ex'
    guild = 'Pirates'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '160'
    tags = ['Dodge', 'Lightning']
    image_path = imgs_dir + 'josephine_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class karabus_sv:
    name = 'Karabus Sv'
    guild = 'Pirates'
    class_ = 'Colossus'
    race = 'Unknown(R)'
    strength = '300'
    tags = ['Heal', 'Powder', 'Lightning']
    image_path = imgs_dir + 'karabus_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class killshot_x_5_ex:
    name = 'Killshot X-5 Ex'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Golem'
    strength = '125'
    tags = ['Dodge', 'Thunderstruck', 'Lightning']
    image_path = imgs_dir + 'killshot_x_5_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class klem_ex:
    name = 'Klem Ex'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Shield', 'Powder', 'Spellbreaker']
    image_path = imgs_dir + 'klem_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class klementine:
    name = 'Klementine'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Golem'
    strength = '130'
    tags = ['Shock', 'Powder', '+STR']
    image_path = imgs_dir + 'klementine.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lady_dynamite_ex:
    name = 'Lady Dynamite Ex'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Human'
    strength = '125'
    tags = ['+STR', 'Powder']
    image_path = imgs_dir + 'lady_dynamite_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lady_eel_ex:
    name = 'Lady Eel Ex'
    guild = 'Pirates'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['Lightning', 'Dodge']
    image_path = imgs_dir + 'lady_eel_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class leviath_r7_sv:
    name = 'Leviath R7 Sv'
    guild = 'Pirates'
    class_ = 'Colossus'
    strength = '200'
    race = 'Dragon'
    tags = ['Lightning', 'Powder', 'Shield', 'Shock']
    image_path = imgs_dir + 'leviath_r7_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lightning_beak:
    name = 'Lightning-beak'
    guild = 'Pirates'
    class_ = 'Mage'
    race = 'beast'
    strength = '100'
    tags = ['Lightning']
    image_path = imgs_dir + 'lightning_beak.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class limahong_ex:
    name = 'Limahong Ex'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Human'
    strength = '125'
    tags = ['+STR', 'Rage', 'Powder']
    image_path = imgs_dir + 'limahong_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mimik_ex:
    name = 'M.I.M.I.K. Ex'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Golem'
    strength = '120'
    tags = ['+DMG', 'Lightning', 'Mimic', 'Powder']
    image_path = imgs_dir + 'mimik_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mc_elektro:
    name = 'MC Elektro'
    guild = 'Pirates'
    class_ = 'Bard'
    race = 'Guemelite'
    strength = '0'
    tags = ['Thunderstruck', 'Lightning']
    image_path = imgs_dir + 'mc_elektro.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mc_laddie_ex:
    name = 'MC Laddie Ex'
    guild = 'Pirates'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['Shock', '+STR', 'Powder', 'Backstab']
    image_path = imgs_dir + 'mc_laddie_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class malderez:
    name = 'Malderez'
    guild = 'Pirates'
    class_ = 'Mage'
    race = 'Human'
    strength = '125'
    tags = ['Powder', 'Spellbreaker', 'Fireball', '+STR']
    image_path = imgs_dir + 'malderez.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mathurin:
    name = 'Mathurin'
    guild = 'Pirates'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['Crit', 'Backstab', 'Powder']
    image_path = imgs_dir + 'mathurin.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class meister_galene:
    name = 'Meister Galene'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Human'
    strength = '120'
    tags = ['+DMG', '+STR', 'Shield']
    image_path = imgs_dir + 'meister_galene.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mylad:
    name = 'Mylad'
    guild = 'Pirates'
    class_ = 'Mage'
    strength = '110'
    race = 'Guemelite'
    tags = ['Dodge', 'Lightning', 'Thunderstruck', 'Buffer']
    image_path = imgs_dir + 'mylad.png'
    turns_texts = ['Y:  Dodge 2 & all opp Thunderstruck 100', 'RR:  3 x Lightning 500', 'RB:  2 x Lightning 750']
    turn1_d = {'cost': 'Y', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Dodge', 'operator': '+', 'value': 2, 'sign': None}, 'sp': {'number': 1, 'target': {'all': True, 'opp': True, 'allspec': ''}, 'ability': 'Thunderstruck', 'operator': '+', 'value': 100, 'sign': None}}
    turn2_d = {'cost': 'RR', 'fp': {'number': 3, 'ability': 'Lightning', 'value': 500, 'sign': None}, 'sp': None}
    turn3_d = {'cost': 'RB', 'fp': {'number': 2, 'ability': 'Lightning', 'value': 750, 'sign': None}, 'sp': None}

class nut:
    name = 'Nut'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Golem'
    strength = '110'
    tags = ['Shock', 'Lightning']
    image_path = imgs_dir + 'nut.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class okto_ex:
    name = 'Okto Ex'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '80'
    tags = ['+STR', 'Powder']
    image_path = imgs_dir + 'okto_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class phylliakant_ex:
    name = 'Phylliakant Ex'
    guild = 'Pirates'
    class_ = 'Marauder'
    race = 'Undead'
    strength = '150'
    tags = ['Dodge', 'Powder', 'Strength Drain']
    image_path = imgs_dir + 'phylliakant_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class poukos:
    name = 'Poukos'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Beast'
    strength = '130'
    tags = ['+STR', 'Powder']
    image_path = imgs_dir + 'poukos.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class raveneau:
    name = 'Raveneau'
    guild = 'Pirates'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['Shock', 'Powder', 'Crit']
    image_path = imgs_dir + 'raveneau.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sarah:
    name = 'S.A.R.A.H'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Golem'
    strength = '130'
    tags = ['Lightning', 'Powder', 'Shock']
    image_path = imgs_dir + 'sarah.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class souchi:
    name = 'Souchi'
    guild = 'Pirates'
    class_ = 'Marauder'
    race = 'Human'
    strength = '140'
    tags = ['Powder', 'Stench']
    image_path = imgs_dir + 'souchi.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sybelle_ex:
    name = 'Sybelle Ex'
    guild = 'Pirates'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['Thunderstruck', 'Fireball']
    image_path = imgs_dir + 'sybelle_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class syd_ironhand:
    name = 'Syd Ironhand'
    guild = 'Pirates'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['Powder', 'Berserk']
    image_path = imgs_dir + 'syd_ironhand.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_cleaner_ex:
    name = 'The Cleaner Ex'
    guild = 'Pirates'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['+STR', 'Dodge', 'Powder']
    image_path = imgs_dir + 'the_cleaner_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_marquis:
    name = 'The Marquis'
    guild = 'Pirates'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['+STR', 'Lightning', 'Powder', 'Fireball', 'Terror']
    image_path = imgs_dir + 'the_marquis.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_ugly_corc:
    name = 'The Ugly Corc'
    guild = 'Pirates'
    class_ = 'Mage'
    race = 'Human'
    strength = '90'
    tags = ['Shield', 'Lightning']
    image_path = imgs_dir + 'the_ugly_corc.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class trumpurr_ex:
    name = 'Trumpurr Ex'
    guild = 'Pirates'
    class_ = 'Bard'
    race = 'Beast'
    strength = '0'
    tags = ['+DMG', 'Spellbreaker']
    image_path = imgs_dir + 'trumpurr_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class tryx_ex:
    name = 'Tryx Ex'
    guild = 'Pirates'
    class_ = 'Mage'
    race = 'Golem'
    strength = '100'
    tags = ['+STR', 'Thunderstruck', 'Lightning', 'Powder']
    image_path = imgs_dir + 'tryx_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class virgil_ex:
    name = 'Virgil Ex'
    guild = 'Pirates'
    class_ = 'Mage'
    strength = '120'
    race = 'Human'
    tags = ['Lightning', 'Thunderstruck']
    image_path = imgs_dir + 'virgil_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class volturia_ex:
    name = 'Volturia Ex'
    guild = 'Pirates'
    class_ = 'Mage'
    race = 'Golem'
    strength = '120'
    tags = ['Shield', 'Lightning', '+STR']
    image_path = imgs_dir + 'volturia_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class von_blaztnin_ex:
    name = 'Von Blaztnin Ex'
    guild = 'Pirates'
    class_ = 'Mage'
    race = 'Human'
    strength = '90'
    tags = ['Lightning', 'Fireball']
    image_path = imgs_dir + 'von_blaztnin_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class watahata:
    name = 'Watahata Ex'
    guild = 'Pirates'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['Lightning', 'Life Drain', 'Strength Drain']
    image_path = imgs_dir + 'watahata.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class chroneon_sv:
    name = 'Chroneon Sv'
    guild = 'Tempus'
    class_ = 'Colossus'
    race = 'Unknown(R)'
    strength = '255'
    tags = ['+DMG', 'Backstab', 'Portal']
    image_path = imgs_dir + 'chroneon_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class doloreann:
    name = 'Doloreann'
    guild = 'Tempus'
    class_ = 'Mage'
    race = 'Human'
    strength = '90'
    tags = ['Fireball', 'Portal']
    image_path = imgs_dir + 'doloreann.png'
    turns_texts = ['R:  Fireball 300', 'RRB:  2 x Portal 500', 'RY:  6 x Hit 150']
    turn1_d = {'cost': 'R', 'fp': {'number': 1, 'ability': 'Fireball', 'value': 300, 'sign': None}, 'sp': None}
    turn2_d = {'cost': 'RRB', 'fp': {'number': 2, 'ability': 'Portal', 'value': 500, 'sign': None}, 'sp': None}
    turn3_d = {'cost': 'RY', 'fp': {'number': 6, 'ability': 'Hit', 'value': 150, 'sign': None}, 'sp': None}

class elysia:
    name = 'Elysia'
    guild = 'Tempus'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '90'
    tags = ['Shield', 'Shock', 'Portal']
    image_path = imgs_dir + 'elysia.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class gatenick_ex:
    name = 'Gatenick Ex'
    guild = 'Tempus'
    class_ = 'Mage'
    race = 'Human'
    strength = '90'
    tags = ['Shock', 'Lightning', 'Spellbreaker', 'Portal']
    image_path = imgs_dir + 'gatenick_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ilfana_ex:
    name = 'Ilfana Ex'
    guild = 'Tempus'
    class_ = 'Mage'
    strength = '100'
    race = 'Human'
    tags = ['Brave', 'Deja vu', 'Dodge', 'Fireball', 'Noble', 'Portal', 'Shock', 'Spellbreaker']
    image_path = imgs_dir + 'ilfana_ex.png'
    turns_texts = ['RR:  Deja vu & 2 x Spellbreaker 750', 'RY:  Brave Portal 1200 & Fireball 600', 'B:  Noble Shock 1200 & Dodge 2']
    turn1_d = {'cost': 'RR', 'fp': {'number': 1, 'ability': 'Deja vu', 'sign': None}, 'sp': {'number': 2, 'ability': 'Spellbreaker', 'value': 750, 'sign': None}}
    turn2_d = {'cost': 'RY', 'fp': {'number': 1, 'attribute': 'Brave', 'ability': 'Portal', 'value': 1200, 'sign': None}, 'sp': {'number': 1, 'ability': 'Fireball', 'value': 600, 'sign': None}}
    turn3_d = {'cost': 'B', 'fp': {'number': 1, 'attribute': 'Noble', 'ability': 'Shock', 'value': 1200, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Dodge', 'operator': '+', 'value': 2, 'sign': None}}

class lady_of_destiny_ex:
    name = 'Lady of Destiny Ex'
    guild = 'Tempus'
    class_ = 'Priest'
    race = 'Guemelite'
    strength = '100'
    tags = ['Heal', 'Shock', 'Portal']
    image_path = imgs_dir + 'lady_of_destiny_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lord_tempus_ex:
    name = 'Lord Tempus Ex'
    guild = 'Tempus'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['Heal', 'Deja vu', 'Shock']
    image_path = imgs_dir + 'lord_tempus_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class paradoxia_ex:
    name = 'Paradoxia Ex'
    guild = 'Tempus'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['Deja vu', 'Spellbreaker']
    image_path = imgs_dir + 'paradoxia_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_announcer:
    name = 'The Announcer'
    guild = 'Tempus'
    class_ = 'Priest'
    race = 'Guemelite'
    strength = '145'
    tags = ['Blessing', 'Deja vu', 'Shock', 'Smite']
    image_path = imgs_dir + 'the_announcer.png'
    turns_texts = ['RY:  Deja vu & All Y->S', 'R:  Hit 300 & Blessing 50', 'RB:  Shock 500 & Smite 1']
    turn1_d = {'cost': 'RY', 'fp': {'number': 1, 'ability': 'Deja vu', 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Y->S', 'value': 'All', 'sign': None}}
    turn2_d = {'cost': 'R', 'fp': {'number': 1, 'ability': 'Hit', 'value': 300, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Blessing', 'operator': '+', 'value': 50, 'sign': None}}
    turn3_d = {'cost': 'RB', 'fp': {'number': 1, 'ability': 'Shock', 'value': 500, 'sign': None}, 'sp': {'number': 1, 'ability': 'Smite', 'value': 1, 'sign': None}}

class the_eternal:
    name = 'The Eternal'
    guild = 'Tempus'
    class_ = 'Unknown(C)'
    race = 'Guemelite'
    strength = '150'
    tags = ['+DMG', 'Dodge', 'Deja vu', 'Shock']
    image_path = imgs_dir + 'the_eternal.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_jailer:
    name = 'The Jailer'
    guild = 'Tempus'
    class_ = 'Priest'
    race = 'Guemelite'
    strength = '150'
    tags = ['+STR', 'Blessing', 'Portal', 'Riposte']
    image_path = imgs_dir + 'the_jailer.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_observer:
    name = 'The Observer'
    guild = 'Tempus'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '90'
    tags = ['+DMG', 'Deja vu', 'Death Stare']
    image_path = imgs_dir + 'the_observer.png'
    turns_texts = ['RY:  Death Stare 1000 & DMG +20', 'RB:  Deja vu & DMG +50', 'R:  3 x Hit 150']
    turn1_d = {'cost': 'RY', 'fp': {'number': 1, 'ability': 'Death Stare', 'value': 1000, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': '+DMG', 'operator': ':', 'value': 20, 'sign': None}}
    turn2_d = {'cost': 'RB', 'fp': {'number': 1, 'ability': 'Deja vu', 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': '+DMG', 'operator': ':', 'value': 50, 'sign': None}}
    turn3_d = {'cost': 'R', 'fp': {'number': 3, 'ability': 'Hit', 'value': 150, 'sign': None}, 'sp': None}

class the_watchmaker_ex:
    name = 'The Watchmaker Ex'
    guild = 'Tempus'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '100'
    tags = ['Crit', 'Shield', 'Deja vu', 'Spellbreaker', 'Fireball']
    image_path = imgs_dir + 'the_watchmaker_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class waliwaktu_sv:
    name = 'Waliwaktu Sv'
    guild = 'Tempus'
    class_ = 'Colossus'
    race = 'Beast'
    strength = '200'
    tags = ['+STR', 'Rage', 'Berserk', 'Portal']
    image_path = imgs_dir + 'waliwaktu_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class bitterness_ex:
    name = 'Bitterness Ex'
    guild = 'Nehantists'
    class_ = 'Warrior'
    strength = '120'
    race = 'Demon'
    tags = ['+DMG', 'Fireball', 'Rage']
    image_path = imgs_dir + 'bitterness_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_guardian:
    name = 'The Guardian'
    guild = 'Tempus'
    class_ = 'Unknown(C)'
    strength = '0'
    race = 'Golem'
    tags = ['+DMG', 'Crit', 'Deja vu', 'Shield']
    image_path = imgs_dir + 'the_guardian.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class kiirome_ex:
    name = 'Kiirome Ex'
    guild = 'Kotobas'
    class_ = 'Marauder'
    strength = '175'
    race = 'Guemelite'
    tags = ['+STR', 'Backstab', 'Shock']
    image_path = imgs_dir + 'kiirome_ex.png'
    turns_texts = ['B:  Backstab 4 x STR & B->S', 'R:  STR +185, - opp STR', 'RY:  Shock 4 x STR']
    turn1_d = {'cost': 'B', 'fp': {'number': 1, 'ability': 'Backstab', 'value': 4, 'mult_opp': False, 'mult': 'STR', 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'B->S', 'value': 1, 'sign': None}}
    turn2_d = {'cost': 'R', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'STR', 'operator': '+', 'value': 185, 'sign': '+', 'addvalue': -1, 'incr_opp': True, 'addability': 'STR'}, 'sp': None}
    turn3_d = {'cost': 'RY', 'fp': {'number': 1, 'ability': 'Shock', 'value': 4, 'mult_opp': False, 'mult': 'STR', 'sign': None}, 'sp': None}

class the_bomb_ex:
    name = 'The Bomb Ex'
    guild = 'Pirates'
    class_ = 'Marauder'
    strength = '200'
    race = 'Golem'
    tags = ['Fireball', 'Lightning', 'Powder']
    image_path = imgs_dir + 'the_bomb_ex.png'
    turns_texts = ['RY:  Fireball 1000, +500 x Golem ally', 'R:  opp Powder 1 & 0 Y->S', 'RB:  Lightning 950 x opp Powder']
    turn1_d = {'cost': 'RY', 'fp': {'number': 1, 'ability': 'Fireball', 'value': 1000, 'sign': '+', 'addvalue': 500, 'incr_opp': False, 'addability': 'Golem'}, 'sp': None}
    turn2_d = {'cost': 'R', 'fp': {'number': 1, 'target': {'all': False, 'opp': True, 'allspec': ''}, 'ability': 'Powder', 'operator': '+', 'value': 1, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Y->S', 'value': 0, 'sign': None}}
    turn3_d = {'cost': 'RB', 'fp': {'number': 1, 'ability': 'Lightning', 'value': 950, 'mult_opp': True, 'mult': 'Powder', 'sign': None}, 'sp': None}

class luminia_ex:
    name = 'Luminia Ex'
    guild = 'Mercenaries'
    class_ = 'Priest'
    strength = '100'
    race = 'Solarian'
    tags = ['Blessing', 'Purify', 'Shock', 'Smite']
    image_path = imgs_dir + 'luminia_ex.png'
    turns_texts = ['R:  Purify 1 & Blessing 160', 'RY:  3 x Shock 650', 'RB:  Shock 1400 & 2 x Smite 2']
    turn1_d = {'cost': 'R', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Purify', 'value': 1, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Blessing', 'operator': '+', 'value': 160, 'sign': None}}
    turn2_d = {'cost': 'RY', 'fp': {'number': 3, 'ability': 'Shock', 'value': 650, 'sign': None}, 'sp': None}
    turn3_d = {'cost': 'RB', 'fp': {'number': 1, 'ability': 'Shock', 'value': 1400, 'sign': None}, 'sp': {'number': 2, 'ability': 'Smite', 'value': 2, 'sign': None}}

class arpelia_ex:
    name = 'Arpelia Ex'
    guild = 'Pirates'
    class_ = 'Marauder'
    strength = '150'
    race = 'Elfine'
    tags = ['+DMG', '+STR', 'Fireball', 'Powder']
    image_path = imgs_dir + 'arpelia_ex.png'
    turns_texts = ['R:  STR +100 & opp Powder 2', 'B:  3 x Physical Attack & DMG +130', 'RY:  5 x Fireball 300 & R->S']
    turn1_d = {'cost': 'R', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'STR', 'operator': '+', 'value': 100, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': True, 'allspec': ''}, 'ability': 'Powder', 'operator': '+', 'value': 2, 'sign': None}}
    turn2_d = {'cost': 'B', 'fp': {'number': 3, 'ability': 'Physical Attack', 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': '+DMG', 'operator': ':', 'value': 130, 'sign': None}}
    turn3_d = {'cost': 'RY', 'fp': {'number': 5, 'ability': 'Fireball', 'value': 300, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'R->S', 'value': 1, 'sign': None}}

class rainspeaker_ex:
    name = 'Rainspeaker Ex'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    strength = '60'
    race = 'Beast'
    tags = ['+DMG', 'Blessing', 'Purify', 'Shock', 'Smite']
    image_path = imgs_dir + 'rainspeaker_ex.png'
    turns_texts = ['RR:  Shock 1500 & Blessing 150', 'Y:  +DMG 2 x -DMG & 2 x Smite 1', 'RB:  5 x Hit 400 & Purify 2']
    turn1_d = {'cost': 'RR', 'fp': {'number': 1, 'ability': 'Shock', 'value': 1500, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Blessing', 'operator': '+', 'value': 150, 'sign': None}}
    turn2_d = {'cost': 'Y', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': '+DMG', 'operator': ':', 'value': 2, 'mult_opp': False, 'mult': '-DMG', 'sign': None}, 'sp': {'number': 2, 'ability': 'Smite', 'value': 1, 'sign': None}}
    turn3_d = {'cost': 'RB', 'fp': {'number': 5, 'ability': 'Hit', 'value': 400, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Purify', 'value': 2, 'sign': None}}

class rany:
    name = 'Rany'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Human'
    strength = '175'
    tags = ['+STR', 'Dodge', 'Eclipse', 'Riposte', 'Shock']
    image_path = imgs_dir + 'rany.png'
    turns_texts = ['R:  Riposte 3 & opp Eclipse 3', 'RB:  Shock 300 x Riposte & STR x 2', 'RY:  Hit 300 x opp Eclipse & Dodge 2']
    turn1_d = {'cost': 'R', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Riposte', 'operator': '+', 'value': 3, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': True, 'allspec': ''}, 'ability': 'Eclipse', 'operator': '+', 'value': 3, 'sign': None}}
    turn2_d = {'cost': 'RB', 'fp': {'number': 1, 'ability': 'Shock', 'value': 300, 'mult_opp': False, 'mult': 'Riposte', 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'STR', 'operator': 'x', 'value': 2, 'sign': None}}
    turn3_d = {'cost': 'RY', 'fp': {'number': 1, 'ability': 'Hit', 'value': 300, 'mult_opp': True, 'mult': 'Eclipse', 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Dodge', 'operator': '+', 'value': 2, 'sign': None}}

class akutsai_ex:
    name = 'Akutsai Ex'
    guild = 'Kotobas'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '150'
    tags = ['Fireball', 'Heal', 'Shock']
    image_path = imgs_dir + 'akutsai_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class ermine_ex:
    name = 'Ermine Ex'
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = 'Beast'
    strength = '100'
    tags = ['Dodge', 'Shield', 'Spellbreaker']
    image_path = imgs_dir + 'ermine_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class living_fire_ex:
    name = 'Living Fire Ex'
    guild = 'Nehantists'
    class_ = 'Warrior'
    race = 'Demon'
    strength = '150'
    tags = ['-DMG', 'Crit', 'Fireball']
    image_path = imgs_dir + 'living_fire_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class erevent_ex:
    name = 'Erevent Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['Fireball', 'Shock', 'Spellbreaker']
    image_path = imgs_dir + 'erevent_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class hu_ex:
    name = 'Hu Ex'
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '160'
    tags = ['+DMG', 'Backstab', 'Rage', 'Spellbreaker']
    image_path = imgs_dir + 'hu_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class shadyja_ex:
    name = 'Shadyja Ex'
    guild = 'Zil Warriors'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '110'
    tags = ['+DMG', 'Fireball', 'Mimic', 'Scarab', 'Terror']
    image_path = imgs_dir + 'shadyja_ex.png'
    turns_texts = ['BY:  Mimic 400 & Scarab 2', 'R:  Fireball 400 & opp Terror 20', 'RB:  DMG +200 & Fireball 800']
    turn1_d = {'cost': 'BY', 'fp': {'number': 1, 'ability': 'Mimic', 'value': 400, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': 'Scarab', 'operator': '+', 'value': 2, 'sign': None}}
    turn2_d = {'cost': 'R', 'fp': {'number': 1, 'ability': 'Fireball', 'value': 400, 'sign': None}, 'sp': {'number': 1, 'target': {'all': False, 'opp': True, 'allspec': ''}, 'ability': 'Terror', 'operator': '+', 'value': 20, 'sign': None}}
    turn3_d = {'cost': 'RB', 'fp': {'number': 1, 'target': {'all': False, 'opp': False, 'allspec': ''}, 'ability': '+DMG', 'operator': ':', 'value': 200, 'sign': None}, 'sp': {'number': 1, 'ability': 'Fireball', 'value': 800, 'sign': None}}

class brutal_hares:
    name = 'Brutal Hares'
    guild = 'Runic Legion'
    class_ = 'Warrior'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Bulwark', 'Rune']
    image_path = imgs_dir + 'brutal_hares.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class pan_ex:
    name = 'Pan Ex'
    guild = 'Runic Legion'
    class_ = 'Priest'
    race = 'Beast'
    strength = '100'
    tags = ['Heal', 'Mimic', 'Rune', 'Shock']
    image_path = imgs_dir + 'pan_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mouseketeer_ex:
    name = 'Mouseketeer Ex'
    guild = 'Mercenaries'
    class_ = 'Berserker'
    race = 'Beast'
    strength = '140'
    tags = ['Backstab', 'Berserk', 'Dodge', 'Rage']
    image_path = imgs_dir + 'mouseketeer_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class malandrin_ex:
    name = 'Malandrin Ex'
    guild = 'Mercenaries'
    class_ = 'Marauder'
    race = 'Human'
    strength = '160'
    tags = ['+DMG', 'Backstab', 'Crit', 'Dodge']
    image_path = imgs_dir + 'malandrin_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class gwalchaved_ex:
    name = 'Gwalchaved Ex'
    guild = 'Avalonians'
    class_ = 'Warrior'
    race = 'Human'
    strength = '150'
    tags = ['+STR', 'Noble', 'Shield', 'Shock']
    image_path = imgs_dir + 'gwalchaved_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class zharmon_ex:
    name = 'Zharmon Ex'
    guild = 'Avalonians'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['+DMG', 'Brave', 'Fireball', 'Noble', 'Spellbreaker']
    image_path = imgs_dir + 'zharmon_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class cryo_ex:
    name = 'Cryo Ex'
    guild = 'Winter Tribes'
    class_ = 'Mage'
    race = 'Ice Elf'
    strength = '120'
    tags = ['Blizzard', 'Dodge', 'Ice', 'Shock', 'Spellbreaker']
    image_path = imgs_dir + 'cryo_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class krampus_ex:
    name = 'Krampus Ex'
    guild = 'Winter Tribes'
    class_ = 'Berserker'
    race = 'Demon'
    strength = '160'
    tags = ['+STR', '-DMG', 'Backstab', 'Ice', 'Spellbreaker']
    image_path = imgs_dir + 'krampus_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class asmoroth_guardian_sv:
    name = 'Asmoroth Guardian Sv'
    guild = 'Nehantists'
    class_ = 'Marauder'
    race = 'Demon'
    strength = '150'
    tags = ['-DMG', 'Fireball']
    image_path = imgs_dir + 'asmoroth_guardian_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class skor_shi_guardian_sv:
    name = "Skor'shi Guardian Sv"
    guild = 'Zil Warriors'
    class_ = 'Marauder'
    race = 'Guemelite'
    strength = '170'
    tags = ['Backstab', 'Dodge']
    image_path = imgs_dir + 'skor_shi_guardian_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class katchu_taoa_guardian_sv:
    name = "Katchu'taoa Guardian Sv"
    guild = 'Sap Hearts'
    class_ = 'Mage'
    race = 'Dais'
    strength = '100'
    tags = ['Fireball', 'Heal', 'Thorn']
    image_path = imgs_dir + 'katchu_taoa_guardian_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class dahre_ma_guardian_sv:
    name = "Dahre'ma Guardian Sv"
    guild = 'Desert Nomads'
    class_ = 'Priest'
    race = 'Solarian'
    strength = '150'
    tags = ['Blessing', 'Shock', 'Smite']
    image_path = imgs_dir + 'dahre_ma_guardian_sv.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class bumbaxt_ex:
    name = 'Bumbaxt Ex'
    guild = 'Avalonians'
    class_ = 'Warrior'
    race = 'Human'
    strength = '500'
    tags = ['+STR', 'Noble', 'Riposte', 'Shock']
    image_path = imgs_dir + 'bumbaxt_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class nailing_ex:
    name = 'Nailing Ex'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Human'
    strength = '150'
    tags = ['+STR', 'Crit', 'Spellbreaker']
    image_path = imgs_dir + 'nailing_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class andria_ex:
    name = 'Andria Ex'
    guild = 'Sap Hearts'
    class_ = 'Marauder'
    race = 'Elfine'
    strength = '150'
    tags = ['+STR', 'Backstab', 'Dodge', 'Thorn']
    image_path = imgs_dir + 'andria_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class sirck_ex:
    name = 'Sirck Ex'
    guild = 'Zil Warriors'
    class_ = 'Priest'
    race = 'Beast'
    strength = '105'
    tags = ['Crit', 'Deja vu', 'Dodge', 'Life Drain']
    image_path = imgs_dir + 'sirck_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class a_the_illusionist_ex:
    name = 'A. The Illusionist Ex'
    guild = 'Zil Warriors'
    class_ = 'Mage'
    race = 'Guemelite'
    strength = '125'
    tags = ['Fireball', 'Mimic', 'Spellbreaker', 'Terror']
    image_path = imgs_dir + 'a_the_illusionist_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class fraxine_ex:
    name = 'fraxine Ex'
    guild = 'Sap Hearts'
    class_ = 'Marauder'
    race = 'Elfine'
    strength = '175'
    tags = ['+STR', 'Berserk', 'Dodge']
    image_path = imgs_dir + 'fraxine_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class gyrdan_ex:
    name = 'Gyrdan Ex'
    guild = 'Noz'
    class_ = 'Mage'
    race = 'Human'
    strength = '100'
    tags = ['-DMG', 'Fireball', 'Lightning', 'Thunderstruck']
    image_path = imgs_dir + 'gyrdan_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class camel_ex:
    name = 'Camel Ex'
    guild = 'Desert Nomads'
    class_ = 'Marauder'
    race = 'Beast'
    strength = '180'
    tags = ['Crit', 'Rage', 'Resil', 'Stench']
    image_path = imgs_dir + 'camel_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class wells_ex:
    name = 'Wells Ex'
    guild = 'Tempus'
    class_ = 'Mage'
    race = 'Human'
    strength = '110'
    tags = ['+DMG', 'Deja vu', 'Portal', 'Purify']
    image_path = imgs_dir + 'wells_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mystic_hunter_ex:
    name = 'Mystic-Hunter Ex'
    guild = 'Mercenaries'
    class_ = 'Marauder'
    race = 'Unknown(R)'
    strength = '175'
    tags = ['Crit', 'Dodge', 'Lightning']
    image_path = imgs_dir + 'mystic_hunter_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class prince_vahn_ex:
    name = 'Prince Vahn Ex'
    guild = 'Avalonians'
    class_ = 'Priest'
    race = 'Human'
    strength = '130'
    tags = ['+STR', 'Blessing', 'Noble', 'Smite', 'Buffer']
    image_path = imgs_dir + 'prince_vahn_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class astryd_ex:
    name = 'Astryd Ex'
    guild = 'Mercenaries'
    class_ = 'Priest'
    race = 'Human'
    strength = '112'
    tags = ['Blessing', 'Heal', 'Resil', 'Shock', 'Buffer']
    image_path = imgs_dir + 'astryd_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class foam_giant_ex:
    name = 'foam Giant Ex'
    guild = 'Mercenaries'
    class_ = 'Warrior'
    race = 'Golem'
    strength = '200'
    tags = ['+STR', 'Shield']
    image_path = imgs_dir + 'foam_giant_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class penelopia_ex:
    name = 'Penelopia Ex'
    guild = 'Runic Legion'
    class_ = 'Priest'
    race = 'Human'
    strength = '80'
    tags = ['Purify', 'Rune', 'Shock', 'Smite']
    image_path = imgs_dir + 'penelopia_ex.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class aleshane_ev:
    name = 'Aleshane Ev'
    guild = 'Sap Hearts'
    class_ = 'Marauder'
    race = 'Elfine'
    strength = '175'
    tags = ['+STR', 'Backstab', 'Crit']
    image_path = imgs_dir + 'aleshane_ev.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class mei_li_ev:
    name = 'Mei-Li Ev'
    guild = 'Kotobas'
    class_ = 'Marauder'
    race = 'Human'
    strength = '175'
    tags = ['+STR', 'Dodge']
    image_path = imgs_dir + 'mei_li_ev.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_psychurgist_ev:
    name = 'The Psychurgist Ev'
    guild = 'Zil Warriors'
    class_ = 'Priest'
    race = 'Guemelite'
    strength = '115'
    tags = ['Fireball', 'Lightning', 'Mimic', 'Shock']
    image_path = imgs_dir + 'the_psychurgist_ev.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class the_receptacle_ev:
    name = 'The Receptacle Ev'
    guild = 'Nehantists'
    class_ = 'Mage'
    race = 'Demon'
    strength = '75'
    tags = ['-DMG', 'Dodge', 'Fireball', 'Shock']
    image_path = imgs_dir + 'the_receptacle_ev.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

class lynus_ex:
    name = 'Lynus Ex'
    guild = 'Pirates'
    class_ = 'Mage'
    race = 'Human'
    strength = '85'
    tags = ['Lightning']
    image_path = imgs_dir + 'lynus_ex.png'
    turns_texts = ['RY:  Lightning 1600', 'R:  2 x Lightning 400, 800 VS Beast', 'RB:  Lightning 3 x opp Thunderstruck']
    turn1_d = {'cost': 'RY', 'fp': {'number': 1, 'ability': 'Lightning', 'value': 1600, 'sign': None}, 'sp': None}
    turn2_d = {'cost': 'R', 'fp': {'number': 2, 'ability': 'Lightning', 'value': 400, 'sign': ',', 'condition': 'VS', 'addvalue': 800, 'addability': 'Beast'}, 'sp': None}
    turn3_d = {'cost': 'RB', 'fp': {'number': 1, 'ability': 'Lightning', 'value': 3, 'mult_opp': True, 'mult': 'Thunderstruck', 'sign': None}, 'sp': None}

class doloreann_ev:
    name = 'Doloreann Ev'
    guild = 'Tempus'
    class_ = 'Mage'
    race = 'Human'
    strength = '90'
    tags = []
    image_path = imgs_dir + 'doloreann_ev.png'
    turns_texts = []
    turn1_d = {}
    turn2_d = {}
    turn3_d = {}

