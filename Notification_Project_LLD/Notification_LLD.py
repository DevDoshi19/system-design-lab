from abc import ABC, abstractmethod
from typing import Any


class INotifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailNotifier(INotifier):
    def __init__(self, smtp_host: str) -> None:
        self.__smtp_host = smtp_host

    def __connect(self) -> dict[str, Any]:
        return {"smtp_host": self.__smtp_host}

    def send(self, message: str) -> None:
        config = self.__connect()
        print(f"[EMAIL] {message}\n└─ via {config['smtp_host']}")


class SmsNotifier(INotifier):
    def __init__(self, api_key: str) -> None:
        self.__api_key = api_key

    def __call_api(self) -> dict[str, Any]:
        return {"api_key": self.__api_key}

    def send(self, message: str) -> None:
        config = self.__call_api()
        print(f"[SMS] {message}\n└─ via key {config['api_key'][:6]}***")


class PushNotifier(INotifier):
    def __init__(self, device_token: str) -> None:
        self.__device_token = device_token

    def __push_fcm(self) -> dict[str, Any]:
        return {"token": self.__device_token}

    def send(self, message: str) -> None:
        config = self.__push_fcm()
        print(f"[PUSH] {message}\n└─ to device {config['token'][:8]}...")


class WhatsAppNotifier(INotifier):
    def __init__(self, number: str) -> None:  
        self.__number = number

    def __get_number(self) -> dict[str, Any]:
        return {"number": self.__number}

    def send(self, message: str) -> None:
        config = self.__get_number()
        print(f"[WHATSAPP] {message}\n└─ to {config['number']}")


class NotificationManager:
    def __init__(self, notifier: INotifier) -> None:
        self.__notifier = notifier            

    def send_notification(self, message: str) -> None:
        self.__notifier.send(message)


if __name__ == "__main__":
    notifications = [
        (SmsNotifier("qwerty123"),            "OTP via SMS"),
        (EmailNotifier("devdoshi@example.com"),   "OTP via Email"),
        (PushNotifier("device_token_xyz"),    "OTP via Push"),
        (WhatsAppNotifier("+91 98765 43210"), "OTP via WhatsApp"),
    ]

    for notifier, message in notifications:
        NotificationManager(notifier).send_notification(message)
        print()