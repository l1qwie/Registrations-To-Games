
from Admin_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn, SelectGameStatus, testDataFitting
from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.language_dictoinary import String as S
from Admin_bot.Game.game_keyboard import AnotherFunc
from Admin_bot.Game.game_database import ScheduleOfGames, LengthOfGames
import language_dictionary_for_all
import used_by_everyone as forall


def CorrectPhrase(text: str, kbd: object, lang: str, launch_point: int):
    schedule_output:list[tuple[str, str, str, str]] = []
    schedule_input:list[tuple[int, str, int, int]] = ScheduleOfGames(launch_point, 7)
    length:int = LengthOfGames()
    _schedule_, schedule_output = forall.SheduleStr([], schedule_input, lang)
    assert(text == S[lang]["choose_game"])
    assert(kbd == forall.Schedule(schedule_output, 7, launch_point, '', length))
    assert(2 == testSelectLevel(738070596))

def CorrectGameId(text: str, kbd: object, lang: str, phrase: str):
    assert(text == S[lang]["game_removed"])
    assert(kbd == AnotherFunc(S[lang]["change_games"], S[lang]["create_games"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
    assert(1 == testSelectLevel(738070596))
    assert(True == SelectGameStatus(int(phrase)))



def DeleteGame(deletephrases: list[str], lang: str, level: int):
    item:str = ''
    for item in deletephrases:
        testDataFitting("game", 2, 738070596)
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            CorrectGameId(text, kbd, lang, item)
        else:
            launch_point = testSelectSomthingColumn(738070596, "game_launch_point")
            print("launch_point =", launch_point)
            CorrectPhrase(text, kbd, lang, launch_point)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)