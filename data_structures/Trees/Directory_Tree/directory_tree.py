import os
from tree import Node, Tree

file_contents = {}  # Diccionario auxiliar para guardar contenido

def build_tree(path):
    root_name = os.path.basename(os.path.abspath(path))
    tree = Tree(root_name)

    def add_items(current_path, current_tree):
        try:
            items = os.listdir(current_path)
        except PermissionError:
            return

        for item in items:
            item_path = os.path.join(current_path, item)
            if os.path.isdir(item_path):
                subtree = Tree(item)
                current_tree.insert_child(subtree)
                add_items(item_path, subtree)
            else:
                node = Node(item)
                current_tree.insert_child(node)

                # Leer y almacenar contenido en el diccionario
                try:
                    with open(item_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        file_contents[item_path] = content
                except (UnicodeDecodeError, OSError):
                    file_contents[item_path] = "<No se pudo leer el contenido>"

    add_items(path, tree)
    return tree

def print_tree(tree, indent=""):
    print(indent + "|-- " + tree.name)
    for child in tree.get_children():
        if isinstance(child, Tree):
            print_tree(child, indent + "    ")
        else:
            print(indent + "    " + "|-- " + child.name)

def main():
    current_path = r"C:\Users\jd7co\OneDrive\Desktop\UFM Progra\Estructura de Datos\Directory_Tree"

    if not os.path.isdir(current_path):
        print(f"El directorio '{current_path}' no existe.")
        return

    tree = build_tree(current_path)
    print("Árbol de directorio:\n")
    print_tree(tree)


if __name__ == "__main__":
    main()
