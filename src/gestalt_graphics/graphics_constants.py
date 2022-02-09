# colour defaults
CC1 = 198
CC2 = 80
house_magic_colour = 170

hull_recolour_CC1 = {
    136: CC1,
    137: CC1 + 1,
    138: CC1 + 2,
    139: CC1 + 3,
    140: CC1 + 4,
    141: CC1 + 5,
    142: CC1 + 6,
    143: CC1 + 7,
}
hull_recolour_CC2 = {
    136: CC2,
    137: CC2 + 1,
    138: CC2 + 2,
    139: CC2 + 3,
    140: CC2 + 4,
    141: CC2 + 5,
    142: CC2 + 6,
    143: CC2 + 7,
}
hull_recolour_white = {
    136: 8,
    137: 9,
    138: 10,
    139: 11,
    140: 12,
    141: 13,
    142: 14,
    143: 15,
}
hull_recolour_silver = {
    136: 16,
    137: 17,
    138: 18,
    139: 19,
    140: 20,
    141: 21,
    142: 22,
    143: 23,
}

# used because it's nicer to draw with dark red as magic colour, but it's not safe as a magic colour, so it's remapped to a spare purple range
house_make_magic_red_safe_recolour_map = {
    40: house_magic_colour,
    41: house_magic_colour + 1,
    42: house_magic_colour + 2,
    43: house_magic_colour + 3,
    44: house_magic_colour + 4,
    45: house_magic_colour + 5,
    46: house_magic_colour + 6,
    47: house_magic_colour + 7,
}
# arbitrary house recolouring maps
house_recolour_CC2_to_CC1 = {
    CC2: CC1,
    CC2 + 1: CC1 + 1,
    CC2 + 2: CC1 + 2,
    CC2 + 3: CC1 + 3,
    CC2 + 4: CC1 + 4,
    CC2 + 5: CC1 + 5,
    CC2 + 6: CC1 + 6,
    CC2 + 7: CC1 + 7,
}
house_recolour_roof_CC1_1 = {
    house_magic_colour: CC1,
    house_magic_colour + 1: CC1 + 1,
    house_magic_colour + 2: CC1 + 2,
    house_magic_colour + 3: CC1 + 3,
    house_magic_colour + 4: CC1 + 4,
    house_magic_colour + 5: CC1 + 5,
    house_magic_colour + 6: CC1 + 6,
    house_magic_colour + 7: CC1 + 7,
}
house_recolour_roof_dark_red_1 = {
    house_magic_colour: 40,
    house_magic_colour + 1: 41,
    house_magic_colour + 2: 42,
    house_magic_colour + 3: 43,
    house_magic_colour + 4: 44,
    house_magic_colour + 5: 45,
    house_magic_colour + 6: 46,
    house_magic_colour + 7: CC1 + 7,
}
house_recolour_roof_silver_1 = {
    house_magic_colour: 16,
    house_magic_colour + 1: 17,
    house_magic_colour + 2: 18,
    house_magic_colour + 3: 19,
    house_magic_colour + 4: 20,
    house_magic_colour + 5: 21,
    house_magic_colour + 6: 22,
    house_magic_colour + 7: 23,
}

# facts about 'standard' spritesheets, spritesheets varying from this will be painful
spriterow_height = 100
spritesheet_top_margin = 10
spritesheet_width = 1200

# --- Livery Recolour Maps ---- #
# label order matters, so tuples are used not dicts
# could probably have used orderedict or named tuple, but...blah

# keep cargos in alphabetical order for ease of reading
# DFLT label is a hack to provide specific livery for unknown cargos and should not be added to cargo translation table

# Containers
# !! simple recolouring, not cargo specific.  May need work ??  Could be cargo-specific??
container_recolour_maps = (
    {170 + i: CC1 + i for i in range(8)},
    {170 + i: CC2 + i for i in range(8)},
    {170 + i: 8 + i for i in range(8)},
)
