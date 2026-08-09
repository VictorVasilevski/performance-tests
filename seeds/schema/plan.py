from pydantic import BaseModel, Field


class SeedCardsPlan(BaseModel):
    count: int = 0


class SeedOperationsPlan(BaseModel):
    count: int = 0


class SeedAccountsPlan(BaseModel):
    count: int = 0
    physical_cards: SeedCardsPlan = Field(default_factory=SeedCardsPlan)
    top_up_operations: SeedOperationsPlan = Field(default_factory=SeedOperationsPlan)
    purchase_operations: SeedOperationsPlan = Field(default_factory=SeedOperationsPlan)


class SeedUsersPlan(BaseModel):
    count: int = 0
    deposit_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)
    savings_account: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)
    debit_cards_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)
    credit_card_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)


class SeedPlanSchema(BaseModel):
    users: SeedUsersPlan = Field(default_factory=SeedUsersPlan)

# SeedPlanSchema(
#     users=SeedUsersPlan(
#         count=1000,
#         debit_cards_accounts=SeedAccountsPlan(
#             count=3,
#             physical_cards=SeedCardsPlan(count=5),
#             top_up_operations=SeedOperationsPlan(count=10)
#         )
#     )
# )