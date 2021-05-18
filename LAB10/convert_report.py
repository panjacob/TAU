import json
from datetime import datetime

import xlsxwriter


# Plik json generowany jest za pomoca: pytest --json-report -v

def get_json(report_path='../.report.json'):
    f = open(report_path, "r")
    report_string = f.read()
    report_json = json.loads(report_string)
    return report_json


def write_info(worksheet, report_json):
    worksheet.write(0, 0, "Python")
    worksheet.write(0, 1, report_json['environment']['Python'])

    worksheet.write(1, 0, "Platform")
    worksheet.write(1, 1, report_json['environment']['Platform'])

    worksheet.write(2, 0, "Duration [s]")
    worksheet.write(2, 1, f"{report_json['duration']}")

    worksheet.write(3, 0, "Pass rate")
    worksheet.write(3, 1, f"{report_json['summary']['passed']}/{report_json['summary']['total']}")

    worksheet.write(4, 0, "Data")
    worksheet.write(4, 1, get_today_date())
    return worksheet


def write_tests(worksheet, report_json, row):
    worksheet.write(row - 1, 0, "Name")
    worksheet.write(row - 1, 1, "Description")
    worksheet.write(row - 1, 2, "Expected")
    worksheet.write(row - 1, 3, "Result")
    worksheet.write(row - 1, 4, "Priority")
    worksheet.write(row - 1, 5, "Duration [s]")
    worksheet.write(row - 1, 6, "Execution date")
    worksheet.write(row - 1, 7, "Owner")
    for i, test in enumerate(report_json['tests']):
        worksheet.write(row + i, 0, test['nodeid'])
        worksheet.write(row + i, 1, f"{test['keywords']}")
        worksheet.write(row + i, 2, "passed")
        worksheet.write(row + i, 3, test['outcome'])
        worksheet.write(row + i, 4, 1)
        worksheet.write(row + i, 5, f"{test['call']['duration']}")
        worksheet.write(row + i, 6, get_today_date())
        worksheet.write(row + i, 7, "Jakub Kwiatkowski")
        print(test)


def get_report_excel(report_json=get_json(), path='', filename='report.xlsx'):
    workbook = xlsxwriter.Workbook(path + filename)
    worksheet = workbook.add_worksheet()
    worksheet = write_info(worksheet, report_json)
    write_tests(worksheet, report_json, row=8)

    workbook.close()


def get_today_date():
    now = datetime.now()
    return now.strftime("%d/%m/%Y")


get_report_excel()
