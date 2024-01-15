from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn, testDataFitting
from Admin_bot.Activities.activities_keyboard import ActivitiesDirection
from Admin_bot.Activities.tests.activities_chatgame import HeadFunc as chatgameHeadFunc
from Admin_bot.Activities.tests.activities_activagame import HeadFunc as activegameHeadFunc
from Admin_bot.Activities.activities_database import SelectLengthChats, SelectLengthOfActiveGames, FindChats, SelectActiveGames
from Admin_bot.language_dictoinary import String as S
import language_dictionary_for_all as foralllang
import used_by_everyone as forall



def ChooseDir(text: str, kbd: object, lang: str):
    assert(text == S[lang]["Choose_dir_of_activities"] + S[lang]["rules_for_chat_game"])
    assert(kbd == ActivitiesDirection(S[lang]["reg_game"], S[lang]["activ_game"], foralllang.String[lang]["main_menu_kb"]))
    assert(1 == testSelectLevel(738070596))

def StartCreateChatGame(text: str, kbd: object, lang: str, phrase: str, launch_point: int, chatinf: list[tuple[int, str]]):
    length:int = SelectLengthChats()
    assert(text == S[lang]["game_rules"] + S[lang]["foundchats"])
    assert(kbd == forall.Chats(chatinf, 7, launch_point, length))
    assert(2 == testSelectLevel(738070596))
    assert(phrase == testSelectSomthingColumn(738070596, "direction"))

def NoChats(text: str, kbd: object, lang: str):
    assert(text == S[lang]["no_new_chats"] + S[lang]["Choose_dir_of_activities"] + S[lang]["rules_for_chat_game"])
    assert(kbd == ActivitiesDirection(S[lang]["reg_game"], S[lang]["activ_game"], foralllang.String[lang]["main_menu_kb"]))
    assert(1 == testSelectLevel(738070596))

def StartShowActiveGame(text: str, kbd: object, lang: str, phrase: str, schedule: list[tuple[int, str, int, int, int]], launch_point: int):
    input_schedule:list[tuple[str, str, str, str, str]] = []
    game_id:int = -1
    sport:str = ''
    date:int = -1
    time:int = -1
    seats:int = -1

    length = SelectLengthOfActiveGames()
    for game_id, sport, date, time, seats in schedule:
        input_schedule.append((str(game_id), sport, forall.CreateDateStr(date), forall.CreateTimeStr(time), str(seats)))

    assert(text == S[lang]["active_games"])
    assert(kbd == forall.Schedule(input_schedule, 7, launch_point, S[lang]["waiting_cl"], length))
    assert(2 == testSelectLevel(738070596))
    assert(phrase == testSelectSomthingColumn(738070596, "direction"))

def NothingToShow(text: str, kbd: object, lang: str):
    assert(text == S[lang]["no_active_games"] + S[lang]["Choose_dir_of_activities"] + S[lang]["rules_for_chat_game"])
    assert(kbd == ActivitiesDirection(S[lang]["reg_game"], S[lang]["activ_game"], foralllang.String[lang]["main_menu_kb"]))
    assert(1 == testSelectLevel(738070596))


def ChooseActivitiesDirection(first_message: list[str], lang: str):
    item:str = ''
    for item in first_message:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        ChooseDir(text, kbd, lang)
        assert(prmode == '')
        assert(halt == False)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)


def StartAct(directions: list[str], lang: str):
    item:str = ''
    for item in directions:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            launch_point = testSelectSomthingColumn(738070596, "activities_launch_point")
            print("HELP ME!", launch_point)
            if item == "create game":
                chatinf = FindChats(7, launch_point)
                if chatinf != []:
                    StartCreateChatGame(text, kbd, lang, item, launch_point, chatinf)
                else:
                    NoChats(text, kbd, lang)
            else:
                schedule = SelectActiveGames(7, launch_point)
                if schedule != []:
                    StartShowActiveGame(text, kbd, lang, item, schedule, launch_point)
                else:
                    NothingToShow(text, kbd, lang)
        else:
            ChooseDir(text, kbd, lang)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def DirectionOfActionActivities(alloflist:list[str], lang: str, level: int):
    testDataFitting("activities", level, 738070596)
    direction = testSelectSomthingColumn(738070596, "direction")
    if direction not in ("create game", "active games"):
        if level == 0:
            ChooseActivitiesDirection(alloflist, lang)
        elif level == 1:
            StartAct(alloflist, lang)
        else:
            assert(False)
    else:
        if direction == "create game":
            chatgameHeadFunc(alloflist, lang, level)
        elif direction == "active games":
            activegameHeadFunc(alloflist, lang, level)
