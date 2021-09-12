from pathlib import Path

from PIL import Image

inpath = "settings icons"
outpath = "shitboard/Library/Themes/shitboard.theme/Bundles/com.apple.preferences-ui-framework"
for icon in Path(inpath).glob("*.png"):
    print(icon)
    im = Image.open(icon)
    im2x = im.resize((59, 59), resample=Image.NEAREST)
    im2x.save(f"{outpath}/{icon.stem}@2x{icon.suffix}")
    im3x = im.resize((89, 89), resample=Image.NEAREST)
    im3x.save(f"{outpath}/{icon.stem}@3x{icon.suffix}")
print("done")
