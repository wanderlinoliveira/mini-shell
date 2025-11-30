import os

def ler_comando():
    """
    Captura a entrada do usuário através de os.read(), processa a string
    e retorna uma lista de argumentos.
    
    Returns:
        list: Lista de argumentos do comando, ou [] para entrada vazia,
              ou None em caso de EOF ou erro.
    """
    prompt = b"> "
    try:
        os.write(1, prompt) 

        entrada_bytes = os.read(0, 1024)

        if not entrada_bytes:
            return None

        entrada_str = entrada_bytes.decode().strip()

        if not entrada_str: 
            return []

        return entrada_str.split()
    
    except OSError as e:
        print(f"Erro na leitura: {e}")
        return None

