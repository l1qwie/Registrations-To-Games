from User_bot.Media.media_database import FindSomeMedia, FoundSomePhotosInLastGamesSchedule, FoundSomeverInLastGamesSchedule, FoundSomePhotosInSchedule, FoundSomeverInSchedule, CreateListOfViewGamesForLastGames, CreateListOfViewGames
from User_bot.Media.media_database import CreateListOfLoadGamesForLastGames, CreateListOfLoadGames, SelectMediaDelGame, CheckGameId, CoutFreeSeatsOfFile
from User_bot.Media.media_keyboard import DirectionBouth, DirectionOnce, TimeInterval, OneTimeInterval, GoTo, EndMediaGroup, TryAgain
from User_bot.Main.tests.main_database_test import testSelectSomthingColumn, testSelectLevel, testSelectCounterFiles, testDataFitting
from User_bot.Main.main_action import DispatchPhrase, DispatchMedia
from User_bot.language_dictionary import Strings as S
import used_by_everyone as forall
import language_dictionary_for_all

#helper functions

#action funtions
def StartAction(text: str, kbd: object, lang: str):
    assert(text == S[lang]["direction"])
    assert(0 == testSelectSomthingColumn(738070596, "counter_mediagroup"))
    assert(1 == testSelectLevel(738070596))
    if FindSomeMedia():
        assert(kbd == DirectionBouth(S[lang]["kbload"], S[lang]["kbview"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
    else:
        assert(kbd == DirectionOnce(S[lang]["kbload"], language_dictionary_for_all.String[lang]["main_menu_kb"]))

def SorryNothingHere(text: str, kbd: object, lang: str):
    assert(text == S[lang]["nothing_there"] + language_dictionary_for_all.String[lang]["main_menu_text"])
    assert(kbd == forall.Options(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"]))
    assert(3 == testSelectLevel(738070596))
    assert("divarication" == testSelectSomthingColumn(738070596, "action"))

def CheckDirection(text: str, kbd: object, lang: str, phrase: str):
    assert(phrase == testSelectSomthingColumn(738070596, "media_direction"))
    assert(2 == testSelectLevel(738070596))
    if (FoundSomePhotosInLastGamesSchedule()) or (FoundSomeverInLastGamesSchedule()):
        assert(text == S[lang]["time"])
        assert(kbd == TimeInterval(S[lang]["kblastgames"], S[lang]["kball_of_rest"]))
    else:
        if (phrase == "viewing") and (not FoundSomePhotosInLastGamesSchedule()) and (not FoundSomePhotosInSchedule()):
            assert(text == S[lang]["nothing_to_watch"] + S[lang]["direction"])
            if FindSomeMedia():
                assert(kbd == DirectionBouth(S[lang]["kbload"], S[lang]["kbview"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
            else:
                assert(kbd == DirectionOnce(S[lang]["kbload"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
        elif (phrase == "loading") and (not FoundSomeverInLastGamesSchedule()) and (not FoundSomeverInSchedule()):
            assert(text == S[lang]["nothing_to_load"] + S[lang]["direction"])
            if FindSomeMedia():
                assert(kbd == DirectionBouth(S[lang]["kbload"], S[lang]["kbview"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
            else:
                assert(kbd == DirectionOnce(S[lang]["kbload"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
        else:
            assert(text == S[lang]["time"])
            assert(kbd == OneTimeInterval(S[lang]["kball_of_rest"]))

def ShowGames(text: str, kbd: object, lang: str, phrase: str):
    schedule_from_db:list[tuple[int, str, int, int]] = []
    schedule:list[tuple[str, str, str, str]] = []
    length:int = -1
    launch_point:int = testSelectSomthingColumn(738070596, "media_launch_point")
    media_direction:str = testSelectSomthingColumn(738070596, "media_direction")

    assert(text == S[lang][phrase])
    interval:str = testSelectSomthingColumn(738070596, "media_time_interval")
    if media_direction == "viewing":
        if interval == "last_game":
            schedule_from_db, length = CreateListOfViewGamesForLastGames(7, launch_point)
        else:
            schedule_from_db, length = CreateListOfViewGames(7, launch_point)
    else:
        if interval == "last_game":
            schedule_from_db, length = CreateListOfLoadGamesForLastGames(7, launch_point)
        else:
            schedule_from_db, length = CreateListOfLoadGames(7, launch_point)
    _trash_, schedule = forall.SheduleStr([], schedule_from_db, lang)
    assert(kbd == forall.Schedule(schedule, 7, launch_point, '', length))
    assert(phrase == testSelectSomthingColumn(738070596, "media_time_interval"))
    assert(3 == testSelectLevel(738070596))

def ShowMedia(text: str, kbd: object, lang: str, phrase: str, file_id: list[str], typeoffile: list[str]):
    files_id_test:list[str] = []
    typesoffiles_test:list[str] = []
    files_id_test, typesoffiles_test = SelectMediaDelGame(738070596)

    assert(text == S[lang]["all_media"])
    assert(kbd == GoTo(S[lang]["main_menu"]))
    assert(file_id == files_id_test)
    assert(typeoffile == typesoffiles_test)
    assert(3 == testSelectLevel(738070596))
    assert(int(phrase) == testSelectSomthingColumn(738070596, "del_game_game_id"))

def BotWasFall(text: str, kbd: object, lang: str):
    assert(text == S[lang]["its_not_time_yet"])
    assert(kbd == forall.Options(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"]))
    assert(4 == testSelectLevel(738070596))
    
def StartDowloading(text: str, kbd: object, lang: str, phrase: str, freefilesseats: int):
    assert(text == S[lang]["Can_downloaded"] % (freefilesseats))
    assert(kbd == GoTo(S[lang]["main_menu"]))
    assert(4 == testSelectLevel(738070596))
    assert(int(phrase) == testSelectSomthingColumn(738070596, "del_game_game_id"))

def NotEnogthSpace(text: str, kbd: object, lang: str, phrase: str):
    assert(text == S[lang]["cant_download"])
    assert(kbd == forall.Options(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"]))
    assert(3 == testSelectLevel(738070596))
    assert("divarication" == testSelectSomthingColumn(738070596, "action"))
    assert(int(phrase) == testSelectSomthingColumn(738070596, "del_game_game_id"))

def SaveToUser(text: str, kbd: object, lang: str, counter:int, edit: bool):
    assert(text == S[lang]["loading_in_progress"] % (counter))
    assert(kbd == EndMediaGroup(S[lang]["all_loaded"]))
    assert(counter == testSelectSomthingColumn(738070596, "counter_mediagroup"))
    if counter > 1:
        assert(edit == True)
    else:
        assert(edit == False)

def CantSaveToUser(text: str, kbd: object, lang: str):
    assert(text == S[lang]["violation"])
    assert(kbd == GoTo(S[lang]["main_menu"]))

def SaveMedia(text: str, kbd: object, lang: str):
    counter:int = testSelectSomthingColumn(738070596, "counter_mediagroup")
    game_id:int = testSelectSomthingColumn(738070596, "del_game_game_id")
    counter_files:int = testSelectCounterFiles(game_id)
    if (counter_files + counter) <= 20:
        assert(text == S[lang]["grac_to_download"] % (counter))
        assert(kbd == GoTo(S[lang]["main_menu"]))
    else:
        if counter_files == 0:
            assert(text == S[lang]["no_data"])
            assert(kbd == GoTo(S[lang]["main_menu"]))
        else:
            print(counter, counter_files)
            assert(text == S[lang]["somthingwrong"] % (counter, 20 - (counter_files-counter), 20 - (counter_files-counter)))
            assert(kbd == TryAgain(S[lang]["all_good"], S[lang]["not_all_good"]))
            assert(5 == testSelectLevel(738070596))

def SaveAgain(text: str, kbd: object, lang: str, halt: bool):

    counter:int = testSelectSomthingColumn(738070596, "counter_mediagroup")
    print(counter)
    if halt:
        assert(text == S[lang]["success"] % (counter))
    else:
        assert(text == S[lang]["wrong_again"])
    assert(kbd == forall.Options(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"]))
    assert(3 == testSelectLevel(738070596))
    assert("divarication" == testSelectSomthingColumn(738070596, "action"))




#header functions
def FirstQuestion(first_message: list[str], lang: str):
    item:str = ''
    for item in first_message:
        testDataFitting("photos&videos", 0, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        if halt:
            StartAction(text, kbd, lang)
        else:
            SorryNothingHere(text, kbd, lang)
        assert(prmode == '')
        assert(address == [])
        assert(img == '')
        assert(edit == False)
        assert(files_id == [])
        assert(typeoffile == [])


def ChoiceOfDirection(directions: list[str], lang: str):
    item:str = ''
    for item in directions:
        testDataFitting("photos&videos", 1, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        if halt:
            CheckDirection(text, kbd, lang, item)
        else:
            StartAction(text, kbd, lang)
        assert(prmode == '')
        assert(address == [])
        assert(img == '')
        assert(edit == False)
        assert(files_id == [])
        assert(typeoffile == [])

def WhatGamesNeedToShow(howmuthgames: list[str], lang: str):
    item:str = ''
    for item in howmuthgames:
        testDataFitting("photos&videos", 2, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        if halt:
            ShowGames(text, kbd, lang, item)
        else:
            media_direction:str = testSelectSomthingColumn(738070596, "media_direction")
            CheckDirection(text, kbd, lang, media_direction)
        assert(prmode == '')
        assert(address == [])
        assert(img == '')
        assert(edit == False)
        assert(files_id == [])
        assert(typeoffile == [])

def CreateMediaList(selected_games: list[str], lang: str):  
    item:str = ''
    for item in selected_games:
        testDataFitting("photos&videos", 3, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        media_time_interval:str = testSelectSomthingColumn(738070596, "media_time_interval")
        if halt == False and item == "next page":
            ShowGames(text, kbd, lang, media_time_interval)
        elif halt:
            if CheckGameId(int(item)):
                if files_id != []:
                    ShowMedia(text, kbd, lang, item, files_id, typeoffile)
                else:
                    BotWasFall(text, kbd, lang)
            else:
                ShowGames(text, kbd, lang, media_time_interval)
        else:
            ShowGames(text, kbd, lang, media_time_interval)
        assert(prmode == '')
        assert(address == [])
        assert(img == '')
        assert(edit == False)

def StartLoading(selected_games: list[str], lang: str):
    item:str = ''
    for item in selected_games:
        testDataFitting("photos&videos", 3, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        media_time_interval:str = testSelectSomthingColumn(738070596, "media_time_interval")
        if forall.IntCheck(item):
            if halt:
                filesseats = CoutFreeSeatsOfFile(int(item))
                if filesseats != 20:
                    new = 20 - filesseats
                    StartDowloading(text, kbd, lang, item, new)
                else:
                    NotEnogthSpace(text, kbd, lang, item)
            else:
                ShowGames(text, kbd, lang, media_time_interval)
        else:
            ShowGames(text, kbd, lang, media_time_interval)
        assert(prmode == '')
        assert(address == [])
        assert(img == '')
        assert(edit == False)
        assert(files_id == [])
        assert(typeoffile == [])


def InspectionFileId(file_id_list: list[str], lang: str):
    #item:str = ''
    i:int = 0
    while i < len(file_id_list):
        testDataFitting("photos&videos", 4, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, edit)= DispatchMedia(738070596, file_id_list[i], "44", "photo", lang)
        #if i == 1: 
        if halt:
            counter_media = testSelectSomthingColumn(738070596, "counter_mediagroup")
            SaveToUser(text, kbd, lang, counter_media, edit)
        else:
            CantSaveToUser(text, kbd, lang)
        assert(prmode == '')
        assert(address == [])
        assert(img == '')
        assert(files_id == [])
        i += 1

def SaveToMediaRep(endofload: list[str], lang: str):
    item:str = ''
    for item in endofload:
        testDataFitting("photos&videos", 4, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        if item == "END":
            SaveMedia(text, kbd, lang)
        else:
            assert(text == S[lang]["pleese_ckick_to_button"])
            assert(kbd == EndMediaGroup(S[lang]["all_loaded"]))
        assert(prmode == '')
        assert(address == [])
        assert(img == '')
        assert(edit == False)
        assert(files_id == [])
        assert(typeoffile == [])
        print(halt)


def TryAgainToSave(second_try: list[str], lang: str):
    item:str = ''
    for item in second_try:
        testDataFitting("photos&videos", 5, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        if item == "try again":
            SaveAgain(text, kbd, lang, halt)
        else:
            assert(text == S[lang]["not_completely"])
            assert(TryAgain(S[lang]["all_good"], S[lang]["not_all_good"]))
        assert(prmode == '')
        assert(address == [])
        assert(img == '')
        assert(edit == False)
        assert(files_id == [])
        assert(typeoffile == [])
        print(halt)