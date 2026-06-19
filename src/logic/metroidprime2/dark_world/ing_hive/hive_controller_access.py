from BaseClasses import ItemClassification, MultiWorld

from ... import (
    can_use_darkburst,
    can_use_sunburst,
    can_lay_bomb,
    can_use_screw_attack,
    has_trick_enabled,
)
from .....Enums import DoorCover
from .....Regions import MetroidPrime2Exit, MetroidPrime2Region
from .....Utils import condition_and, condition_or

class HiveControllerAccess(MetroidPrime2Region):
    name = "Hive Controller Access"
    exits = [
        MetroidPrime2Exit(
            destination="Ing Hive - Hive Energy Controller",
            door=DoorCover.Any,
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
            destination="Ing Hive - Hive Temple (South)",
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
    ]