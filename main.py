def main():
    """
    Функция для запуска основной программы
    """
    vacancies_json = []
    user_name = input('Введите Ваше имя: ').capitalize()
    print(f'{user_name}, приветствую в нашем парсере вакансий!')
    keyword = input("Введи ключевое слово для поиска вакансий: ")

    hh = HeadHunter(keyword)
    sj = SuperJob(keyword)
    pass


if __name__ == "__main__":
    pass