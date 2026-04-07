# A meta script for extracting the data from example_card.csv and putting it into a more user friendly format
import yaml

with open("anki_fields.yaml", "r", encoding="utf-8") as fields_file:
    anki_fields = yaml.safe_load(fields_file)

with open("example_card.csv") as f:
    for line in f:
        fields_content = line.strip().split("\t")
        for content, metadata in zip(fields_content, anki_fields):
            name = metadata["name"]
            with open(f"example_card/{name}.txt", "w") as f:
                f.write(content)
