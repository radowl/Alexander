import json
from datetime import datetime
from pathlib import Path
from collections import defaultdict, Counter
import webbrowser
import time
Name = "events.json"

def load_events():

    if not Path(Name).exists():

        date = [
            {
                "date": "1941-06-22",
                "description": "Начало Великой Отечественной войны",
                "participants": ["СССР", "Германия"]
            },
            {
                "date": "1943-02-02",
                "description": "Окончание Сталинградской битвы",
                "participants": ["СССР", "Германия"]
            },
            {
                "date": "1945-05-09",
                "description": "День Победы",
                "participants": ["СССР", "Германия", "Союзники"]
            },
            {
                "date": "1950-01-01",
                "description": "Основание ПАО «Татнефть»",
                "participants": ["СССР", "Татарстан"]
            },
            {
                "date": "1970-05-18",
                "description": "Добыча миллиардной тонны нефти в Татарстане",
                "participants": ["ПАО «Татнефть»"]
            },
            {
                "date": "1994-04-24",
                "description": "ПАО «Татнефть» становится акционерным обществом",
                "participants": ["ПАО «Татнефть»", "Россия"]
            }
        ]
        with open(Name, "w", encoding="utf-8") as file:
            json.dump(date, file, ensure_ascii=False, indent=4)
        return date

    try:
        with open(Name, "r", encoding="utf-8") as file:
         
            content = file.read().strip()
            if not content:
            
                date = [
                    {
                        "date": "1941-06-22",
                        "description": "Начало Великой Отечественной войны",
                        "participants": ["СССР", "Германия"]
                    },
                    {
                        "date": "1943-02-02",
                        "description": "Окончание Сталинградской битвы",
                        "participants": ["СССР", "Германия"]
                    },
                    {
                        "date": "1945-05-09",
                        "description": "День Победы",
                        "participants": ["СССР", "Германия", "Союзники"]
                    },
                    {
                        "date": "1950-01-01",
                        "description": "Основание ПАО «Татнефть»",
                        "participants": ["СССР", "Татарстан"]
                    },
                    {
                        "date": "1970-05-18",
                        "description": "Добыча миллиардной тонны нефти в Татарстане",
                        "participants": ["ПАО «Татнефть»"]
                    },
                    {
                        "date": "1994-04-24",
                        "description": "ПАО «Татнефть» становится акционерным обществом",
                        "participants": ["ПАО «Татнефть»", "Россия"]
                    }
                ]
                with open(Name, "w", encoding="utf-8") as file:
                    json.dump(date, file, ensure_ascii=False, indent=4)
                return date
         
            return json.loads(content)
    except json.JSONDecodeError:
  
        print("Ошибка: Файл events.json содержит некорректные данные. Будет использован пустой список событий.")
        return []
url = "https://vk.com/video-11254710_456241594?ysclid=m559rnk7tk771928623"
def SAVE(events):

    with open(Name, "w", encoding="utf-8") as file:
        json.dump(events, file, ensure_ascii=False, indent=4, default=str)

def ADD():

    date = input("Введите дату события (формат YYYY-MM-DD): ")
    description = input("Введите описание события: ")
    participants = input("Введите участников (через запятую, если есть): ")

    try:
        event_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Ошибка: Неверный формат даты. Используйте YYYY-MM-DD.")
        return

    events = load_events()
    event = {
        "date": date,
        "description": description,
        "participants": participants.split(", ") if participants else []
    }
    events.append(event)
    SAVE(events)
    print(f"Событие добавлено: {date} - {description}")

def POISK():

    keyword = input("Введите ключевое слово для поиска (или нажмите Enter для пропуска): ")
    start_date = input("Введите начальную дату (формат YYYY-MM-DD, или нажмите Enter для пропуска): ")
    end_date = input("Введите конечную дату (формат YYYY-MM-DD, или нажмите Enter для пропуска): ")

    events = load_events()
    results = []
    for event in events:
        if keyword and keyword.lower() not in event["description"].lower():
            continue
        event_date = datetime.strptime(event["date"], "%Y-%m-%d")
        if start_date and event_date < datetime.strptime(start_date, "%Y-%m-%d"):
            continue
        if end_date and event_date > datetime.strptime(end_date, "%Y-%m-%d"):
            continue
        results.append(event)

    if results:
        print("Найденные события:")
        for event in results:
            print(f"{event['date']}: {event['description']}")
    else:
        print("Событий не найдено.")

def stat():

    events = load_events()
    if not events:
        print("Нет данных для статистики.")
        return


    total_events = len(events)
    print(f"Общее количество событий: {total_events}")
    time.sleep(1)


    participants_counter = Counter()
    for event in events:
        participants_counter.update(event["participants"])
    if participants_counter:
        print("Самые упоминаемые участники:")
        time.sleep(2)
        for participant, count in participants_counter.most_common(5):
            print(f"  {participant}: {count} упоминаний")
            time.sleep(1)

 
    events_by_year = defaultdict(int)
    for event in events:
        year = datetime.strptime(event["date"], "%Y-%m-%d").year
        events_by_year[year] += 1
    print("События по годам:")
    for year, count in sorted(events_by_year.items()):
        print(f"  {year}: {count} событий")
        time.sleep(1)
url2 = "https://vkvideo.ru/video782249585_456239039"
def help():
   

    print("Доступные команды:")
    print("  1 - Добавить событие")
    print("  2 - Найти событие")
    print("  3 - Показать статистику")
    print("  4 - Показать справку")
    print("  0 - Выйти")

def main():

    while True:
        
        print("\nЧто вы хотите сделать?")
        help()
        choice = input("Введите номер команды: ")

        if choice == "1":
            ADD()
        elif choice == "2":
            POISK()
        elif choice == "3":
           stat()
        elif choice == "4":
             help()
        elif choice == "0":
            print("Выход из программы.")
            break
        elif choice == "секрет":
            webbrowser.open(url)
        elif choice == "42":
            webbrowser.open(url2)
        else:
            print("Ошибка: Неверный выбор. Попробуйте снова.")
if __name__ == "__main__":
    main()
