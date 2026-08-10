from fastapi import FastAPI, APIRouter, Path, Body, status, HTTPException
from pydantic import BaseModel, Field, EmailStr, RootModel


app = FastAPI()

users_router = APIRouter(
    prefix="/api/v1/users",
    tags=["users-service"]
)


class UserIn(BaseModel):
    email: EmailStr
    username: str


class UserOut(UserIn):
    id: int


class UsersStore(RootModel):
    root: list[UserOut]

    def find(self, user_id: int) -> UserOut | None:
        return next((u for u in self.root if u.id == user_id), None)

    def create(self, user: UserIn) -> UserOut:
        user_out = UserOut(
            id=len(self.root) + 1,
            **user.model_dump()
        )
        self.root.append(user_out)
        return user_out

    def update(self, user_id: int, user: UserIn) -> UserOut:
        idx = next(i for i, user in enumerate(self.root) if user.id == user_id)
        updated = UserOut(id=user_id, **user.model_dump())
        self.root[idx] = updated
        return updated

    def delete(self, user_id: int) -> None:
        self.root = [u for u in self.root if u.id != user_id]


store = UsersStore(root=[])


@users_router.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: int):
    if not (user := store.find(user_id)):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    return user


@users_router.get("", response_model=list[UserOut])
async def get_users():
    return store.root


@users_router.post("", response_model=UserOut)
async def create_user(user: UserIn):
    return store.create(user)


@users_router.put("/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user: UserIn):
    if not store.find(user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    return store.update(user_id, user)


@users_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    if not store.find(user_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    store.delete(user_id)


app.include_router(users_router)
