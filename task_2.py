def find_common_participants(first_group, second_group):  #
    first_group = first_group.split("|")  # Участники первой группы
    second_group = second_group.split("|")  # Участники второй группы

    # Формирую список общих участников
    similar = []
    for first_members in first_group:
        for second_members in second_group:
            if second_members == first_members:
                similar.append(second_members)

    similar.sort()  # сортировка по алфавиту
    print("Общие участники среди двух групп -", similar)

# Списки участников
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group)
