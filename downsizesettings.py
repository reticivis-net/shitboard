from pathlib import Path

from PIL import Image

inpath = "settings icons"
outpaths = [
    "shitboard/Library/Themes/shitboard.theme/Bundles/com.apple.preferences-ui-framework",
    "shitboard/Library/Themes/shitboard.theme/Bundles/com.apple.preferences-framework",
    "shitboard/Library/Themes/shitboard.theme/Bundles/com.apple.Preferences",
]
for icon in Path(inpath).glob("*.png"):
    print(icon)
    im = Image.open(icon)
    im1x = im.resize((29, 29), resample=Image.NEAREST)
    im2x = im.resize((29 * 2, 29 * 2), resample=Image.NEAREST)
    im3x = im.resize((29 * 3, 29 * 3), resample=Image.NEAREST)
    for outpath in outpaths:
        im1x.save(f"{outpath}/{icon.stem}{icon.suffix}")
        im2x.save(f"{outpath}/{icon.stem}@2x{icon.suffix}")
        im3x.save(f"{outpath}/{icon.stem}@3x{icon.suffix}")
print("done")
