
def wait_user():
    input()

def input_option(options: list[str], message: str = "Escolha uma opção:"):
    while True:
        print(f'\n{message}')
        for index, option in enumerate(options):
            print(f"[{index+1}]-{option}")
        print()
        option = input()

        if valid_option(option, (1, len(options))):
            return int(option) - 1
        
        print("Opção inválida! Tente novamente")

def valid_option(option: str, op_range: tuple) -> bool:
    if not option.isdigit():
        return False
    
    option = int(option)
    if option not in range(op_range[0], op_range[1]+1):
        return False
    
    return True

if __name__ == "__main__":

    options = ['opção 1', 'opção 2', 'opção 3']
    print(input_option(options, "escolha uma opção"))