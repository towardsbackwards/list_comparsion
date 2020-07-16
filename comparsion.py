"""скрипт для сравнения двух списков с указанием что добавилось в список, что ушло, насколько позиций произошло
смещение элемента в списке"""

list_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'A']
list_b = ['B', 'C', 'D', 'A', 'F', 'E', 'Z', 'M', 'N', 'J', 'K', 'L']
list_c = ['B', 'C', 'D', 'A', 'F', 'E', 'Z', 'M', 'N', 'J', 'K', 'L', 'A', 'A', 'B']


def compare_2(orig_list, changed_list):
    if orig_list == changed_list:
        return f"Списки идентичны:\n " \
               f"{orig_list}\n" \
               f"{changed_list} "
    else:
        print(f'Сравниваем списки: \n '
              f'до:\t{orig_list} \n '
              f'после:\t{changed_list}')
        for i in range(len(orig_list)):
            if orig_list[i] in changed_list:
                if changed_list.index(orig_list[i]) == i:
                    print(f'({orig_list[i]}, индекс {i}) оригинального списка остался на своем месте!')
                    changed_list[i] = None
                elif changed_list.index(orig_list[i]) != i:
                    movement = 'влево' if (i - changed_list.index(orig_list[i])) > 0 else 'вправо' \
                        if (i - changed_list.index(orig_list[i])) < 0 else 'никак'
                    print(f'({orig_list[i]}, индекс {i}) сместился на индекс '
                          f'{changed_list.index(orig_list[i])} ({movement} на {abs(i - changed_list.index(orig_list[i]))})')
                    changed_list[changed_list.index(orig_list[i])] = None
            elif orig_list[i] not in changed_list:
                print(f'({orig_list[i]}, индекс {i}) был удален из списка')
        for n in range(len(changed_list)):
            if changed_list[n] is not None:
                print(f'({changed_list[n]}, индекс {n}) был добавлен дополнительно')


compare_2(list_a, list_b)