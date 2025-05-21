import logging

# настраиваем конфигурацию логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="/Users/vertianovev/Учеба/Code/StudyProject/logs/application.log",
    filemode="w",
)
# создаем логер
card_logger = logging.getLogger("masks.card")
account_logger = logging.getLogger("masks.account")


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску в формате XXXX XX** **** XXXX,
    где X — это цифра номера."""
    nums_in_number_card = 16
    str_card_number = str(card_number)
    # записываем лог о запуске кода
    card_logger.info("Запуск кода")
    if nums_in_number_card != len(str_card_number):
        # записываем лог, если некорректно введен номер карты
        card_logger.info("Некорректно введен номер карты")
        raise ValueError("Вы ввели неверное количество цифр карты")
    else:
        # записываем лог об успешном возврате маски номера карты
        card_logger.info("Маска номера карты выполнена успешно")
        return f"{str_card_number[0:4]} {str_card_number[4:6]}** **** {str_card_number[12:16]}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску в формате **ХХХХ,
    где ХХХХ последние четыре цифры."""
    nums_in_account_number = 20
    str_account_number = str(account_number)
    # записываем лог о запуске кода
    account_logger.info("Запуск кода")
    if nums_in_account_number != len(str_account_number):
        # записываем лог, если некорректно введен номер счета
        account_logger.info("Некорректно введен номер счета")
        raise ValueError("Вы ввели неверное количество цифр счета")
    else:
        # записываем лог об успешном возврате маски номера счета
        account_logger.info("Маска номера счета выполнена успешно")
        return f"**{str_account_number[-4:]}"


# if __name__ == "__main__":
#     print(get_mask_card_number("9807890767676541"))
#     print(get_mask_account("12345654321890765436"))
