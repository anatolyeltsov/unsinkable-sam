import codecs  # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os

currentdir = os.curdir
from multiprocessing import Pool
import multiprocessing

logger = multiprocessing.log_to_stderr()
logger.setLevel(25)
from time import time

import unsinkable_sam
import utils
import global_constants


def run_pipeline(ship):
    if ship.gestalt_graphics.pipeline == None:
        shutil.copy(
            os.path.join(graphics_input, ship.id + ".png", graphics_output_path)
        )
    else:
        result = ship.gestalt_graphics.pipeline.render(ship, global_constants)
        return result


def report_sprites_complete(ships):
    # project management eh :P
    complete = len([ship.sprites_complete for ship in ships if ship.sprites_complete])
    print(
        "Sprites complete for",
        complete,
        "ships; incomplete for",
        len(ships) - complete,
        "ships;",
        str(int(100 * (complete / len(ships)))) + "%",
    )


# wrapped in a main() function so this can be called explicitly, because unexpected multiprocessing fork bombs are bad
def main():
    print("[RENDER GRAPHICS]")
    start = time()
    unsinkable_sam.main()
    # get args passed by makefile
    makefile_args = utils.get_makefile_args(sys)
    # default to no mp, makes debugging easier (mp fails to pickle errors correctly)
    num_pool_workers = makefile_args.get("num_pool_workers", 0)
    if num_pool_workers == 0:
        use_multiprocessing = False
        # just print, no need for a coloured echo_message
        print("Multiprocessing disabled: (PW=0)")
    else:
        use_multiprocessing = True
        # just print, no need for a coloured echo_message
        print("Multiprocessing enabled: (PW=" + str(num_pool_workers) + ")")

    graphics_input = os.path.join(currentdir, "src", "graphics", "ships")
    graphics_output_path = os.path.join(unsinkable_sam.generated_files_path, "graphics")
    if not os.path.exists(graphics_output_path):
        os.mkdir(graphics_output_path)

    hint_file = codecs.open(
        os.path.join(graphics_output_path, "_graphics_files_here_are_generated.txt"),
        "w",
        "utf8",
    )
    hint_file.write(
        "Don't edit the graphics files here.  They're generated by the build script. \n Edit sources in graphics_sources and export spritesheets to graphics_input."
    )
    hint_file.close()

    ships = unsinkable_sam.get_ships_in_buy_menu_order()
    if use_multiprocessing == False:
        for ship in ships:
            run_pipeline(ship)
    else:
        pool = Pool(processes=num_pool_workers)
        pool.map(run_pipeline, ships)
        pool.close()
        pool.join()

    report_sprites_complete(ships)

    # eh, how long does this take anyway?
    print(
        "[RENDER GRAPHICS]",
        "- complete",
        format((time() - start), ".2f") + "s",
    )


if __name__ == "__main__":
    main()
