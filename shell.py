import os
import sys

# --- MÓDULO DE LEITURA E PARSING ---
def ler_comando():
    prompt = b"myshell> "
    try:
        os.write(1, prompt) 
        entrada_bytes = os.read(0, 1024)
        if not entrada_bytes: return None
        entrada_str = entrada_bytes.decode().strip()
        if not entrada_str: return []
        return entrada_str.split()
    except OSError as e:
        print(f"Erro na leitura: {e}")
        return None

# --- MÓDULO DE EXECUÇÃO (NOVO!) ---
def executar_comando(args):
    """
    Recebe uma lista de argumentos (ex: ['ls', '-l']).
    Cria um processo filho e executa o comando.
    """
    try:
        pid = os.fork()

        if pid == 0:
            # === ESTAMOS NO PROCESSO FILHO ===
            # Aqui, vamos substituir o Python pelo comando digitado.
            try:
                # os.execvp(programa, lista_de_argumentos)
                # args[0] é o nome do comando (ex: "ls")
                # args é a lista completa (ex: ["ls", "-l"])
                os.execvp(args[0], args)
                
            except FileNotFoundError:
                # Se o comando não existir, o execvp falha e cai aqui.
                print(f"Erro: Comando '{args[0]}' não encontrado.")
                os._exit(1) # Encerra o filho com erro
            except OSError as e:
                print(f"Erro ao executar: {e}")
                os._exit(1)

        elif pid > 0:
            # === ESTAMOS NO PROCESSO PAI (SHELL) ===
            # O pai precisa esperar o filho terminar antes de mostrar o prompt de novo.
            # os.wait() retorna uma tupla (pid, status), mas só queremos esperar.
            os.wait()

        else:
            # pid < 0: Erro grave, o sistema não conseguiu criar o processo
            print("Erro ao criar processo (fork falhou).")

    except OSError as e:
        print(f"Erro de sistema: {e}")

# --- MÓDULO PRINCIPAL ---
def main():
    while True:
        args = ler_comando()
        
        if args is None: # EOF
            os.write(1, b"\n")
            break
            
        if len(args) == 0: # Enter vazio
            continue
            
        if args[0] == "exit":
            os.write(1, b"Saindo...\n")
            break
            
        # Agora chamamos a execução real!
        executar_comando(args)

if __name__ == "__main__":
    main()