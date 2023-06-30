import random
art = """
                                          :=*#%@@@%#*=:                         
                                       -#@@@@@@%%%@@@@@@#-                      
                                      +@@@#=:       :=#@@@@=                    
                                       .=.  .=+*#*+=.  .*@@@#                   
                                           -@*=:::=*@#-  -@@@%                  
                     -============================.  *@+  -@@@+                 
                    %@@@@@@@@@@**********@@@@@@@@@@-  %@.  %@@%                 
                   :@@@*************************@@@*  #@.  %@@%                 
                   :@@%                         %@@* .#*  :@@@+                 
                   :@@%                         %@@*     .%@@%                  
                   :@@%                         %@@*      :*#.                  
                   :@@%                         %@@*                            
                   :@@%                         %@@*                            
                   :@@%                         %@@*                            
                   :@@%                         %@@*                            
                   :@@%                         %@@*                            
                   :@@%                         %@@*                            
                   :@@%                         %@@*                            
                   :@@%                         %@@*                            
                   :@@%                         %@@*                                                       
                   :@@%                         %@@*                            
                   :@@%                         %@@*                            
                   :@@%                         %@@*                            
                   :@@%                         %@@*                            
                   :@@@%%%%%%%%%%#=--#%%%%%%%%%%@@@*                            
                   :@@@@@@@@@@@@@     %@@@@@@@@@@@@*                            
                    %@@@@@@@@@@@@+. .=@@@@@@@@@@@@@-                            
                     :===========================-.                                                                                                                                                                                                                                                                           
"""                                                                                
print(art)                                                                                
                      
# Função para exibir uma frase aleatória de hackers
def display_random_hacker_quote():
    # Lista de frases de hackers
    hackers_quotes = [
        ("Não é um bug, é uma funcionalidade.", "Autor Desconhecido"),
        ("Hackeie o planeta!", "Autor Desconhecido"),
        ("A única maneira de fazer um ótimo trabalho é amar o que você faz.", "Steve Jobs"),
        ("Nós somos os criadores de música e somos os sonhadores dos sonhos.", "Arthur O'Shaughnessy"),
        ("O conhecimento é poder.", "Sir Francis Bacon"),
        ("Hackers resolvem problemas e constroem coisas, e eles acreditam em liberdade e ajuda mútua voluntária.", "Eric S. Raymond"),
        ("Nós somos os escolhidos, nós somos os puros.", "Mr. Robot"),
        ("Mantenha-se faminto, mantenha-se tolo.", "Steve Jobs"),
        ("Nós somos Anônimos. Nós somos Legião. Nós não perdoamos. Nós não esquecemos. Espere por nós.", "Autor Desconhecido"),
        ("Segurança é um processo, não um produto.", "Bruce Schneier"),
        ("O mais silencioso está mais apto a escutar.", "Autor Desconhecido"),
        ("Você não está sozinho.", "Mr. Robot"),
        ("Hackeie o Gibson.", "Dade Murphy (do filme 'Hackers - Piratas de Computador')"),
        ("Fique de pé, caia, levante novamente. E repita até que você não possa mais levantar. Aí você saberá que você está vivo.", "Mr. Robot"),
        ("Quem está no controle? Responda: eu estou.", "Mr. Robot"),
        ("A revolução começa em casa.", "Mr. Robot"),
        ("Nossos destinos estão selados. Porque essa é a natureza do poder. Total, completo, absoluto. - White Rose", "Mr. Robot"),
        ("Eu sou sério. Eu estou.", "Autor Desconhecido"),
        ("Hackeie o Gibson e lembre: abraços são mais dignos que apertos de mãos.", "Autor Desconhecido"),
        ("Você não está sozinho.", "Mr. Robot"),
        ("Nós somos Anônimos. Nós somos Legião. Nós não perdoamos. Nós não esquecemos. Espere por nós.", "Autor Desconhecido"),
        ("O mais silencioso está mais apto a escutar.", "Autor Desconhecido"),
        ("Hackeie o Gibson.", "Dade Murphy (do filme 'Hackers - Piratas de Computador')"),
        ("Você não está sozinho.", "Mr. Robot"),
        ("Hackeie o Gibson e lembre: abraços são mais dignos que apertos de mãos.", "Autor Desconhecido"),
        ("Fique de pé, caia, levante novamente. E repita até que você não possa mais levantar. Aí você saberá que você está vivo.", "Mr. Robot"),
        ("Quem está no controle? Responda: eu estou.", "Mr. Robot"),
        ("A revolução começa em casa.", "Mr. Robot"),
        ("Nossos destinos estão selados. Porque essa é a natureza do poder. Total, completo, absoluto. - White Rose", "Mr. Robot")
    ]
    
    # Exibe uma frase aleatória
    random_index = random.randint(0, len(hackers_quotes) - 1)
    quote, author = hackers_quotes[random_index]
    print(quote)
    print("- ", author)

# Chama a função para exibir uma frase aleatória de hackers
display_random_hacker_quote()
