#frontend da aplicação
#importante para o desacoplamento da aplicação
from .config import settings


def main():
    print("Hello from", settings.NAME)
