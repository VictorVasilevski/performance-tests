from pydantic import BaseModel, Field
import random


class SeedCardResult(BaseModel):
    card_id: str


class SeedOperationResult(BaseModel):
    operation_id: str


class SeedAccountResult(BaseModel):
    account_id: str
    physical_cards: list[SeedCardResult] = Field(default_factory=list)
    top_up_operations: list[SeedOperationResult] = Field(default_factory=list)
    purchase_operations: list[SeedOperationResult] = Field(default_factory=list)


class SeedUserResult(BaseModel):
    user_id: str
    deposit_accounts: list[SeedAccountResult] = Field(default_factory=list)
    savings_accounts: list[SeedAccountResult] = Field(default_factory=list)
    debit_accounts: list[SeedAccountResult] = Field(default_factory=list)
    credit_accounts: list[SeedAccountResult] = Field(default_factory=list)


class SeedsResultSchema(BaseModel):
    users: list[SeedUserResult] = Field(default_factory=list)

    def get_next_user(self) -> SeedUserResult:
        return self.users.pop(0)

    def get_random_user(self):
        return random.choice(self.users)
