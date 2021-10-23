from configparser import ConfigParser, NoOptionError, NoSectionError
import os

def load_conf(config: ConfigParser, section: str, name: str, default=None) -> str:
    try:
        output = config.get(section, name)
    except (NoOptionError, NoSectionError):
        output = default
    return output

def config() -> None:
    config_parse = ConfigParser()
    config_parse.read("settings.ini")
    DATABASE = "DATABASE"
    BOT = "BOT"

    #DATABASE
    os.environ.setdefault("DATABASE_NAME", load_conf(config_parse, DATABASE, "NAME", "dbname"))
    os.environ.setdefault("DATABASE_USER", load_conf(config_parse, DATABASE, "USER", "user"))
    os.environ.setdefault("DATABASE_PASSW", load_conf(config_parse, DATABASE, "PASSWORD", "root"))
    os.environ.setdefault("DATABASE_HOST", load_conf(config_parse, DATABASE, "HOST", "localhost"))
    os.environ.setdefault("DATABASE_PORT", load_conf(config_parse, DATABASE, "PORT", "5432"))
    os.environ.setdefault("DRIVER", load_conf(config_parse, DATABASE, "DRIVER", "sqlite"))

    #BOT
    os.environ.setdefault("TOKEN", load_conf(config_parse, BOT, "BOT_TOKEN", None))

def get_messages() -> dict:
    return {
        "HI": "Привет {}. Какая проблема?", 
        "Peshkom": {
                    1: "1. Разбитый тротуар.",
                    2: "2. Отсутствие тротуара.",
                    3: "3. Пандус не соответствует нормам.",
                    4: "4. Тратуар перекрыт(забором, парковкой, пристройкой, и тд...)",
                    5: "5. Снять(Удалить) проблему."
                }
    }