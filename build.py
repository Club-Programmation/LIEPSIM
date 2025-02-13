import os
import sys
import platform

def get_os_separator():
    # Séparateur de chemin en fonction du système d'exploitation.
    if platform.system() == "Windows":
        return ";"
    return ":"

def main():
    separator = get_os_separator()

    print(f'Vous êtes sur : {"Windows" if platform.system() == "Windows" else "Linux/MacOS"}')

    exe_name = input("Entrez le nom de l'exécutable (LIEPSIM par défaut) : ").strip() or "LIEPSIM"

    command = f'pyinstaller --onefile --add-data "assets{separator}assets" --name {exe_name} src/main.py'
    
    print(f"Exécution de la commande : {command}")
    os.system(command)

if __name__ == "__main__":
    main()
