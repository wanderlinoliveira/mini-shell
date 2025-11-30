# Mini Shell - Projeto Integrador

## Descrição

Este projeto, desenvolvido como parte da disciplina MATA58 – Sistemas Operacionais da Universidade Federal da Bahia (UFBA), ministrada pela professora Larissa Barbosa Leoncio Pinheiro no semestre 2025.2, implementa um mini interpretador de comandos (shell) em Python que simula a execução de comandos em um terminal Linux, explorando chamadas ao sistema operacional.

O shell permite que o usuário interaja com o sistema por meio de comandos digitados, interpretando e executando essas instruções por meio da criação e gerenciamento de processos filhos, oferecendo uma visão prática do funcionamento interno de um ambiente Unix-like.

## Compilação e Execução

### Requisitos

- Python 3.10 ou superior
- Sistema operacional Linux

### Como executar

```bash
python3 shell.py
```

O shell iniciará e exibirá o prompt `> `, aguardando comandos do usuário. Para encerrar o shell, digite `exit` ou pressione `Ctrl+D`.

## Chamadas ao Sistema Utilizadas

O projeto utiliza as seguintes chamadas ao sistema do módulo `os` do Python:

- **`os.fork()`**: Cria um processo filho duplicando o processo atual. Retorna 0 no processo filho e o PID do filho no processo pai.

- **`os.execvp()`**: Substitui o processo filho pelo programa especificado. Recebe o nome do comando e uma lista de argumentos, buscando o executável no PATH do sistema.

- **`os.wait()`**: Faz o processo pai aguardar o término da execução do processo filho antes de continuar.

- **`os.read()`**: Lê dados do descritor de arquivo especificado (0 para entrada padrão). Utilizado para capturar comandos digitados pelo usuário.

- **`os.write()`**: Escreve dados no descritor de arquivo especificado (1 para saída padrão). Utilizado para exibir o prompt e mensagens.

## Exemplo de Uso

### ls (Listar arquivos)

```bash
$> ls
$> ls -l
$> ls -la
```

### echo (Exibir texto)

```bash
$> echo Olá mundo
$> echo "Teste com aspas"
$> echo -n "Sem quebra de linha"
```

### cat (Exibir conteúdo de arquivo)

```bash
$> cat README.md
$> cat shell.py
```

### exit (Sair do shell)

```bash
$> exit
```

## Estrutura do Código

O código está organizado em três arquivos principais, cada um contendo um módulo funcional:

1. **`leitura.py`** - Módulo de Leitura e Parsing: Contém a função `ler_comando()` que captura a entrada do usuário através de `os.read()`, processa a string e retorna uma lista de argumentos.

2. **`execucao.py`** - Módulo de Execução: Contém a função `executar_comando()` que cria um processo filho com `os.fork()`, executa o comando no filho com `os.execvp()` e faz o pai aguardar com `os.wait()`.

3. **`shell.py`** - Módulo Principal: Contém a função `main()` que controla o loop principal do shell, processando comandos até receber `exit` ou EOF. Este arquivo importa as funções dos outros módulos e serve como ponto de entrada do programa.

## Exemplos de Comandos Testados

### Comando `ls`

```
> ls
README.md  execucao.py  leitura.py  shell.py
```

### Comando `ls` com argumentos

```
> ls -l
total 20
-rwxrwx--- 1 root vboxsf 1388 nov 30 19:33 execucao.py
-rwxrwx--- 1 root vboxsf  713 nov 30 19:28 leitura.py
drwxrwx--- 1 root vboxsf    0 nov 30 19:45 __pycache__
-rwxrwx--- 1 root vboxsf 4989 nov 30 19:34 README.md
-rwxrwx--- 1 root vboxsf  656 nov 30 19:27 shell.py
```

### Comando `echo`

```
> echo Olá mundo
Olá mundo
```

### Comando `cat`

```
> cat README.md
# Mini Shell - Projeto Integrador
...
```

### Comando inexistente

```
> comando_inexistente
Erro: Comando 'comando_inexistente' não encontrado.
```

### Encerramento do shell

```
> exit
Saindo...
```

## Limitações Conhecidas

1. **Redirecionamento de entrada/saída**: O shell não suporta redirecionamento de entrada (`<`) ou saída (`>`, `>>`).

2. **Pipes**: Não há suporte para encadeamento de comandos através de pipes (`|`).

3. **Comandos internos**: Apenas o comando `exit` é tratado internamente. Outros comandos internos de shells tradicionais (como `cd`, `pwd`) não estão implementados.

4. **Execução em background**: Não é possível executar comandos em segundo plano usando `&`.

5. **Variáveis de ambiente**: Não há suporte para expansão de variáveis de ambiente ou substituição de comandos.

6. **Histórico de comandos**: O shell não mantém histórico de comandos executados.

7. **Comandos compostos**: Não é possível executar múltiplos comandos em uma única linha separados por `;` ou `&&`.

8. **Tratamento de aspas**: Strings com espaços não são tratadas adequadamente quando envolvidas por aspas.

9. **Autocompletar de comandos**: O shell não possui funcionalidade de autocompletar comandos ou nomes de arquivos através da tecla Tab.

10. **Tratamento de sinais**: Apenas o sinal EOF (Ctrl+D) é tratado para encerrar o shell. Outros sinais como SIGINT (Ctrl+C) não são tratados adequadamente.
