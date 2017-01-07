from roster import Roster

# ships in alphabetical order
from ships import (bulk_carrier_large,
                   bulk_carrier_small,
                   edibles_tanker_large,
                   flatdeck_barge_large,
                   flatdeck_barge_small,
                   livestock_carrier_large,
                   livestock_carrier_small,
                   piece_goods_carrier_large,
                   piece_goods_carrier_small,
                   reefer_large,
                   reefer_small,
                   tanker_large,
                   tanker_small,
                   trawler_small,
                   trawler_micro,
                   trawler_mini,
                   universal_freighter_large,
                   universal_freighter_micro,
                   universal_freighter_mini,
                   universal_freighter_small)


roster = Roster(id = 'default',
                numeric_id = 1,
                freighter_speeds = {0: 20, 1950: 30},
                # ships in buy menu order
                ships = [universal_freighter_micro,
                         universal_freighter_mini,
                         universal_freighter_small,
                         universal_freighter_large,
                         piece_goods_carrier_small,
                         piece_goods_carrier_large,
                         flatdeck_barge_small,
                         flatdeck_barge_large,
                         bulk_carrier_small,
                         bulk_carrier_large,
                         tanker_small,
                         tanker_large,
                         livestock_carrier_small,
                         livestock_carrier_large,
                         reefer_small,
                         reefer_large,
                         edibles_tanker_large,
                         trawler_micro,
                         trawler_mini,
                         trawler_small])
