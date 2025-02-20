import os
import sys
import platform

os_name = platform.system()

def get_os_command(app_name):
    match os_name:
        case "Windows":
            return f'pyinstaller --onefile --windowed --icon=assets/images/logos/club_programmation.ico --add-data "assets;assets" --name {app_name} src/main.py'
        case "Darwin":
            return f'pyinstaller --onedir --windowed --icon=assets/images/logos/club_programmation.icns --add-data "assets:assets" --name {app_name} --osx-bundle-identifier com.club-programmation.liepsim src/main.py'
        case _:
            return f'pyinstaller --onefile --windowed --add-data "assets:assets" --name {app_name} src/main.py'

def main():
    print(f'Vous êtes sur : {os_name}')

    app_name = input("Entrez le nom de l'exécutable (LIEPSIM par défaut) : ").strip() or "LIEPSIM"
    command = get_os_command(app_name)
    
    print(f"Exécution de la commande : {command}")
    os.system(command)

if __name__ == "__main__":
    main()
