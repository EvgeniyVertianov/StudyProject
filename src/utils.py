import json
import logging
from typing import Any

# настраиваем конфигурацию логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="/Users/vertianovev/Учеба/Code/StudyProject/logs/application.log",
    filemode="w",
)
# создаем логер
utils_logger = logging.getLogger("info.utils")


def get_info_about_transactions(path_to_file: str) -> Any:
    """Функция принимает путь к json файлу с транзакциями и открывает его"""
    try:
        # записываем лог о запуске кода
        utils_logger.info("Запуск кода")
        with open(path_to_file) as file:
            # записываем лог об открытии файла
            utils_logger.info("Файл успешно открыт")
            data = json.load(file)
            return data
    except FileNotFoundError as expect_info:
        # записываем ошибку, если она произошла во время работы кода
        utils_logger.error(f"Произошла ошибка: {expect_info}", exc_info=True)
        print(f"Файл не найден: {expect_info}")
        return []
    except json.JSONDecodeError as expect_info:
        # записываем ошибку, если она произошла во время работы кода
        utils_logger.error(f"Произошла ошибка: {expect_info}", exc_info=True)
        print(f"Ошибка декодирования файла: {expect_info}")
        return []


# if __name__ == "__main__":
#     print(get_info_about_transactions("/Users/vertianovev/Учеба/Code/StudyProject/data/operations.json"))
