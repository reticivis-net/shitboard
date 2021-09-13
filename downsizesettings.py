from pathlib import Path

from PIL import Image

inpath = "settings icons"
outpaths = [
    "shitboard/Library/Themes/shitboard.theme/Bundles/com.apple.preferences-ui-framework",
    "shitboard/Library/Themes/shitboard.theme/Bundles/com.apple.preferences-framework",
    "shitboard/Library/Themes/shitboard.theme/Bundles/com.apple.Preferences",
]
mask = Image.open("mask@512px.png")
mask1x = mask.resize((29, 29))
mask2x = mask.resize((29 * 2, 29 * 2))
mask3x = mask.resize((29 * 3, 29 * 3))

for icon in Path(inpath).glob("*.png"):
    print(icon)
    im = Image.open(icon)
    im1x = Image.new("RGBA", (29, 29))
    im1x.paste(im.resize((29, 29), resample=Image.NEAREST), (0, 0), mask1x)
    im2x = Image.new("RGBA", (29 * 2, 29 * 2))
    im2x.paste(im.resize((29 * 2, 29 * 2), resample=Image.NEAREST), (0, 0), mask2x)
    im3x = Image.new("RGBA", (29 * 3, 29 * 3))
    im3x.paste(im.resize((29 * 3, 29 * 3), resample=Image.NEAREST), (0, 0), mask3x)
    for outpath in outpaths:
        im1x.save(f"{outpath}/{icon.stem}{icon.suffix}")
        im2x.save(f"{outpath}/{icon.stem}@2x{icon.suffix}")
        im3x.save(f"{outpath}/{icon.stem}@3x{icon.suffix}")
print("done")
