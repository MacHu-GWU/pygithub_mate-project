# -*- coding: utf-8 -*-

import dataclasses
from home_secret.api import hs


@dataclasses.dataclass
class Settings:
    owner_name: str = dataclasses.field()
    repo_name: str = dataclasses.field()
    token: str = dataclasses.field()


settings = Settings(
    owner_name="MacHu-GWU",
    repo_name="learn-github",
    token=hs.v("providers.github.accounts.sh.users.sh.secrets.dev.value"),
)
