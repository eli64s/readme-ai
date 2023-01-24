"""src/format.py
"""
import pandas as pd


def get_icons(icon_list):
    icon_map = {}
    idx = 0
    while True:
        try:
            row = icon_list["icons"][idx]
            icon_map[row["name"].lower()] = row
        except:
            break
        idx += 1
    return icon_map


def create_header(file_io, pkgs):
    icon_list = file_io.read_json()
    icons = get_icons(icon_list)
    pkgs.append("github")
    header = ""
    for pkg in pkgs:
        if pkg in icons:
            badge = icons[pkg.strip().lower()]["src"]
            header += f'<img src="{badge}">\n\t\t\t\t'
    return header


def create_html(cfg, badges, name, path):
    header = f"""{cfg.html.head}
        <h1>{name}</h1>
        <hr>
        <h3>Software & Packages</h3>
        <p>[description]</p>
        <p>{badges}</p>
        </div>
        """
    body = cfg.html.body
    closing = cfg.html.close

    data = pd.read_csv(path)

    prev_dir = None
    for i, j in data.iterrows():
        file = j[0].split("/")
        curr_dir = file[0]
        script = file[1]

        if prev_dir != curr_dir:
            body = f"""{body}
            <div><details open>
            <summary>{curr_dir.upper()}</summary>"""

        tag = f"""
            <h5>{script}</h5>
            <p>{j[1].replace('"', '')}</p>
        """
        body = f"{body}{tag}"

        prev_dir = curr_dir

        if curr_dir != prev_dir:
            body = f"{body}</details></div>"

    return f"{header}{body}{closing}"
