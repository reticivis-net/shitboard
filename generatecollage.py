from pathlib import Path
import random

folders = [r"shitboard\Library\Themes\shitboard.theme\IconBundles", r"settings icons"]
imgs = []
for folder in folders:
    for icon in Path(folder).glob("*.png"):
        imgs.append(f"    <img src=\"{icon}\" alt=\"{icon.stem}\">")
random.shuffle(imgs)
imgs = "\n".join(imgs)
outfile = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        * {{
            padding: 0;
            margin: 0;
        }}

        body {{
            background: #555;
        }}

        .flex-container {{
            display: flex;
            flex-wrap: wrap;

        }}

        .flex-container > img {{
            width: 60px;
            margin: 10px;
            border-radius: 13px;
        }}
    </style>
</head>
<body>
<div class="flex-container">
{imgs}
</div>
</body>
</html>
"""
with open("collagething.html", "w+") as f:
    f.truncate(0)
    f.seek(0)
    f.write(outfile)