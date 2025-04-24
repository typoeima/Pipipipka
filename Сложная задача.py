import os

def scan_directory(path):
    emptys = []
    largest_file = {"path": None, "size": 0}
    total_files = 0
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            full_path = os.path.join(dirpath, file)
            size = os.path.getsize(full_path)
            total_files += 1
            total_size += size
            if size == 0:
                emptys.append(full_path)
            if size > largest_file["size"]:
                largest_file["path"] = full_path
                largest_file["size"] = size

    return {
        "emptys": emptys,
        "largest_file": largest_file,
        "total_files": total_files,
        "total_size": total_size
    }

def generate_report(report_data, output_path):
    with open(output_path, 'w', encoding='utf-8') as report:
        report.write("~~~~~~~~~~~~~~~~~СТАТИСТИКА СКАНИРОВАНИЯ:~~~~~~~~~~~~~~~~~\n")
        report.write(f"всего файлов: {report_data['total_files']}\n")
        report.write(f"общий размер: {report_data['total_size']} байт\n")
        report.write("\nПустые файлы:\n")

        #.write()
        if len(report_data["emptys"]) > 0:
            for path in report_data["emptys"]:
                report.write(f"- {path}\n")
        else:
            report.write("\nПустых файлов не оказалось\n")
        report.write("\nСамый большой файл:\n")

        if report_data["largest_file"]["path"]:
            report.write(f"{report_data['largest_file']['path']} ({report_data['largest_file']['size']} байт)\n")
        else:
            report.write("Не найдено\n")


dir = r'C:\Users\Sergey\Documents\gonna makeit'
output_report_path = r'C:\Users\Sergey\Documents\gonna makeit\REPORT!.txt'

data = scan_directory(dir)
generate_report(data, output_report_path)
print(f"отчет смотри в папке, которую я изучал.")
