from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()


if __name__ == "__main__":
    print("Project Root :", BASE_DIR)
    print("ENV Exists   :", (BASE_DIR / ".env").exists())
    print("DATABASE_URL :", settings.DATABASE_URL)
    print("REDIS_URL    :", settings.REDIS_URL)
    print("ALGORITHM    :", settings.ALGORITHM)