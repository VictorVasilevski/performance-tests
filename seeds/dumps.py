from pathlib import Path

from seeds.schema.result import SeedsResultSchema


def save_seeds_result(result: SeedsResultSchema, scenario: str):
    Path("dumps").mkdir(exist_ok=True)
    with open(f"./dumps/{scenario}_seeds.json", "w+", encoding="utf-8") as f:
        f.write(result.model_dump_json(indent=4))


def load_seeds_result(scenario: str) -> SeedsResultSchema:
    with open(f"./dumps/{scenario}_seeds.json", "r", encoding="utf-8") as f:
        return SeedsResultSchema.model_validate_json(f.read())
