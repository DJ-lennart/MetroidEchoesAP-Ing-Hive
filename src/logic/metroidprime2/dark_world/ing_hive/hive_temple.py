from BaseClasses import ItemClassification, MultiWorld

from ... import (
    has_light_ammo,
    can_use_power_beam,
    can_use_light_beam,
    can_use_charged_power_beam,
    can_use_charged_dark_beam,
    can_use_charged_light_beam,
    can_use_charged_annihilator_beam,
    can_use_super_missile,
    can_use_darkburst,
    can_use_sunburst,
    can_use_boost_ball,
    can_use_spider_ball,
    can_lay_bomb,
    can_lay_bomb_or_pb,
    can_use_screw_attack,
    get_missile_count,
    has_dark_suit,
    has_light_suit,
    can_activate_safe_zone,
    has_trick_enabled,
)

from .....Enums import DoorCover
from .....Items import MetroidPrime2Item
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class HiveTemple(MetroidPrime2Region):
    name = "Hive Temple"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple (North)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Ing Hive - Hive Temple | Quadraxis", player),
                condition_or([
                    state.count("Energy Tank", player) >= 2,
                    has_dark_suit(state, player),
                    has_light_suit(state, player)
                ]),
                condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple | Z-Axis SA to Temple doors"),
                        can_use_screw_attack(state, player, True),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple | E-Dash to Temple Doors"),
                        state.has_all({
                            "Space Jump Boots",
                            "Scan Visor",
                        }, player),
                    ]),
                ]),
                can_use_spider_ball(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple (South)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Ing Hive - Hive Temple | Quadraxis", player),
                condition_or([
                    state.count("Energy Tank", player) >= 2,
                    has_dark_suit(state, player),
                    has_light_suit(state, player)
                ]),
                condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple | Z-Axis SA to Temple doors"),
                        can_use_screw_attack(state, player, True),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple | E-Dash to Temple Doors"),
                        state.has_all({
                            "Space Jump Boots",
                            "Scan Visor",
                        }, player),
                    ]),
                ]),
                can_use_spider_ball(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple (West)",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Ing Hive - Hive Temple | Quadraxis", player),
                condition_or([
                    state.count("Energy Tank", player) >= 2,
                    has_dark_suit(state, player),
                    has_light_suit(state, player)
                ]),
                condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple | Z-Axis SA to Temple doors"),
                        can_use_screw_attack(state, player, True),
                    ]),
                    condition_and([
                        condition_or([ #These two tricks have the same requirements but different difficulties
                            has_trick_enabled(state, player, "Ing Hive - Hive Temple | E-Dash to Temple Doors"),
                            has_trick_enabled(state, player, "Ing Hive - Hive Temple | Scan Dash to West Door"),
                        ]),
                        state.has_all({
                            "Space Jump Boots",
                            "Scan Visor",
                        }, player),
                    ]),
                ]),
                can_use_spider_ball(state, player),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple (Quadraxis)",
            door=DoorCover.Opened,
            rule=lambda state, player: quadraxis_combat_logic(state, player)
        ),
    ]

class HiveTemple_North(MetroidPrime2Region):
    name = "Hive Temple"
    desc = "North"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple",
            door=DoorCover.Opened,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple Access (Safe Zone)",
            door=DoorCover.Any,
            rule=lambda state, player: condition_or([
                can_activate_safe_zone(state, player),
                state.count("Energy Tank", player) >= 1,
                has_dark_suit(state, player),
                has_light_suit(state, player),
            ]),
        ),
    ]

class HiveTemple_South(MetroidPrime2Region):
    name = "Hive Temple"
    desc = "South"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Controller Access",
            door=DoorCover.Annihilator,
            rule=lambda state, player: condition_or([
                can_lay_bomb(state, player),
                condition_and([
                    has_trick_enabled(state, player, "Ing Hive - Hive Controller Access | Bomb Slot Without Bombs"),
                    state.has("Space Jump Boots", player),
                    condition_or([
                        can_use_darkburst(state, player),
                        can_use_sunburst(state, player),
                    ]),
                ]),
                condition_and([
                    has_trick_enabled(state, player, "Ing Hive - Hive Controller Access | Bomb Slot Without Bombs NSJ SA Standable"),
                    can_use_screw_attack(state, player, True),
                    condition_or([
                        can_use_darkburst(state, player),
                        can_use_sunburst(state, player),
                    ]),
                ]),
            ]),
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple",
            door=DoorCover.Opened,
            rule=lambda state, player: True
        ),
    ]

