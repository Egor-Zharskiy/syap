# 3. Сформировать (не программно) текстовый файл. В нём каждая
# строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и
# количество занятий. Необязательно, чтобы для каждого предмета были все
# типы занятий.
# Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#  Физика: 30(л) 10(лаб)
#  Физкультура: 30(пр)
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”:30}

subjects_dict = {}

with open('subjects.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    parts = line.strip().split(':')
    if len(parts) == 2:
        subject_name = parts[0].strip()
        details = parts[1].split()

        total_classes = 0
        for detail in details:
            try:
                count = int(detail.split('(')[0])
                total_classes += count
            except ValueError:
                pass

        subjects_dict[subject_name] = total_classes

print("Информация о занятиях по предметам:")
for subject, total_classes in subjects_dict.items():
    print(f"{subject}: {total_classes} занятий")
