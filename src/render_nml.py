import codecs  # used for writing files - more unicode friendly than standard open() module

import sys
import os

currentdir = os.curdir
from time import time

import unsinkable_sam
import utils
import global_constants
import gestalt_graphics.graphics_constants as graphics_constants
from polar_fox import git_info
from rosters import (
    registered_rosters,
)  # Iron Horse has support for compiling only active roster, copy if/when needed

# get args passed by makefile
makefile_args = utils.get_makefile_args(sys)

from chameleon import PageTemplateLoader  # chameleon used in most template cases

# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, "src", "templates"))

generated_files_path = unsinkable_sam.generated_files_path


def render_header_item_nml(header_item, consists):
    template = templates[header_item + ".pynml"]
    return utils.unescape_chameleon_output(
        template(
            consists=consists,
            global_constants=global_constants,
            temp_storage_ids=global_constants.temp_storage_ids,  # convenience measure
            graphics_constants=graphics_constants,
            utils=utils,
            registered_rosters=registered_rosters,
            makefile_args=makefile_args,
            git_info=git_info,
        )
    )


def render_consist_nml(consist):
    result = utils.unescape_chameleon_output(consist.render())
    # write the nml per vehicle to disk, it aids debugging
    consist_nml = codecs.open(
        os.path.join(generated_files_path, "nml", consist.id + ".nml"), "w", "utf8"
    )
    consist_nml.write(result)
    consist_nml.close()
    # also return the nml directly for writing to the concatenated nml, don't faff around opening the generated nml files from disk
    return result


def main():
    print("[RENDER NML]")
    start = time()
    unsinkable_sam.main()
    print(unsinkable_sam.find_vacant_id_runs())

    generated_nml_path = os.path.join(generated_files_path, "nml")
    if not os.path.exists(generated_nml_path):
        os.mkdir(
            generated_nml_path
        )  # reminder to self: inside main() to avoid modifying filesystem simply by importing module
    grf_nml = codecs.open(
        os.path.join(generated_files_path, "unsinkable-sam.nml"), "w", "utf8"
    )

    consists = (
        unsinkable_sam.get_ships_in_buy_menu_order()
    )  # 'consists' not 'ships', it makes it easier to cross-maintain this script with scripts in IH and RH

    header_items = [
        "header",
        "cargo_table",
        "recolour_sprites",
        "procedures_alternative_var_random_bits",
        "procedures_colour_randomisation_strategies",
        "spriteset_empty_ss",
    ]
    for header_item in header_items:
        grf_nml.write(render_header_item_nml(header_item, consists))

    # multiprocessing was tried here and removed as it was empirically slower in testing (due to overhead of starting extra pythons probably)
    for consist in consists:
        grf_nml.write(render_consist_nml(consist))
    grf_nml.close()
    # eh, how long does this take anyway?
    print(
        "[RENDER NML]",
        "- complete",
        format((time() - start), ".2f") + "s",
    )


if __name__ == "__main__":
    main()
