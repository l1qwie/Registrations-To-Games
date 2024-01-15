from Admin_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn, testDataFitting
from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.language_dictoinary import String as S
from Admin_bot.Game.game_keyboard import GamesOptions, KindOfSport
from Admin_bot.Game.game_database import ScheduleOfGames, LengthOfGames
from Admin_bot.Game.tests.creategames_tester import CreateDiraction
from Admin_bot.Game.tests.deletegames_tester import DeleteGame
from Admin_bot.Game.tests.changegames_tester import ChangeDiraction
from language_dictionary_for_all import String
import used_by_everyone as forall

#Action functions
def Directions(text: str, kbd: object, lang: str):
    assert(text == S[lang]["games_directions"])
    assert(kbd == GamesOptions(S[lang]["change_games"], S[lang]["create_games"], S[lang]["delete_games"]))
    assert(1 == testSelectLevel(738070596))

def DirOfChangeOrDelete(text: str, kbd: object, lang: str, launch_point: int):

    schedule_output:list[tuple[str, str, str, str]] = []
    schedule_input:list[tuple[int, str, int, int]] = ScheduleOfGames(launch_point, 7)
    length:int = LengthOfGames()
    _schedule_, schedule_output = forall.SheduleStr([], schedule_input, lang)
    assert(text == S[lang]["choose_game"])
    assert(kbd == forall.Schedule(schedule_output, 7, launch_point, '', length))
    assert(2 == testSelectLevel(738070596))

def DirOfCreate(text: str, kbd: object, lang: str):
    assert(text == S[lang]["start_create_game"])
    assert(kbd == KindOfSport(String[lang]["volleyball"], String[lang]["football"], String[lang]["main_menu_kb"]))
    assert(2 == testSelectLevel(738070596))



#Header functions
def ChooseDiraction(directions: list[str], lang: str):
    item:str = ''
    for item in directions:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        Directions(text, kbd, lang)
        assert(prmode == '')
        assert(halt == False)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def DirectionsOfDirection(directions2: list[str], lang: str):
    item:str = ''
    for item in directions2:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            launch_point:int = testSelectSomthingColumn(738070596, "game_launch_point")
            if item in ("change games", "delete games", "previous page", "next page"):
                DirOfChangeOrDelete(text, kbd, lang, launch_point)
            elif item == "create games":
                DirOfCreate(text, kbd, lang)
            assert(item == testSelectSomthingColumn(738070596, "direction"))
        else:
            Directions(text, kbd, lang)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)


def ActionWithGame(data_list:list[str], lang: str, level: int):
    direction = testSelectSomthingColumn(738070596, "direction")
    testDataFitting("game", level, 738070596)
    if direction not in ("create games", "change games", "delete games"):
        if level == 0:
            ChooseDiraction(data_list, lang)
        elif level == 1:
            DirectionsOfDirection(data_list, lang)
        else:
            assert(False)
    else:
        if direction == "create games":
            CreateDiraction(data_list, lang, level)
        elif direction == "change games":
            ChangeDiraction(data_list, lang, level)
        elif direction == "delete games":
            DeleteGame(data_list, lang, level)



def HeadOfGame(alloflist:list[str], lang: str, level: int):
    i:int = 0
    while i <= 10:
        testDataFitting("games", i, 738070596)
        direction = testSelectSomthingColumn(738070596, "direction")
        if direction == '':
            if level == 0:
                ChooseDiraction(alloflist, lang)
            elif level == 1:
                DirectionsOfDirection(alloflist, lang)
            else:
                assert(False)
        else:
            if direction == "create games":
                CreateDiraction(alloflist, lang, level)
            elif direction == "change games":
                pass
            elif direction == "delete games":
                DeleteGame(alloflist, lang, level)
            else:
                assert(False)
        i += 1
        