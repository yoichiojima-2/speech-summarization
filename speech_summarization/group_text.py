import re
from argparse import ArgumentParser
from pathlib import Path


def group_text(target: str) -> None:
    output_path = Path("./data/group_text")
    output_path.mkdir(parents=True, exist_ok=True)

    target_list = []

    for i in Path(target).rglob("*.txt"):
        match_ = re.match(r"(.*)_(\d+).txt", i.name)
        if match_:
            target_list.append({"obj": i, "name": match_.group(1), "number": match_.group(2)})
        else:
            i.rename(output_path / i.name)

    names = set([i["name"] for i in target_list])

    for name in names:
        files_to_grp = filter(lambda x: x["name"] == name, target_list)

        for file in sorted(files_to_grp, key=lambda x: int(x["number"])):
            with (output_path / f"{name}.txt").open(mode="a") as f:
                f.write(file["obj"].read_text())


def parse_args() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("--target", "-t", type=str)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    group_text(args.target)
