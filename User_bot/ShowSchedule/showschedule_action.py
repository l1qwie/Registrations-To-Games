from User_bot.ShowSchedule.showschedule_database import CreateTable
from User_bot.ShowSchedule.showschedule_keyboard import GoTo
import subprocess
import used_by_everyone as forall

def HTML(html_table: str, name: str):
    with open(name, "w", encoding="UTF-8") as html_file:
        html_file.write('<html><head><meta charset="UTF-8"></head><body>')
        
        html_file.write('<style>table {margin: 0 auto; text-align: center;}</style>')
        html_file.write('<style>td {padding-top: 10px; padding-bottom: 10px;}</style>')
        html_file.write('<style>th {font-size: 25px; padding: 10px; color: #006400;}</style>')
        html_file.write("</head><body>")
        html_file.write('<style>body {background-color: #C0C0C0; color: #000000;}</style>')
        html_file.write(html_table)
        html_file.write("</body></html>")

    with open(name, "r", encoding="UTF-8") as html_file:
        return html_file.read()

def CreateHtmlFileAllSchedule(S: dict[str, str]):
    data:list[tuple[str, int, int, int, str]] = []
    html_table:str = ''
    row:tuple[str, int, int, int, str]
    seats:int = -1
    sport:str = ''
    date:int = -1
    time:int = -1
    gameaddress:str = ''

    data = CreateTable()
    html_table = "<table>"
    html_table += "<tr><th>Вид спорта</th><th>Дата проведения</th><th>Время проведения</th><th>Свободные места</th><th>Адрес</th></tr>"    

    for row in data:
        sport, date, time, seats, gameaddress = row
        time_str = forall.CreateTimeStr(time)
        date_str = forall.CreateDateStr(date)
        sport = S[sport]

        html_table += f"<tr><td>{sport}</td><td>{date_str}</td><td>{time_str}</td><td>{seats}</td><td>{gameaddress}</td></tr>"
    html_table += "</table>"
    HTML(html_table, "userhtml.html")

def CreateAFile(S: dict[str, str]) -> tuple[str, object, str]:

    res:subprocess.CompletedProcess[str]
    img:str = ''
    text:str = ''
    kbd:object = None

    CreateHtmlFileAllSchedule(S)
    res = subprocess.run("wkhtmltoimage userhtml.html Schedule.jpg", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res.returncode == 0:
        print("Файлы созданы и данные в них записаны.")
        img = 'Schedule.jpg'
        text = S["show_schedule"]
        kbd = GoTo(S["main_menu"])
    else:
        print('Произошла ошибка:')
        print(res.stderr)
    
    return text, kbd, img