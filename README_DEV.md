# Guia para Desenvolvedores

## Configurando seu ambiente de trabalho

Execute estas instruçõess imediatamente após criar seu projeto com o cookiecutter.

1. Navegue para o diretório que você criou:

        cd code_copy_detector

2. Crie e ative um ambiente virtual para seu desenvolvimento:

        conda create -n code_copy_detector python=3.11
        conda activate code_copy_detector

3. **Instale `uv` e o aplicativo `gh` (opcional)**

   Instale o gerenciador de pacotes `uv` e o aplicativo `gh` (GitHub CLI):

        conda install uv gh --channel conda-forge
        gh auth login

4. **Instale seu módulo em modo editável com `uv`:**

   O `uv` é usado aqui para instalar o pacote no modo editável (`-e .`):

        uv pip install -e .

5. Verifique que a ferramenta de linha de comando está funcionando:

        code_copy_detector-cli --help

## Sincronizando com Github

### Com o aplicativo `gh`

Na pasta-raiz de seu projeto recém-criado:

    git init
    git add *
    git commit -m "Commit inicial"
    gh repo create code_copy_detector --public --push --source .

### Sem o aplicativo `gh`

1. Em seu navegador, vá para o [GitHub](https://www.github.com) e faça login.
1. Crie um novo repositório (vazio, sem README inicial, sem gitignore, etc) chamado **code_copy_detector** (lembre-se de respeitar maiúsculas, minúsculas, etc).
1. Execute os comandos abaixo na pasta-raiz de seu projeto recém-criado:

        git init
        git add *
        git commit -m "Commit inicial"
        git remote add origin https://github.com/<SEU-USUÁRIO-DO-GITHUB>/code_copy_detector.git
        git push --set-upstream origin main