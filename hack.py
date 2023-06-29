import os
import time
from pyIRsend import irsend
import nmap
import xml.etree.ElementTree as ET

# Pasta que contém os arquivos XML com os códigos IR
CODES_FOLDER = 'codes'

# Função para carregar os nomes das teclas disponíveis para uma marca de dispositivo
def load_device_commands(brand):
    brand_folder = os.path.join(CODES_FOLDER, brand)
    if os.path.isdir(brand_folder):
        commands = []
        for file_name in os.listdir(brand_folder):
            if file_name.endswith('.xml'):
                file_path = os.path.join(brand_folder, file_name)
                tree = ET.parse(file_path)
                root = tree.getroot()
                for code in root.findall('code'):
                    code_name = code.get('name')
                    if code_name not in commands:
                        commands.append(code_name)
        return commands
    return None

# Função para listar as marcas disponíveis
def list_brands():
    brands = os.listdir(CODES_FOLDER)
    if len(brands) > 0:
        print("Marcas disponíveis:")
        for brand in brands:
            print(f"- {brand}")
    else:
        print("Não foram encontradas marcas de dispositivos.")

# Função para listar os comandos disponíveis para uma marca de dispositivo
def list_commands(brand):
    commands = load_device_commands(brand)
    if commands is not None:
        print(f"Comandos disponíveis para a marca {brand}:")
        for command in commands:
            print(f"- {command}")
    else:
        print(f"Não foram encontrados comandos para a marca {brand}.")

# Função para controlar um dispositivo específico
def control_device(brand):
    brand_folder = os.path.join(CODES_FOLDER, brand)
    if os.path.isdir(brand_folder):
        commands = load_device_commands(brand)
        if commands is not None:
            while True:
                list_commands(brand)
                print("Digite 'sair' para voltar ao menu principal.")
                command = input("Digite o comando desejado: ")
                if command == 'sair':
                    break
                elif command in commands:
                    file_name = command + ".xml"
                    file_path = os.path.join(brand_folder, file_name)
                    tree = ET.parse(file_path)
                    root = tree.getroot()
                    for code in root.findall('code'):
                        code_name = code.get('name')
                        code_ccf = code.find('ccf').text.strip()
                        irsend.send_ircode(code_ccf)
                        print(f"Enviado comando IR: {code_name}")
                        time.sleep(1)  # Aguarda 1 segundo entre os comandos
                else:
                    print("Comando inválido.")
        else:
            print(f"Não foram encontrados comandos para a marca {brand}.")
    else:
        print("Marca de dispositivo não encontrada.")

# Função principal para interagir com o usuário
def interact_with_user():
    while True:
        print("\n== Mi Remote ==\n")
        print("Opções disponíveis:")
        print("1. Listar marcas de dispositivos")
        print("2. Listar comandos disponíveis para uma marca")
        print("3. Controlar dispositivo")
        print("4. Sair")

        option = input("Digite o número da opção desejada: ")
        if option == '1':
            list_brands()
        elif option == '2':
            brand = input("Digite a marca do dispositivo: ")
            list_commands(brand)
        elif option == '3':
            brand = input("Digite a marca do dispositivo: ")
            control_device(brand)
        elif option == '4':
            break
        else:
            print("Opção inválida. Digite novamente.")

# Executa a interação com o usuário
interact_with_user()
