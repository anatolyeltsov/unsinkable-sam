from ship import MailShip


def main():
    ship = MailShip(
        numeric_id=280,
        name="Diamond",
        gen=3,
        subtype="A",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = MailShip(
        numeric_id=270,
        name="Delta",
        gen=3,
        subtype="B",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = MailShip(
        numeric_id=260,
        name="Olympic",
        gen=3,
        subtype="D",
        hull="TempHouseNone",
        effect_type="EFFECT_SPRITE_STEAM",
    )
