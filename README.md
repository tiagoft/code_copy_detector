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

    pip uninstall install code_copy_detector

## Uso

Para encontrar todos os comandos implementados, execute:

    code_copy_detector-cli --help