class HiveTemple_West(MetroidPrime2Region):
    name = "Hive Temple"
    desc = "South"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple",
            door=DoorCover.Opened,
            rule=lambda state, player: True
        ),
        MetroidPrime2Exit(
            destination="Ing Hive - Temple Security Access",
            door=DoorCover.Annihilator,
            rule=lambda state, player: condition_and([
                condition_or([
                    can_lay_bomb(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Get through with NSJ SA"),
                        can_use_screw_attack(state, player, True),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Get through with SA"),
                        can_use_screw_attack(state, player),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Get through with Wall Boosts"),
                        can_use_boost_ball(state, player)
                    ]),
                ]),
                condition_or([
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Temple Security Access with Dark Suit"),
                        has_dark_suit(state, player),
                        state.count("Energy Tank", player) >= 2
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Temple Security Access | Temple Security Access with No Suit"),
                        state.count("Energy Tank", player) >= 4
                    ]),
                    has_light_suit(state, player),
                ]),
            ]),
        ),
    ]

class HiveTemple_Quadraxis(MetroidPrime2Region):

    name = "Hive Temple"
    desc = "Quadraxis"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Temple",
            door=DoorCover.Opened,
            rule=lambda state, player: condition_and([
                state.has("Ing Hive - Hive Temple | Quadraxis", player),
                condition_or([
                    state.count("Energy Tank", player) >= 1,
                    has_dark_suit(state, player),
                    has_light_suit(state, player)
                ]),
                condition_or([
                    can_use_screw_attack(state, player),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple | Z-Axis SA to Temple doors"),
                        can_use_screw_attack(state, player, True),
                    ]),
                    condition_and([
                        has_trick_enabled(state, player, "Ing Hive - Hive Temple | E-Dash to Temple Doors"),
                        state.has_all({
                            "Space Jump Boots",
                            "Scan Visor",
                        }, player),
                    ]),
                ]),
                can_use_spider_ball(state, player),
                quadraxis_combat_logic(state, player),
            ]),
        ),
    ],



    def __init__(self, region_name: str, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)

        self.add_location(
            name="Quadraxis",
            locked_item=MetroidPrime2Item(
                name="Ing Hive - Hive Temple | Quadraxis",
                classification=ItemClassification.progression,
                code=None,
                player=player,
            ),
            can_access=lambda state, player: True,
        )
        self.add_location(
            name="Pickup (Annihilator Beam)",
            can_access=lambda state, player: state.has("Ing Hive - Hive Temple | Quadraxis", player),
        )

"""
Things needed for Quadraxis:
Morph Ball Bombs/Power Bombs
A way to beat it

Things that are usually required but can be skipped with tricks:
Echo Visor
Spider Ball
Boost Ball
Screw Attack
about 4 E-tanks with dark suit
"""

