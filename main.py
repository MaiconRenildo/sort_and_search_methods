from sort import quicksort,bubble_sort,selection_sort
from search import binary_search,sequential_search


array = []
ARRAY_LEN = 10


def clear_terminal():
    import os
    os.system('clear' if os.name == 'posix' else 'cls')


def clear_vetor():
    array.clear()


def fill_array():
    clear_vetor()
    clear_terminal()
    print("Preenchimento do vetor: \n")
    i = 0
    while(i<ARRAY_LEN):
        array.append(int(input('['+str(i)+']:'))) 
        i = i+ 1
    main()


def fill_array_menu():
    if(len(array)!=0):
        clear_terminal()
        print("O vetor já está preenchido com os seguintes dados: ",array)
        option = str(input('\nDeseja preenchê-lo novamente? \n(s/n): '))
        if option.upper() == "S":
            fill_array()
        elif option.upper() == "N":
            main()
        else:
            fill_array_menu()
    else:
        fill_array()


def exit_program():
    exit("\nPrograma encerrado com sucesso")




search_options = {
  "A": { "method": binary_search, "name": "Binary Search" },
  "B": { "method": sequential_search, "name": "Sequential search" },
}


def search_menu():
    clear_terminal()
    print("Métodos de Busca\n ")

    for key, value in search_options.items():
        print(str(key) + " - " + value['name'])
  
    opt = str(input('\nSua opção: '))

    if search_options.get(opt.upper()):
        option_selected = search_options[opt.upper()]
        clear_terminal()

        print("Busca com " + option_selected['name'] )
        print("\nVetor: ",array)

        search_for = int(input("\nNúmero procurado: "))
        
        if option_selected['name'] == "Binary Search":
            sorted_array = array.copy()
            sorted_array.sort()
            print("\nVetor ordenado: ",sorted_array)
            index = option_selected['method'](sorted_array,search_for)
        else:
            index = option_selected['method'](array,search_for)

        if index:
            print("\nNúmero encontrado no índice",index)
        else:
            print("\nNúmero não encontrado")

        input("\n")
        main()

    else:
        search_menu()




sort_options = {
  "A": { "method": quicksort, "name": "Quicksort" },
  "B": { "method": selection_sort, "name": "Selection sort" },
  "C": { "method": bubble_sort, "name": "Buble sort" },
}


def sort_menu():
    clear_terminal()
    print("Métodos de ordenação\n ")

    for key, value in sort_options.items():
        print(str(key) + " - " + value['name'])
  
    opt = str(input('\nSua opção: '))

    if sort_options.get(opt.upper()):
        option_selected = sort_options[opt.upper()]
        clear_terminal()

        print("Ordenação com " + option_selected['name'] )
        print("\nVetor a ser ordenado: ",array)
        ordenado = option_selected['method'](array)
        print("\nVetor ordenado: ",ordenado)

        input("\n")
        main()

    else:
        sort_menu()




options = {
  1: { "method": fill_array_menu, "description": "Preencher o vetor" },
  2: { "method": search_menu, "description": "Buscar por um valor" },
  3: { "method": sort_menu, "description": "Ordenar o vetor" },
  4: { "method": exit_program, "description": "Sair" }
}


def main():
    clear_terminal()
    print("Métodos de busca e ordenação\n")
    print("Opções:\n")

    for key, value in options.items():
        print(str(key) + " - " + value['description'])

    opt = int(input('\nSua opção: '))
    option_selected = options[opt]['method'] if options.get(opt) else main
    option_selected()


main()