from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file="secrets/.env")

    binance_key: str
    binance_secret: str
    binance_base_url: str
    binance_future_url: str


config = Config()
