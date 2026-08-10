from pydantic import BaseModel, Field, ConfigDict
from clients.http.gateway.cards.schema import CardSchema


class AccountSchema(BaseModel):
    id: str
    type: str
    cards: list[CardSchema]
    status: str
    balance: float


class GetAccountsQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenDepositAccountRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenDepositAccountResponseSchema(BaseModel):
    account: AccountSchema


class OpenSavingsAccountRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenSavingsAccountResponseSchema(BaseModel):
    account: AccountSchema


class OpenDebitAccountRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenDebitAccountResponseSchema(BaseModel):
    account: AccountSchema


class OpenCreditAccountRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenCreditAccountResponseSchema(BaseModel):
    account: AccountSchema


class GetAccountsResponseSchema(BaseModel):
    accounts: list[AccountSchema]
