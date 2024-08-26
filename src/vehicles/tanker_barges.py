from ship import TankerBarge


def main():
    ship = TankerBarge(
        numeric_id=980,
        name="Walney",
        gen=3,
        subtype="C",
        hull="BargeHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = TankerBarge(
        numeric_id=400,
        name="Durance",
        gen=3,
        subtype="D",
        hull="BargeHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = TankerBarge(
        numeric_id=490,
        name="Notto",
        gen=3,
        subtype="E",
        hull="BargeHouseRear",
        str_type_info="SMALL_TANKER_COASTAL_INLAND",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = TankerBarge(
        numeric_id=390,
        name="Columbus",
        gen=3,
        subtype="F",
        hull="BargeHouseRear",
        str_type_info="COASTAL_TANKER",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        sprites_complete=False,
    )
