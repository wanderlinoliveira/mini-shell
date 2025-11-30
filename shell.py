import os
from leitura import ler_comando
from execucao import executar_comando


def main():
    """
    Controla o loop principal do shell, processando comandos até receber
    'exit' ou EOF (Ctrl+D).
    """
    while True:
        args = ler_comando()
        
        if args is None: # EOF (End of File) (Ctrl+D)
            os.write(1, b"\n")
            break
            
        if len(args) == 0: # Enter vazio
            continue
            
        if args[0] == "exit":
            os.write(1, b"Saindo...\n")
            break
            
        executar_comando(args)

if __name__ == "__main__":
    main()
