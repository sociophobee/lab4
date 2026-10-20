import string

# Імена файлів за варіантом 13
FILE_1 = "TF16_1.txt"
FILE_2 = "TF16_2.txt"

def create_initial_file():
    """Частина а) Завдання Тімліда: створення файлу TF16_1 із рядків різної довжини"""
    lines = [
        "Осінь прийшла несподівано, принісши прохолодний вітер та жовте листя.",
        "Програмування на Python — це дуже цікаво, зручно і перспективно!",
        "Екран монітора світиться в темряві; алгоритми, функції, цикли працюють чітко.",
        "Іноді варто зробити паузу: випити чаю, подумати про ідеї, оновити думки.",
        "Успіх у навчанні залежить від практики, уважності та командної роботи."
    ]
    
    try:
        with open(FILE_1, "w", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")
        print(f"\n[Успіх] Файл '{FILE_1}' успішно створено та заповнено початковими даними!\n")
    except IOError as e:
        print(f"\n[Помилка] Не вдалося створити або записати файл '{FILE_1}': {e}\n")


# ==========================================
# ФУНКЦІЯ СТУДЕНТА 1 (Анастасія) - Частина б)
# ==========================================
def process_words_starting_with_vowel():
    """Частина б) Читання TF16_1, пошук слів на голосну літеру та запис у TF16_2"""
    vowels = "аеєиіїоуюяaeiouy"
    punctuation = string.punctuation + "—«»…"
    found_words = []

    try:
        with open(FILE_1, "r", encoding="utf-8") as file_in:
            for line in file_in:
                for char in punctuation:
                    line = line.replace(char, " ")
                
                words = line.split()
                for word in words:
                    if word and word[0].lower() in vowels:
                        found_words.append(word)
                        
    except FileNotFoundError:
        print(f"\n[Помилка] Файл '{FILE_1}' не знайдено! Спочатку виконайте пункт 1.\n")
        return
    except IOError as e:
        print(f"\n[Помилка] Помилка читання файлу '{FILE_1}': {e}\n")
        return

    try:
        with open(FILE_2, "w", encoding="utf-8") as file_out:
            for word in found_words:
                file_out.write(word + "\n")
        print(f"\n[Успіх] Оброблення завершено! Знайдено слів на голосну: {len(found_words)}.")
        print(f"Результат записано у файл '{FILE_2}'.\n")
    except IOError as e:
        print(f"\n[Помилка] Не вдалося записати дані у файл '{FILE_2}': {e}\n")


# ==========================================
# ФУНКЦІЯ СТУДЕНТА 2 (Дмитро) - Частина в)
# ==========================================
def print_result_file():
    """Частина в) Читання вмісту файлу TF16_2 та виведення його по рядках"""
    try:
        with open(FILE_2, "r", encoding="utf-8") as file:
            print(f"\n--- Вміст файлу '{FILE_2}' (слова на голосну літеру) ---")
            lines = file.readlines()
            if not lines:
                print("Файл порожній.")
            else:
                for index, line in enumerate(lines, start=1):
                    print(f"{index}. {line.strip()}")
            print("-------------------------------------------------------\n")
    except FileNotFoundError:
        print(f"\n[Помилка] Файл '{FILE_2}' не знайдено! Спочатку виконайте пункт 2.\n")
    except IOError as e:
        print(f"\n[Помилка] Не вдалося прочитати файл '{FILE_2}': {e}\n")


def main():
    while True:
        print(" ОБРОБЛЕННЯ ТЕКСТОВИХ ФАЙЛІВ (Варіант 13) ")
        print("1. Створити початковий файл TF16_1 (Тімлід - частина а)")
        print("2. Знайти слова на голосну літеру і записати в TF16_2 (Студент 1 - частина б)")
        print("3. Вивести вміст файлу TF16_2 по рядках (Студент 2 - частина в)")
        print("4. Вийти з програми")
        print("======================================================")
        
        choice = input("Оберіть дію (1-4): ")
        
        if choice == '1':
            create_initial_file()
        elif choice == '2':
            process_words_starting_with_vowel()
        elif choice == '3':
            print_result_file()
        elif choice == '4':
            print("Роботу програми завершено.")
            break
        else:
            print("\n[Помилка] Невірний вибір. Спробуйте ще раз.\n")

if __name__ == "__main__":
    main()