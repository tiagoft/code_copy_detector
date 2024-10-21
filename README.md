# Code Copy Detector

A detector for copied code

Se você vai *desenvolver* deste repositório, vá para o [guia de desenvolvimento](README_DEV.md).

## Instalando Code Copy Detector:

Lembre-se de seguir essas instruções de dentro do seu ambiente virtual preferido:

    conda create -n code_copy_detector python=3.11
    conda activate code_copy_detector

A primeira maneira é clonar o repositório e fazer uma instalação local:

    git clone https://github.com/tiagoft/code_copy_detector.git
    cd code_copy_detector
    pip install .

A segunda maneira é instalar diretamente

    pip install git+https://github.com/tiagoft/code_copy_detector.git

Para desinstalar, use:

    pip uninstall code_copy_detector

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

