from pydantic import BaseModel, Field, ConfigDict


class CardSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    pin: str
    cvv: str
    type: str
    status: str
    account_id: str = Field(alias="accountId")
    card_number: str = Field(alias="cardNumber")
    card_holder: str = Field(alias="cardHolder")
    expiry_date: str = Field(alias="expiryDate")
    payment_system: str = Field(alias="paymentSystem")


class IssueVirtualCardRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")
    account_id: str = Field(alias="accountId")


class IssuePhysicalCardRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    user_id: str = Field(alias="userId")
    account_id: str = Field(alias="accountId")


class IssueVirtualCardResponseSchema(BaseModel):
    card: CardSchema


class IssuePhysicalCardResponseSchema(BaseModel):
    card: CardSchema
