# import uuid
# from typing import Optional, Union
#
# from fastapi import Depends, Request
# from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin, InvalidPasswordException
# from fastapi_users.authentication import (
#     AuthenticationBackend,
#     BearerTransport,
#     JWTStrategy,
# )
# from fastapi_users.db import SQLAlchemyUserDatabase
#
# from user.models import User, get_user_db
# from user import schemas
#
# SECRET = "qwesdadsa132!@#@!#@321312dsdaodfk"
#
#
# class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
#     reset_password_token_secret = SECRET
#     reset_password_token_lifetime_seconds = 3600
#     verification_token_secret = SECRET
#
#     async def on_after_register(self, user: User, request: Optional[Request] = None):
#         print(f"User {user.id} has registered.")
#
#     async def on_after_forgot_password(
#             self, user: User, token: str, request: Optional[Request] = None
#     ):
#         print(f"User {user.id} has forgot their password. Reset token: {token}")
#
#     async def on_after_request_verify(
#             self, user: User, token: str, request: Optional[Request] = None
#     ):
#         print(f"Verification requested for user {user.id}. Verification token: {token}")
#
#     def validate_password(
#             self, password: str, user: Union[schemas.UserCreate, User]
#     ) -> None:
#         if len(password) < 8:
#             raise InvalidPasswordException(
#                 reason="Password should be at least 8 characters"
#             )
#         if user.email in password:
#             raise InvalidPasswordException(
#                 reason="Password should not contain e-mail"
#             )
#
#
# async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
#     yield UserManager(user_db)
#
#
# bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")
#
#
# def get_jwt_strategy() -> JWTStrategy:
#     return JWTStrategy(secret=SECRET, lifetime_seconds=3600)
#
#
# auth_backend = AuthenticationBackend(
#     name="jwt",
#     transport=bearer_transport,
#     get_strategy=get_jwt_strategy,
# )
#
# fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])
#
# current_active_user = fastapi_users.current_user(active=True)
