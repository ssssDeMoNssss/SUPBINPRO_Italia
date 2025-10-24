import vk_api
import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Инициализация VK API
vk_session = vk_api.VkApi(token=os.getenv('VK_TOKEN'))
vk = vk_session.get_api()

# Пример функции для отправки сообщения
def send_message(user_id, message):
    vk.messages.send(
        user_id=user_id,
        message=message,
        random_id=0
    )

if __name__ == "__main__":
    print("Бот запущен!")