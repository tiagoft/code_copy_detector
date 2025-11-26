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

def results_to_dot(output_dict : dict):
    """Writes a string that can be compiled as graphviz .dot file from the results of a comparison"""
    output_str = ""
    output_str += "digraph G {\n"

    added_nodes = set()
    for results in output_dict.keys():
        if results[0] not in added_nodes:
            output_str += f"\"{results[0]}\" \[label=\"{results[0].split('/')[-1]}\"];\n"
            added_nodes.add(results[0])
        if results[1] not in added_nodes:
            output_str += f"\"{results[1]}\" \[label=\"{results[1].split('/')[-1]}\"];\n"
            added_nodes.add(results[1])

    for results in output_dict.keys():
        output_str += f"\"{results[0]}\" -> \"{results[1]}\" \[label=\"{output_dict[results][0]/output_dict[results][1]:.1%}\"];\n"
        output_str += f"\"{results[1]}\" -> \"{results[0]}\" \[label=\"{output_dict[results][0]/output_dict[results][2]:.1%}\"];\n"

    output_str += "}\n"
    return output_str