def quadraxis_combat_logic(state: CollectionState, player: int) -> bool:
    """Quadraxis has very complicated logic due to being such a late game boss in the vanilla game and not having any safe zones.
    Realistically one should be well over the requirements before one can even reach Quadraxis.
    There can however always be edge cases and future settings could change how relevant this is.
    Pickups change how the fight works a lot, but missile pickups seemed to not be guaranteed but energy pickups were plentiful."""

    if not can_lay_bomb_or_pb(state, player): return False #Is simply not possible to beat Phase 3 without this
    if not (has_dark_suit(state, player) or has_light_suit(state, player)): return False #Is its own check in case non suit logic gets added in the future
    
    skip_boost = has_trick_enabled(state, player, "Quadraxis Without Boost Ball")
    skip_echo = has_trick_enabled(state, player, "Quadraxis Without Echo Visor")
    skip_spider = has_trick_enabled(state, player, "Quadraxis Without Spider Ball")
    if not skip_boost and not can_use_boost_ball(state, player): return False
    if not skip_echo and not state.has("Echo Visor", player): return False
    if not skip_spider and not can_use_spider_ball(state, player): return False

    offence = 0
    ammunition = 0
    speed = 0
    defence = 0
    #Offence
    if can_use_charged_power_beam(state, player): 
        offence += 10
        speed += 10
    elif can_use_power_beam(state, player): offence += 1

    if not can_use_light_beam(state, player): light_ammo = 0
    elif has_light_ammo(state, player, 200): 
        light_ammo = 4 #Around 100 is required if done optimally, so 250 is basically same as 200, and even 200 is very high but could be good for less experienced players
        ammunition += 25

    elif has_light_ammo(state, player, 150): 
        light_ammo = 3
        ammunition += 20

    elif has_light_ammo(state, player, 100): 
        light_ammo = 2
        ammunition += 15
    else: 
        light_ammo = 1
        ammunition += 10


    light_beam = 0
    if can_use_charged_light_beam(state, player): 
        light_beam = 20
        speed += 10
        ammunition += 10
    elif can_use_light_beam(state, player): 
        light_beam = 20
        ammunition += 10

    offence += (light_ammo*light_beam)

    missiles = get_missile_count(state, player)
    if not state.has("Echo Visor", player): missiles = min(missiles, 150)
    offence += math.floor(missiles / 10)
    ammunition += math.floor(missiles / 10)
    if can_use_super_missile(state, player): speed += math.floor(missiles / 15)

    if ammunition < 25 and not (can_use_power_beam(state, player) or can_use_charged_power_beam(state, player)): #This checks whether there is enough ammo to beat the boss
        offence = 0

    #Defence
    if condition_or([
        can_use_charged_power_beam(state, player),
        can_use_charged_dark_beam(state, player),
        can_use_charged_light_beam(state, player),
        can_use_charged_annihilator_beam(state, player)
    ]): 
        defence += 30

    e_tanks = state.count("Energy Tank", player)
    space_jump = state.has("Space Jump Boots", player)
    dark_suit = has_dark_suit(state, player)
    light_suit = has_light_suit(state, player)
    boost = can_use_boost_ball(state, player)

    defence += e_tanks*10
    defence += int(boost)*5
    defence += int(space_jump)*5
    defence += int(light_suit)*2*e_tanks

    #Tricks
    if has_trick_enabled(state, player, "Quadraxis Screw Attack Centre Antennae"): speed += 10

    samus = offence + defence + speed

    if defence < 60: samus = 0 #This is to just set a minimum of at least 1 E-Tank with light suit and 2 with dark suit
    if offence == 0: samus = 0 #To prevent situations where if one only has dark or annihilator beam or insufficient ammunition for Quadraxis to be in logic

    quadraxis = 150

    return samus >= quadraxis


    #base power beam needs like at least 13 E-tanks with dark suit
    #Relevant tricks, P3 can be done without boost or spider, should both be separate tricks
    #P2 can do the middle thing with just SA, mostly relevant for energy tanks as the surrounding rooms use SA a lot, but tricks can bypass like all those uses
    #Charge beam you might lose around 2 E-tanks, +- depending on play, the pickups is a massive change, by this logic super missiles should maybe just be 1 E-tank just for safety
    #Base Light beam about 3 E-tanks around 100 ammo used, a bit more than 100 but a bunch could be saved so 100 should be bare minimum and anything about that should be a comfortable amount
    #Charge light beam can do 8 ammo per leg if optimal, which means first phase is 32 as opposed to 40 if you just charge light beam all legs
    #Ammo consumed about the same, a bit easier to stay around 100 but honestly ammo wise it should not be different from without charge, health wise probably also around 1-2 E-tanks, what makes it different is the ability to attract distant pickups
    #Dark beam sucks against quadraxis not even gonna consider it unless infinite, and even the single dark would probably not be logical without light suit and I'd just put charge dark as like, maybe 6 E-tanks or whatever
    #60 missiles phase 1 because god damn hitting those legs suuuuuck
    #9 missiles per antenna phase 2
    #7 missiles to stun phase 3, missiles suck
    #5 E-tanks
    #E tanks went down to like 1 used up with light suit, it would depend on how long it takes with each beam but lets say 60% of the expected health drain is from the atmosphere, rounding up
    #Light suit should probably still have 1 E-tank as a buffer regardless, let's say base power be around 6, missiles 2, light beams 1
    #So basically at optimal damage and defence, 1 E-tank as minimum unless a trick for minimal Quadraxis gets addedd where it can go down to 0
    #Annihilator can probably never realistically have enough ammo on its own and it is quite bad so no real reason to consider it
    #Two supers for just about everything
    #Base power light suit 2 E tanks P1
    #Phase 2 like an extra 3
    #Phase 3 was a cake walk, do like minimum 7 or so



#Centre platform, you can get to all the exits without screw attack if you have space jump and scan visor
#without space jump you can do a NSJ screw attack
