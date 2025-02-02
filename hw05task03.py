from sys import argv
from collections import Counter

def parse_log_line(line: str) -> dict:
    parts_logs = line.split(maxsplit=3)
    if len(parts_logs) < 4:
        raise ValueError(f"Не правильний формат рядка лог файлу")
    logs_dict = {
        "date": parts_logs[0],
        "time": parts_logs[1],
        "level": parts_logs[2],
        "message": parts_logs[3].strip()
    }
    return logs_dict

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            for line in file.readlines():
                log = parse_log_line(line)
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print(f'Помиллка віддкриття файлу. Файл не знайдено')
    except Exception as e:
        print('Сталася помилка:', e)
    return logs
    
def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'] == level, logs))
    
def count_logs_by_level(logs: list) -> dict:
    return dict(Counter(log["level"] for log in logs))

    
def display_log_counts(counts: dict):
    if counts:
        print('Рівень логування | Кількість\n------------------|----------')

        for level, count in counts.items():
            print(f'{level:<18}| {count}')

def main():
    if len(argv) < 2:
        print("Usage: python main.py <log_file_path> [log_level]")
        
    file_path = argv[1]
    log_level = argv[2].upper() if len(argv) > 2 else None
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    
    display_log_counts(counts)
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f'Деталі логів для рівня \'{log_level}\':')
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

if __name__ == '__main__':
    main()