import os
import shutil
import time
import requests
import motd
from pyIRsend import irsend
import xml.etree.ElementTree as ET
from tqdm import tqdm

#mensagem hacker do dia
motd.display_random_hacker_quote()

# Pasta onde o script está localizado
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Pasta que contém os arquivos XML com os códigos IR
CODES_FOLDER = os.path.join(SCRIPT_DIR, 'codes')

# URL do repositório "lirc-remotes"
REMOTES_REPO_URL = 'https://github.com/probonopd/lirc-remotes/archive/refs/heads/master.zip'

# Função para criar a pasta "codes" e mover para o diretório correto
def setup_codes_folder():
    if not os.path.exists(CODES_FOLDER):
        os.makedirs(CODES_FOLDER)
        print("Pasta 'codes' criada.")

    current_dir = os.getcwd()
    if current_dir != SCRIPT_DIR:
        codes_dir = os.path.join(current_dir, 'codes')
        if os.path.exists(codes_dir):
            print("Movendo a pasta 'codes' para o diretório correto...")
            shutil.move(codes_dir, CODES_FOLDER)
            print("Pasta 'codes' movida para o diretório correto.")

# Função para baixar e extrair o repositório "lirc-remotes" para a pasta "codes"
def download_lirc_remotes():
    print("Baixando o repositório 'lirc-remotes'...")
    response = requests.get(REMOTES_REPO_URL, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
    with open('lirc-remotes.zip', 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    print("Download concluído.")

    print("Extraindo o repositório 'lirc-remotes'...")
    shutil.unpack_archive('lirc-remotes.zip', CODES_FOLDER)
    extracted_folder = os.path.join(CODES_FOLDER, 'lirc-remotes-master')
    if os.path.exists(extracted_folder):
        shutil.move(extracted_folder, CODES_FOLDER)
    print("Extração concluída.")

    os.remove('lirc-remotes.zip')

# Função para listar as marcas disponíveis
def list_brands():
    brands = os.listdir(CODES_FOLDER)
    if len(brands) > 0:
        print("Marcas disponíveis:")
        for brand in brands:
            print(f"- {brand}")
    else:
        print("Não foram encontradas marcas de dispositivos.")

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

# Função para listar os comandos disponíveis para uma marca de dispositivo
def list_commands(brand):
    commands = load_device_commands(brand)
    if commands is not None:
        print(f"Comandos disponíveis para a marca {brand}:")
        for command in commands:
            print(f"- {command}")
    else:
        print(f"Não foram encontrados comandos para a marca {brand}.")

# Função para listar as marcas de dispositivos por inicial
def list_brands_by_initial(initial):
    brands = os.listdir(CODES_FOLDER)
    matching_brands = [brand for brand in brands if brand.lower().startswith(initial.lower())]
    if len(matching_brands) > 0:
        print(f"Marcas disponíveis com a inicial '{initial}':")
        for brand in matching_brands:
            print(f"- {brand}")
    else:
        print(f"Não foram encontradas marcas de dispositivos com a inicial '{initial}'.")

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
    print("\n== Mi Remote ==\n")
    print("Criado por Jeanpseven")
    print("Objetivo: Controlar dispositivos por sinais de infravermelho")
    
    while True:
        print("\nOpções disponíveis:")
        print("1. Listar marcas de dispositivos")
        print("2. Listar comandos disponíveis para uma marca")
        print("3. Listar marcas de dispositivos por inicial")
        print("4. Controlar dispositivo")
        print("5. Sair")

        option = input("Digite o número da opção desejada: ")
        if option == '1':
            list_brands()
        elif option == '2':
            brand = input("Digite a marca do dispositivo: ")
            list_commands(brand)
        elif option == '3':
            initial = input("Digite a inicial desejada: ")
            list_brands_by_initial(initial)
        elif option == '4':
            brand = input("Digite a marca do dispositivo: ")
            control_device(brand)
        elif option == '5':
            break
        else:
            print("Opção inválida. Digite novamente.")

# Função principal para execução do script
def main():
    setup_codes_folder()
    download_lirc_remotes()
    interact_with_user()

# Executa o script
if __name__ == "__main__":
    main()
