import re
from pathlib import Path
from pprint import pprint


def group_text(target: str) -> None:
    output_path = Path("./data/group_text")
    output_path.mkdir(parents = True, exist_ok = True)

    target_list = []

    for i in Path(target).rglob("*.txt"):
        if match := re.match(r"(.*)_(\d+).txt", i.name):
            target_list.append({
                "obj": i,
                "name": match.group(1),
                "number": match.group(2)
            })
            
    names = set([i["name"] for i in target_list])

    for name in names:
        files_to_grp = filter(lambda x: x["name"] == name, target_list)

        for file in sorted(files_to_grp, key = lambda x: int(x["number"])):
            with (output_path / f"{name}.txt").open(mode = "a") as f:
                f.write(file["obj"].read_text())
    
