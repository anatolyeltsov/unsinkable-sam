from ship import BulkShip


def main():
    ship = BulkShip(
        numeric_id=54,
        name="Saltlick",
        gen=3,
        subtype="C",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkShip(
        numeric_id=53,
        name="Lotsberget",
        gen=3,
        subtype="D",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkShip(
        numeric_id=51,
        name="Gravelly",
        gen=3,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkShip(
        numeric_id=50,
        name="Alligator",
        gen=3,
        subtype="F",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
