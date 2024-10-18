import json

def jupyter_to_py(fname_in : str, fname_out : str):
    """Returns a virtual file for the python content of a jupyter notebook"""
    with open(fname_in, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    pyfile = ''

    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            src = ''.join(cell['source'])
            pyfile += src + '\n'

    with open(fname_out, 'w') as f:
        f.write(pyfile)

    return fname_out