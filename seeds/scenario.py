from abc import ABC, abstractmethod

from seeds.builder import build_grpc_seeds_builder
from seeds.dumps import save_seeds_result, load_seeds_result
from seeds.schema.plan import SeedPlanSchema
from seeds.schema.result import SeedsResultSchema


class SeedsScenario(ABC):
    def __init__(self):
        self.builder = build_grpc_seeds_builder()

    @property
    @abstractmethod
    def plan(self) -> SeedPlanSchema:
        ...

    @property
    @abstractmethod
    def scenario(self) -> str:
        ...

    def save(self, result: SeedsResultSchema) -> None:
        save_seeds_result(result=result, scenario=self.scenario)

    def load(self) -> SeedsResultSchema:
        return load_seeds_result(scenario=self.scenario)

    def build(self) -> None:
        result = self.builder.build(self.plan)
        self.save(result)
