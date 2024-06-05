[![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/hidden_coding)


### README

#### English

## Telegram Bot for Solving Captchas for WTF

### Overview

This Telegram bot is designed to automate the process of solving captchas and choosing the Russian language in a bot interaction. It uses the Telethon library to interact with the Telegram API.

### Prerequisites

- Python 3.7 or higher
- Telethon library

### Installation

1. Clone the repository or download the script.
2. Install the required Python libraries:
   ```sh
   pip install telethon
   ```

### Configuration

1. Open the script and update the `account_list` with your Telegram account details:
   ```python
   account_list = [
       ('user_id', 'username', 'phone', 'appid', 'app_hash', 'telethon_hash'),
   ]
   ```

2. Update the `join_what` list with the commands to be sent to the bot:
   ```python
   join_what = [
       '/start refID', # e.g., /start 1234567890
   ]
   ```

### Usage

1. Run the script:
   ```sh
   python your_script_name.py
   ```

2. The bot will:
   - Start a conversation with the specified bot.
   - Automatically select the Russian language.
   - Solve captchas by identifying the correct button to click.

### Important Notes

- Ensure that your Telegram account details are correct to avoid login issues.
- The script includes a random delay between actions to mimic human behavior and avoid bot detection.

### License

This project is licensed under the MIT License.

---

#### Русский
[![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/hidden_coding)

## Telegram-бот для решения капч WTF

### Обзор

Этот Telegram-бот предназначен для автоматизации процесса решения капч и выбора русского языка во взаимодействии с ботом. Он использует библиотеку Telethon для взаимодействия с API Telegram.

### Предварительные требования

- Python 3.7 или выше
- Библиотека Telethon

### Установка

1. Клонируйте репозиторий или скачайте скрипт.
2. Установите необходимые библиотеки Python:
   ```sh
   pip install telethon
   ```

### Конфигурация

1. Откройте скрипт и обновите список `account_list` с данными ваших аккаунтов Telegram:
   ```python
   account_list = [
       ('user_id', 'username', 'phone', 'appid', 'app_hash', 'telethon_hash'),
   ]
   ```

2. Обновите список `join_what` с командами, которые будут отправлены боту:
   ```python
   join_what = [
       '/start refID', # например, /start 1234567890
   ]
   ```

### Использование

1. Запустите скрипт:
   ```sh
   python your_script_name.py
   ```

2. Бот будет:
   - Начинать разговор с указанным ботом.
   - Автоматически выбирать русский язык.
   - Решать капчи, определяя правильную кнопку для нажатия.

### Важные заметки

- Убедитесь, что данные вашего аккаунта Telegram верны, чтобы избежать проблем с входом.
- Скрипт включает случайные задержки между действиями, чтобы имитировать поведение человека и избежать обнаружения ботом.

### Лицензия

Этот проект лицензирован по лицензии MIT.
