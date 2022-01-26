#!/usr/bin/env python3

from fontTools.subset import *
from fontTools.ttLib.ttCollection import TTCollection
import io
import logging

VF_FONT = "Sans/Variable/OTC/NotoSansCJK-VF.otf.ttc"
NUM_FONTS = 5
OUT_COLLECTION = "NotoSansCJK-VF-subset.otf.ttc"
SUBSET_CHAR = "是"

logging.basicConfig(format="%(asctime)s %(message)s")
log = logging.getLogger("fontTools.subset")
log.setLevel(logging.INFO)


if __name__ == "__main__":
    options = Options()
    options.notdef_outline = True
    options.verbose = True
    collection = TTCollection()
    for font_number in range(5):
        options.font_number = font_number
        subsetter = Subsetter(options=options)
        subsetter.populate(text=SUBSET_CHAR)
        subset_font = load_font(VF_FONT, options)
        subsetter.subset(subset_font)
        collection.fonts.append(subset_font)
    collection.save(OUT_COLLECTION)
