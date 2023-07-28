file1 = open('list - Copy (0).txt', 'r', encoding="utf-8")
lines = file1.readlines()
print(f'{lines}')
lines = list(filter(lambda line: line.startswith('Конкурсная группа') or
                                 (len(line) > 13 and (line.endswith('Да\n') or line.endswith('Нет\n'))), lines))
print(lines)