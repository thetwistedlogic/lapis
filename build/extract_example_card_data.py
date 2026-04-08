# A meta script for extracting the data from example_card.csv and putting it into a more user friendly format
from pathlib import Path
import yaml

Path("example_card").mkdir(exist_ok=True)

with open("anki_fields.old.yaml", "r", encoding="utf-8") as fields_file:
    anki_fields = yaml.safe_load(fields_file)

with open("example_card.csv") as f:
    for line in f:
        fields_content = line.strip().split("\t")
        i = 0
        for content, metadata in zip(fields_content, anki_fields):
            name = metadata["name"]
            i += 1
            with open(f"example_card/{i:02}_{name}.txt", "w") as f:
                f.write(content)
