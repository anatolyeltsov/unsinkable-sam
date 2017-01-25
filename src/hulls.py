# moved these out of ship.py to stop it geting bloated
# tried them as a module in their own dir, but that's overkill

class Hull(object):
    # base for rudimentary classes to hold hull properties for a ship
    # there's only instance of each, so I just used class properties...boilerplate reduced to minimum eh :)
    size_class = 'Define in subclass'
    # length
    # hull spritesheet file
    # vertical offset if needed, accounting for buy menu especially
    # mask_name
    # effects position
    # fatter / thinner ships might need offset adjustments
    print("HULL")

    def __init__(self):
        print("__init__")

    @property
    def spritesheet_name(self):
        return self.size_class +  '_' + self.hull_type + '_house_' + self.house_position

    @property
    def mask_name(self):
        return self.hull_type + '_' + self.size_class + '_hull_mask'

    @property
    def wake_name(self):
        return self.hull_type + '_' + self.size_class + '_wake'


class LargeShipHouseRear(Hull):
    def __init__(self):
        self.size_class = 'large'
        self.hull_type = 'ship'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 1), ('full_load', 3)]


class LargeShipHouseForward(Hull):
    def __init__(self):
        self.size_class = 'large'
        self.hull_type = 'ship'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 1), ('full_load', 3)]


class LargeRiverboatHouseRear(Hull):
    def __init__(self):
        self.size_class = 'large'
        self.hull_type = 'riverboat'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]


class SmallRiverboatHouseRear(Hull):
    def __init__(self):
        self.size_class = 'small'
        self.hull_type = 'riverboat'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]


class SmallShipHouseRear(Hull):
    def __init__(self):
        self.size_class = 'small'
        self.hull_type = 'ship'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]


class TempMini(Hull):
    def __init__(self):
        self.size_class = 'mini'
        self.hull_type = 'ship'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]


class TempMicro(Hull):
    def __init__(self):
        self.size_class = 'micro'
        self.hull_type = 'ship'
        self.house_position = 'rear'
        self.load_state_y_offsets = [('empty', -1), ('part_load', 0), ('full_load', 1)]


registered_hulls = {'LargeRiverboatHouseRear': LargeRiverboatHouseRear(),
                    'LargeShipHouseForward': LargeShipHouseForward(),
                    'LargeShipHouseRear': LargeShipHouseRear(),
                    'SmallRiverboatHouseRear': SmallRiverboatHouseRear(),
                    'SmallShipHouseRear': SmallShipHouseRear(),
                    'TempMini': TempMini(),
                    'TempMicro': TempMicro()}
