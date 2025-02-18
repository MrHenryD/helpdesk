import os


class Settings:
    NAME: str = "helpdesk"
    DATABASE_URI: str = os.environ["DATABASE_URI"]
    IS_TEST_ENVIRONMENT: bool = os.environ.get("TEST", False)


settings = Settings()
