from ship import PaxLuxuryShip


def main():
    ship = PaxLuxuryShip(
        numeric_id=230,
        name="Bonavista",
        gen=3,
        subtype="C",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = PaxLuxuryShip(
        numeric_id=220,
        name="Zealand",
        gen=3,
        subtype="D",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )
