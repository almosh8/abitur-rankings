def parse():
    candidate_rankings = {}
    roles_info = {}

    for i in range(19):
        file1 = open(f'list - Copy ({i}).txt', 'r', encoding="utf-8")
        lines = file1.readlines()
        lines = list(filter(lambda line: line.startswith('Конкурсная группа') or
                                            line.startswith('Количество мест для зачисления') or
                                            (len(line) > 13 and (line.endswith('Да\n') or line.endswith('Нет\n'))), lines))


        name = lines[0]
        places = int(lines[1].strip()[-2:])
        roles_info[name] = places
        if name == '09.03.02':
            print(places)

        for line in lines[2:]:
            l = line.split('\t')
            id = l[1]
            score = int(l[2])
            prior = int(l[-2])

            orig = l[-3]
            if orig != 'Да':
                continue

            if not id in candidate_rankings:
                candidate_rankings[id] = [score, {}]
            candidate_rankings[id][1][prior] = name

    return roles_info, candidate_rankings