# Code Copy Detector

Um detector para código copiado.

Se você vai *desenvolver* deste repositório, vá para o [guia de desenvolvimento](README_DEV.md).

## Instalando Code Copy Detector:

Lembre-se de seguir essas instruções de dentro do seu ambiente virtual preferido. Recomendamos o uso do **`uv`** para gerenciamento de ambientes e pacotes.

### Configuração do Ambiente

Por favor, prefira o python 3.13 para desenvolvimento e instalação.

* **Linux/macOS:**
    ```bash
    uv venv <SEU-NOME-DO-VENV> --python 3.13
    source <SEU-NOME-DO-VENV>/bin/activate
    ```
* **Windows (Prompt de Comando):**
    ```bash
    uv venv <SEU-NOME-DO-VENV> --python 3.13
    <SEU-NOME-DO-VENV>\Scripts\activate
    ```
> **Observação:** Substitua `<SEU-NOME-DO-VENV>` pelo nome desejado (ex: `ccd-venv`).

### Instalação

A primeira maneira é clonar o repositório e fazer uma instalação local:

    git clone https://github.com/tiagoft/code_copy_detector.git
    cd code_copy_detector
    uv pip install .

A segunda maneira é instalar diretamente:

    uv pip install git+https://github.com/tiagoft/code_copy_detector.git

Para desinstalar, use:

    uv pip uninstall code_copy_detector

## Uso

### Comparar dois códigos-fonte

    code_copy_detector-cli compare codigo1.py codigo2.py

### Comparar códigos em um diretório

    code_copy_detector-cli comparedir caminho/do/diretorio --threshold=0.8 --ngram-length=10

* Ajuste o `threshold` para evitar muitas linhas desnecessárias na tela.
* Ajuste o `ngram-length` para ajustar o tamanho da janela (entre 10 e 20 parecem ser valores razoáveis)

### Gerar um grafo com a quantidade semelhança de códigos:

Essa funcionalidade ajuda para visualizar comunidades de compartilhamento de código:

    code_copy_detector-cli comparedir caminho/do/diretorio --threshold=0.8 --ngram-length=10 --output-dot > output.dot
    dot -Tpdf input.dot -o output.pdf

### Para encontrar todos os comandos implementados, execute:

    code_copy_detector-cli --help

