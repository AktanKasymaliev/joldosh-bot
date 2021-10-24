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
    BOT = "BOT"

    #BOT
    os.environ.setdefault("TOKEN", load_conf(config_parse, BOT, "BOT_TOKEN", None))

def get_messages() -> dict:
    return {
        "HI": "Привет, {}. Какая проблема?", 
        "Peshkom": {
                    1: "Разбитый тротуар.",
                    2: "Отсутствие тротуара.",
                    3: "Пандус не соответствует нормам.",
                    4: "Тротуар перекрыт(забором, парковкой, пристройкой, и тд...)",
                    5: "Снять(Удалить) проблему."
                }
    }