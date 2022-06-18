def is_tabel(arg_str):
    if arg_str[0]=='[' and arg_str[-1]==']':
        return True
    return False

def clean_tabel(arg_str):
    if is_tabel(arg_str):
        return arg_str[1:-1]