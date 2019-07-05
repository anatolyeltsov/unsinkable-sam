from roster import Roster

# ships in alphabetical order
from vehicles import (bulk_carrier_B,
                   bulk_carrier_C,
                   bulk_carrier_D,
                   covered_hopper_carrier_D,
                   chemicals_tanker_C,
                   chemicals_tanker_D,
                   cryo_tanker_C,
                   cryo_tanker_D,
                   edibles_tanker_C,
                   edibles_tanker_D,
                   flatdeck_barge_B,
                   flatdeck_barge_C,
                   flatdeck_barge_D,
                   fruit_veg_carrier_C,
                   fruit_veg_carrier_D,
                   livestock_carrier_C,
                   livestock_carrier_D,
                   #mail_ship_D, # no large mail ship, nonsense having so many mailbags in one vehicle
                   mail_ship_A,
                   mail_ship_B,
                   mail_ship_C,
                   pax_fast_loading_A,
                   pax_fast_loading_B,
                   pax_fast_loading_C,
                   pax_fast_loading_D,
                   pax_luxury_C,
                   pax_luxury_D,
                   piece_goods_carrier_C,
                   piece_goods_carrier_D,
                   reefer_C,
                   reefer_D,
                   #supply_vessel_C,
                   #supply_vessel_D,
                   tanker_B,
                   tanker_C,
                   tanker_D,
                   trawler_A,
                   trawler_B,
                   trawler_C,
                   universal_freighter_A,
                   universal_freighter_B,
                   universal_freighter_C,
                   universal_freighter_D)


roster = Roster(id = 'default',
                numeric_id = 1,
                speeds = {'freight': {0: 25, 1950: 35},
                          'fast_freight': {}, # unused currently
                          'pax_mail': {0: 35, 1950: 45, 1980: 70}},
                # ships in buy menu order
                ships = [pax_fast_loading_A,
                         pax_fast_loading_B,
                         pax_fast_loading_C,
                         pax_fast_loading_D,
                         pax_luxury_C,
                         pax_luxury_D,
                         mail_ship_A,
                         mail_ship_B,
                         mail_ship_C,
                         universal_freighter_A,
                         universal_freighter_B,
                         universal_freighter_C,
                         universal_freighter_D,
                         piece_goods_carrier_C,
                         piece_goods_carrier_D,
                         flatdeck_barge_B,
                         flatdeck_barge_C,
                         flatdeck_barge_D,
                         bulk_carrier_B,
                         bulk_carrier_C,
                         bulk_carrier_D,
                         tanker_B,
                         tanker_C,
                         tanker_D,
                         chemicals_tanker_C,
                         chemicals_tanker_D,
                         cryo_tanker_C,
                         cryo_tanker_D,
                         covered_hopper_carrier_D,
                         livestock_carrier_C,
                         livestock_carrier_D,
                         edibles_tanker_C,
                         edibles_tanker_D,
                         reefer_C,
                         reefer_D,
                         fruit_veg_carrier_C,
                         fruit_veg_carrier_D,
                         trawler_A,
                         trawler_B,
                         trawler_C
                         ])
