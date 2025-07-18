import os


class Settings:
    NAME: str = "helpdesk"
    DATABASE_URI: str = os.environ.get("DATABASE_URI")
    IS_TEST_ENVIRONMENT: bool = os.environ.get("TEST", False)

    LOG_LEVEL: str = os.environ.get("LOG_LEVEL", "INFO")
    LOG_DIRECTORY: str = os.environ.get("LOG_DIRECTORY", "logs")

settings = Settings()
