def read_file(file_path):
    """Citește conținutul unui fișier și returnează liniile ca listă."""
    with open(file_path, "r") as file:
        return file.readlines()

def write_file(file_path, lines):
    """Scrie o listă de linii într-un fișier."""
    with open(file_path, "w") as file:
        file.writelines(lines)
