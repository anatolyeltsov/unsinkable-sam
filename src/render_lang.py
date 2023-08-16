print("[RENDER LANG] render_lang.py")

import unsinkable_sam
import utils
from polar_fox import git_info

import codecs
import os
import shutil
import sys

from time import time

currentdir = os.curdir
sys.path.append(os.path.join("src"))  # add to the module search path

from chameleon import PageTemplateLoader  # chameleon used in most template cases

# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, "src", "templates"))

# get args passed by makefile
makefile_args = utils.get_makefile_args(sys)


def render_lang(lang_name, lang_dst, ships):
    lang_data = utils.get_lang_data(lang_name, ships)
    lang_template = templates["lang_file.pylng"]
    # flatten the strings for rendering
    lang_strings_formatted_as_lng_lines = []
    longest_string_length = max([len(key)] for key in lang_data["lang_strings"].keys())[
        0
    ]
    for string_name, string_value in lang_data["lang_strings"].items():
        # note that stupid pretty formatting of generated output is just to ease debugging string generation when needed, otherwise not essential
        separator = ":".rjust(longest_string_length - len(string_name) + 7)
        lang_strings_formatted_as_lng_lines.append(
            string_name + separator + string_value
        )

    lang_content = utils.unescape_chameleon_output(
        lang_template(
            git_info=git_info,
            utils=utils,
            lang_data=lang_data,
            lang_strings_formatted_as_lng_lines=lang_strings_formatted_as_lng_lines,
        )
    )
    # we clean up some templating artefacts just to produce more readable output for debugging when needed, otherwise not essential
    lines = lang_content.split("\n")
    stripped_lines = [line.lstrip() for line in lines]
    cleaned_lang_content = "\n".join(stripped_lines)
    # write the output eh
    dst_file = codecs.open(os.path.join(lang_dst, lang_name + ".lng"), "w", "utf8")
    dst_file.write(cleaned_lang_content)
    dst_file.close()


def main():
    start = time()
    unsinkable_sam.main()
    ships = set(unsinkable_sam.get_ships_in_buy_menu_order())

    lang_dst = os.path.join(unsinkable_sam.generated_files_path, "lang")
    if os.path.exists(lang_dst):
        shutil.rmtree(lang_dst)
    os.makedirs(lang_dst)

    hint_file = codecs.open(
        os.path.join(lang_dst, "_lang_files_here_are_generated.txt"), "w", "utf8"
    )
    hint_file.write(
        "Don't edit the lang files here.  They're generated by the build script. \n Edit the files in src/lang/ instead."
    )
    hint_file.close()

    # we'll try and read any toml file in the lang dir, this requires that no other toml files are present there
    # possibly the installed languages should be handled by the roster when it parses the toml, not sure eh? (potato / potato?)
    for file_name in os.listdir(os.path.join("src", "lang")):
        if file_name.endswith(".toml"):
            lang_name = file_name.split(".")[0]
            render_lang(lang_name, lang_dst, ships)

    print(
        "[RENDER LANG]",
        "- complete",
        format((time() - start), ".2f") + "s",
    )


if __name__ == "__main__":
    main()
