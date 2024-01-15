from Admin_bot.Welcome.tests.welcome_tester import FirstMessage, EnterPassword, ShowRules, ShowMenu
from Admin_bot.Main.tests.main_database_test import testSelectSomthingColumn, SelectGameId, ChangeDir, ResetAllLaunchPoints, SelectNewUserId, SelectChatId
from Admin_bot.Main.tests.main_database_test import ConnectTo as mainConnectTo
from Admin_bot.Game.tests.game_tester import ActionWithGame
from Admin_bot.Game.game_database import ConnectTo as gameConnectTo
from Admin_bot.Clients.tests.clients_tester import DirectionOfActionClients
from Admin_bot.Clients.clients_database import ConnectTo as clientsConnectTo
from Admin_bot.Activities.tests.activites_tester import DirectionOfActionActivities as actDirectionOfActionActivities
from Admin_bot.Money.tests.money_tester import DirectionOfActionActivities as moneyDirectionOfActionActivities
from Admin_bot.Settings.tests.settings_tester import DirectionOfActionSettings
from Admin_bot.secretdata import phiz_host, phiz_user, phiz_password, phiz_db_name
import random
import used_by_everyone as forall
import tools

def CreateGame() -> int:
    tools.ChangeAdmin(738070596, 'game_game_id', '-1', 'int')
    tools.ResetForCreateGame(738070596)
    date_int:int = tools.RandomFutureDate()
    date:str = forall.CreateDateStr(date_int)
    sport, time_int, seats, status, latitude, longitude, address, price, currency = tools.CreateRandomGameInSchedule()
    time:str = forall.CreateTimeStr(time_int)
    print(status)

    first_message:list[str] = ["qweqw dqw","12311231", "asdasae"]
    directions:list[str] = ["1231313", "adadewq", "create games"]
    sports:list[str] = ["1231asdd", "asdjklasdjkl", f"{sport}"]
    dates:list[str] = ["31231231", "aklsdakl;sd", f"{date}"]
    times:list[str] = ["13131", "asdjasjkd", f"{time}"]
    seats_list:list[str] = ["12qeqweq", "1ajklmsdjklasdj", f"{seats}"]
    links:list[str] = ["ajknsdijad", "1kj23jkl111", f"https://www.google.com/maps?q={latitude},{longitude}"]
    nameaddress:list[str] = [f"{address}"]
    prices:list[str] = ["asnjkldaijklod", "ADJKASJKDAJKL", f"{price}"]
    currences:list[str] = [f"{currency}"]
    commands:list[str] = ["12678317", "adkl;askiop", "save"]

    all_of_lists:list[list[str]] = [first_message, directions, sports, dates, times, seats_list, prices, currences, links, nameaddress, commands]
    lang = testSelectSomthingColumn(738070596, "language")
    level = 0
    while level <= 10:
        ActionWithGame(all_of_lists[level], lang, level)
        level += 1
    game_id = SelectGameId()
    return game_id 

def ChangeGame(game_id: int):
    tools.ChangeAdmin(738070596, 'game_game_id', '-1', 'int')
    ChangeDir(738070596)
    date:int = tools.RandomFutureDate()
    sport, time_int, seats, status, latitude, longitude, address, price, currency = tools.CreateRandomGameInSchedule()
    print("trash", status)
    datas:list[str] = [f"{sport}", f"{forall.CreateDateStr(date)}", f"{forall.CreateTimeStr(time_int)}", f"{seats}", f"{price}", f"{currency}", f"https://www.google.com/maps?q={latitude},{longitude}", f"{address}"]


    first_message:list[str] = ["qweqw dqw","12311231", "asdasae"]
    directions:list[str] = ["1231313", "adadewq", "change games"]
    game_ids:list[str] = ["126783178ea", "asjkldasjkdiakls", f"{game_id}"]
    change_dir:list[str] = ["1231asdd", "asdjklasdjkl"]
    subsequence:list[str] = ["sport", "date", "time", "seats", "price", "currency", "link", "address"]
    change_data:list[str] = ["ASDJKASJK!@#JKASKD!@#E!", "aklsdakl;sd"]
    change_another:list[str] = ["ajknsdjklasdk", "12367rrfr1231", "another data change"]

    lang = testSelectSomthingColumn(738070596, "language")

    ActionWithGame(first_message, lang, 0)
    ActionWithGame(directions, lang, 1)
    ActionWithGame(game_ids, lang, 2)

    i: int = 0

    while i < len(datas):
        change_dir.append(subsequence[i])
        if subsequence[i] in ("currency", "address"):
            change_data.pop()
            change_data.pop()
        change_data.append(datas[i])
        all_of_lists:list[list[str]] = [change_dir, change_data, change_another]
        level:int = 3 
        while level <= 5:
            ActionWithGame(all_of_lists[level-3], lang, level)
            level += 1
        if subsequence[i] in ("currency", "address"):
            change_data:list[str] = ["1231asdd", "asdjklasdjkl", "asdasd"]
        change_dir.pop()
        change_data.pop()
        i += 1

def RemoveGame(game_id: int):
    tools.ChangeAdmin(738070596, 'game_game_id', '-1', 'int')
    ChangeDir(738070596)
    lang = testSelectSomthingColumn(738070596, "language")

    first_message:list[str] = ["qweqw dqw","12311231", "asdasae"]
    directions:list[str] = ["1231313", "adadewq", "delete games"]
    game_ids:list[str] = ["126783178ea", "asjkldasjkdiakls", f"{game_id}"]


    ActionWithGame(first_message, lang, 0)
    ActionWithGame(directions, lang, 1)
    ActionWithGame(game_ids, lang, 2)

def CheckAdditionalButtonsGames():
    ResetAllLaunchPoints(738070596)
    tools.ChangeAdmin(738070596, 'game_game_id', '-1', 'int')
    ChangeDir(738070596)
    game_ids:list[int] = []
    i:int = 0
    while i < 16:
        game_id = tools.HeadOfCreateFutureGames()
        game_ids.append(game_id)
        i += 1

    lang = testSelectSomthingColumn(738070596, "language")
    
    first_message:list[str] = ["qweqw dqw","12311231", "asdasae"]
    directions:list[str] = ["1231313", "adadewq", "change games"]
    next:list[str] = ["ajklsdjklasjkld", "!#@#!!@#", "next page"]
    previous:list[str] = ["ASNDJKAJKS", "!#!@#!@%SDASD", "previous page"]
    buttons:list[list[str]] = [next, previous]

    ActionWithGame(first_message, lang, 0)
    ActionWithGame(directions, lang, 1)
    i = 0
    while i < 2:
        ActionWithGame(buttons[i], lang, 2)
        i += 1

    i = 0
    while i < 16:
        tools.DeleteGameInSchedule(game_ids[i])
        i += 1

def CreateClient():

    ChangeDir(738070596)
    clientsConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    lang = testSelectSomthingColumn(738070596, "language")
    name, last_name, phone, fw = tools.CreateInfUser()

    first_message:list[str] = ["qweqw dqw","12311231", "asdasae"]
    directions:list[str] = ["1231313", "adadewq", "create client"]
    from_wheres:list[str] = ["126783178ea", "asjkldasjkdiakls", f"{fw}"]
    names:list[str] = [f"{name}"]
    last_names:list[str] = [f"{last_name}"]
    phones:list[str] = ["126783178ea", "asjkldasjkdiakls", f"{phone}"]
    saveorchanges:list[str] = ["askl;dkl;asdkl;", "1231231", "save"] #save or change

    alloflist:list[list[str]] = [first_message, directions, from_wheres, names, last_names, phones, saveorchanges]
    i:int = 0
    while i <= 6:
        DirectionOfActionClients(alloflist[i], lang, i)
        i += 1

    user_id:int = SelectNewUserId()    
    tools.DeleteUsers(user_id)

def ChangeClient():
    user_id = tools.CreateUser()


    ChangeDir(738070596)
    clientsConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    lang = testSelectSomthingColumn(738070596, "language")
    name, last_name, phone, fw = tools.CreateInfUser()

    datas:list[str] = [f"{fw}", f"{name}", f"{last_name}", f"{phone}"]
    directionsofchange:list[str] = ["from_where", "name", "last_name", "phone_number"]
    change_another:list[str] = ["ajknsdjklasdk", "123671231", "another data change"]

    first_message:list[str] = ["qweqw dqw","12311231", "asdasae"]
    directions:list[str] = ["1231313", "adadewq", "change client"]
    user_ids:list[str] = ["asjkldjklasdk", "31uih312uihj3", f"{user_id}"]

    change_dir:list[str] = ["ajklsdjklad", "13231312"]
    change_data:list[str] = ["!#!@#!#!!Q#Q!#@!!#!@#", "dasasdas"]

    DirectionOfActionClients(first_message, lang, 0)
    DirectionOfActionClients(directions, lang, 1)
    DirectionOfActionClients(user_ids, lang, 2)


    i:int = 0
    while i < len(datas):
        change_dir.append(directionsofchange[i])
        if directionsofchange[i] in ("name", "last_name"):
            change_data.pop()
            change_data.pop()
        change_data.append(datas[i])

        all_of_lists:list[list[str]] = [change_dir, change_data, change_another]
        level = 3
        while level <= 5:
            DirectionOfActionClients(all_of_lists[level-3], lang, level)
            level += 1
    
        if directionsofchange[i] in ("name", "last_name"):
            change_data = ["!#!@#!#!!Q#Q!#@!!#!@#", "dasasdas"]
        change_dir.pop()
        i += 1
    
    tools.DeleteUsers(user_id)

def DeleteClient():
    user_id = tools.CreateUser()

    ChangeDir(738070596)
    clientsConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    lang = testSelectSomthingColumn(738070596, "language")

    first_message:list[str] = ["qweqw dqw","12311231", "asdasae"]
    directions:list[str] = ["1231313", "adadewq", "delete client"]
    user_ids:list[str] = ["asjkldjklasdk", "31uih312uihj3", f"{user_id}"]

    DirectionOfActionClients(first_message, lang, 0)
    DirectionOfActionClients(directions, lang, 1)
    DirectionOfActionClients(user_ids, lang, 2)

    tools.DeleteUsers(user_id)

def RegToGame():
    tools.ChangeAdmin(738070596, 'direction', '', 'str')
    tools.ChangeAdmin(738070596, 'level', 0, 'int')
    user_id = tools.CreateUser()
    game_id = tools.HeadOfCreateFutureGames()
    clientsConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    gameConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    pay:list[str] = ["cash", "card"]

    first_message:list[str] = ["qweqw dqw","12311231", "asdasae"]
    directions:list[str] = ["1231313", "adadewq", "reg client to game"]
    user_ids:list[str] = ["asjkldjklasdk", "31uih312uihj3", f"{user_id}"]
    game_ids:list[str] = ["dasjkldjklasdkl", "!#W!!!@#!Q@#!@#!", f"{game_id}"]
    seatslist:list[str] = ["ASDASJKL", "asdaasdsq", f"{random.randint(1, 10)}"]
    paymethods:list[str] = ["asjkldJKL", "!@##!@#!!@#", f"{pay[random.randint(0, 1)]}"]

    alloflist:list[list[str]] = [first_message, directions, user_ids, game_ids, seatslist, paymethods]
    lang = testSelectSomthingColumn(738070596, "language")

    i:int = 0
    while i < len(alloflist):
        DirectionOfActionClients(alloflist[i], lang, (i))
        i += 1

    tools.DeleteAllWaitGames()
    tools.DeleteUsers(user_id)
    tools.DeleteGameInSchedule(game_id)
    
def CheckAdditionalButtonsClients():
    ResetAllLaunchPoints(738070596)
    tools.ChangeAdmin(738070596, 'direction', '', 'str')
    tools.ChangeAdmin(738070596, 'level', 0, 'int')
    user_ids:list[int] = []
    i:int = 0
    while i < 16:
        user_id = tools.CreateUser()
        user_ids.append(user_id)
        i += 1
    first_message:list[str] = ["qweqw dqw","12311231", "asdasae"]
    directions:list[str] = ["1231313", "adadewq", "change client"]
    next:list[str] = ["ajklsdjklasjkld", "!#@#!!@#", "next page"]
    previous:list[str] = ["ASNDJKAJKS", "!#!@#!@%SDASD", "previous page"]
    buttons:list[list[str]] = [next, previous]
    lang = testSelectSomthingColumn(738070596, "language")

    DirectionOfActionClients(first_message, lang, 0)
    DirectionOfActionClients(directions, lang, 1)
    i = 0
    while i < 2:
        DirectionOfActionClients(buttons[i], lang, 2)
        i += 1

    i = 0
    while i < 16:
        tools.DeleteUsers(user_ids[i])
        i += 1

def CheckAdditionalButtonsClientsWithGames():
    ResetAllLaunchPoints(738070596)
    tools.ChangeAdmin(738070596, 'direction', '', 'str')
    tools.ChangeAdmin(738070596, 'level', 0, 'int')
    user_ids:list[int] = []
    game_ids:list[int] = []
    i:int = 0
    while i < 16:
        game_id = tools.HeadOfCreateFutureGames()
        game_ids.append(game_id)
        user_id = tools.CreateUser()
        user_ids.append(user_id)
        i += 1
    first_message:list[str] = ["qweqw dqw","12311231", "asdasae"]
    directions:list[str] = ["1231313", "adadewq", "reg client to game"]
    exemple:list[str] = ['AMJKLSDKL', "!@#!@&#$P", f"{user_ids[7]}"]
    next:list[str] = ["ajklsdjklasjkld", "!#@#!!@#", "next page"]
    previous:list[str] = ["ASNDJKAJKS", "!#!@#!@%SDASD", "previous page"]
    lang = testSelectSomthingColumn(738070596, "language")
    buttons:list[list[str]] = [next, previous]


    DirectionOfActionClients(first_message, lang, 0)
    DirectionOfActionClients(directions, lang, 1)
    i = 0
    while i < 2:
        DirectionOfActionClients(buttons[i], lang, 2)
        i += 1
    DirectionOfActionClients(exemple, lang, 2)
    i = 0
    while i < 2:
        DirectionOfActionClients(buttons[i], lang, 3)
        i += 1

    i = 0
    while i < 16:
        tools.DeleteGameInSchedule(game_ids[i])
        tools.DeleteUsers(user_ids[i])
        i += 1

def ThereExist():
    #chat_id = tools.AddSomeChats()
    chat_id = SelectChatId()
    game_id = tools.HeadOfCreateFutureGames()
    tools.ChangeAdmin(738070596, 'direction', 'create game', 'str')
    languages:list[str] = ["ru", "en", "tur"]

    chat_ids:list[str] = ["aiolsjkdklas", "12313asd12", f"{chat_id}"]
    game_ids:list[str] = ["ajksdajkldajk", "13121kl23jkl1", f"{game_id}"]
    choose_lang:list[str] = ["aklsdklasd", "A#@!O#!#!", f"{languages[random.randint(0, 2)]}"]

    sendcomms:list[str] = ["jklqdjklasjkl", "!W!QW!Q@!#!#!", "send"]

    lang = testSelectSomthingColumn(738070596, "language")
    alloflist:list[list[str]] = [chat_ids, game_ids, choose_lang, sendcomms]

    i:int = 0
    while i < len(alloflist):
        actDirectionOfActionActivities(alloflist[i], lang, (i+2))
        i += 1
    #tools.DeleteAllChats()
    #tools.DeleteGameInSchedule(game_id)

def ShowChats(first_message: list[str], directions: list[str]):
    ChangeDir(738070596)
    tools.ChangeAdmin(738070596, 'level', 0, 'int')

    alloflist:list[list[str]] = [first_message, directions]
    lang = testSelectSomthingColumn(738070596, "language")

    i:int = 0
    while i < len(alloflist):
        actDirectionOfActionActivities(alloflist[i], lang, i)
        i += 1
    tools.ChangeAdmin(738070596, 'direction', 'create game', 'str')
    ThereExist()

def AddChat(first_message: list[str], directions: list[str]):
    ChangeDir(738070596)
    tools.ChangeAdmin(738070596, 'level', 0, 'int')
    chat_id = tools.AddSomeChats()
    game_id = tools.HeadOfCreateFutureGames()
    dirofdirection:list[str] = ["aiolsjkdklas", "12313asd12", "add new chat"]

    chat_ids:list[str] = ["aiolsjkdklas", "12313asd12", f"{chat_id}"]
    game_ids:list[str] = ["ajksdajkldajk", "13121kl23jkl1", f"{game_id}"]
    sendcomms:list[str] = ["jklqdjklasjkl", "!W!QW!Q@!#!#!", "send"]

    alloflist:list[list[str]] = [first_message, directions, dirofdirection, chat_ids, game_ids, sendcomms]
    lang = testSelectSomthingColumn(738070596, "language")

    i:int = 0
    while i < len(alloflist):
        actDirectionOfActionActivities(alloflist[i], lang, i)
        i += 1

    tools.DeleteAllChats()
    tools.DeleteGameInSchedule(game_id)

def NothingThereToShowGames(first_message: list[str], directions: list[str]):
    ChangeDir(738070596)
    tools.ChangeAdmin(738070596, 'level', 0, 'int')
    tools.DeleteAllWaitGames()
    tools.DeleteAllUsers()
    tools.DeleteAllWaitGames()
    lang = testSelectSomthingColumn(738070596, "language")

    actDirectionOfActionActivities(first_message, lang, 0)
    actDirectionOfActionActivities(directions, lang, 1)

def ShowGames(first_message: list[str], directions: list[str]):
    ChangeDir(738070596)
    tools.ChangeAdmin(738070596, 'level', 0, 'int')
    user_id = tools.CreateUser()
    game_id = tools.HeadOfCreateFutureGames()
    tools.RegistrationUserToGames(user_id, game_id)
    lang = testSelectSomthingColumn(738070596, "language")

    gameids:list[str] = ["asjkldjklas", "12jkl3ejkl123jkl", f"{game_id}"]
    user_ids:list[str] = ["akl;sdakl;d", "12jkl312ijk31", f"{user_id}"]
    removecomm:list[str] = ["amskldkl;masdkl;", "!@#!@!@#!", "remove from game"]
    alloflist:list[list[str]] = [first_message, directions, gameids, user_ids, removecomm]

    i:int = 0
    while i < len(alloflist):
        actDirectionOfActionActivities(alloflist[i], lang, i)
        i += 1

def ChatGame():
    ChangeDir(738070596)
    first_message:list[str] = ["qweqw dqw","12311231", "asdasae"]
    directions:list[str] = ["1231313", "adadewq", "create game"]
    chat_ids:list[int] = []
    i:int = 0
    while i < 3:
        chat_id = tools.CreateChat()
        chat_ids.append(chat_id)
        i += 1

    ShowChats(first_message, directions)

    i = 0
    while i < 3:
        tools.DeleteChat(chat_ids[i])
        i += 1

def ActiveGame():
    first_message:list[str] = ["qweqw dqw","12311231", "asdasae"]
    directions:list[str] = ["1231313", "adadewq", "active games"]

    NothingThereToShowGames(first_message, directions)
    ShowGames(first_message, directions)

def Statistic():
    i:int = 0
    monitor:bool = False
    rand = random.randint(2, 10)
    while i < rand:
        user_id = tools.CreateUser()
        game_id = tools.HeadOfCreateFutureGames()
        tools.RegistrationUserToGames(user_id, game_id)
        if monitor:
            monitor = False
        else:
            tools.Paid(user_id, game_id)
            monitor = True
        i += 1

    ChangeDir(738070596)
    first_message:list[str] = ["askasdad", "1312312", "/start"]
    direction:list[str] = ["ajklsdjklasd", "!!@#!!@#!", "see stat"]
    lang = testSelectSomthingColumn(738070596, "language")
    moneyDirectionOfActionActivities(first_message, lang, 0)
    moneyDirectionOfActionActivities(direction, lang, 1)

    tools.DeleteAllWaitGames()
    tools.DeleteAllUsers()

def CheckAdditionalButtonsChatsAndGames():
    ChangeDir(738070596)
    ResetAllLaunchPoints(738070596)
    chat_ids:list[int] = []
    game_ids:list[int] = []
    i:int = 0
    while i < 16:
        game_id = tools.HeadOfCreateFutureGames()
        chat_id = tools.CreateChat()
        chat_ids.append(chat_id)
        game_ids.append(game_id)
        i += 1

    first_message:list[str] = ["qweqw dqw","12311231", "asdasae"]
    directions:list[str] = ["1231313", "adadewq", "create game"]
    example:list[str] = ["AJKLDSKL", "!@#!$AWEQW%!#", f"{chat_ids[random.randint(0, 15)]}"]
    next:list[str] = ["ajklsdjklasjkld", "!#@#!!@#", "next page"]
    previous:list[str] = ["ASNDJKAJKS", "!#!@#!@%SDASD", "previous page"]
    buttons:list[list[str]] = [next, previous]
    lang = testSelectSomthingColumn(738070596, "language")

    actDirectionOfActionActivities(first_message, lang, 0)
    actDirectionOfActionActivities(directions, lang, 1)
    i = 0
    while i < 2:
        actDirectionOfActionActivities(buttons[i], lang, 2)
        i += 1

    actDirectionOfActionActivities(example, lang, 2)

    i = 0
    while i < 2:
        actDirectionOfActionActivities(buttons[i], lang, 3)
        i += 1

    i = 0
    while i < 16:
        tools.DeleteGameInSchedule(game_ids[i])
        tools.DeleteChat(chat_ids[i])
        i += 1
    
    
def CheckAdditionalButtonsGamesInActivities():
    ChangeDir(738070596)
    ResetAllLaunchPoints(738070596)
    game_ids:list[int] = []
    user_ids:list[int] = []
    i:int = 0
    while i < 16:
        game_id = tools.HeadOfCreateFutureGames()
        user_id = tools.CreateUser()
        tools.RegistrationUserToGames(user_id, game_id)
        game_ids.append(game_id)
        user_ids.append(user_id)
        i += 1
    
    first_message:list[str] = ["qweqw dqw","12311231", "asdasae"]
    directions:list[str] = ["1231313", "adadewq", "active games"]
    next:list[str] = ["ajklsdjklasjkld", "!#@#!!@#", "next page"]
    previous:list[str] = ["ASNDJKAJKS", "!#!@#!@%SDASD", "previous page"]
    buttons:list[list[str]] = [next, previous]
    lang = testSelectSomthingColumn(738070596, "language")

    actDirectionOfActionActivities(first_message, lang, 0)
    actDirectionOfActionActivities(directions, lang, 1)
    i = 0
    while i < 2:
        actDirectionOfActionActivities(buttons[i], lang, 2)
        i += 1
    
    i = 0
    while i < 16:
        tools.DeleteWaitGame(game_ids[i], user_ids[i])
        tools.DeleteGameInSchedule(game_ids[i])
        tools.DeleteUsers(user_ids[i])
        i += 1

def PaidAction():
    ChangeDir(738070596)
    alloflist:list[list[str]] = []
    first_message:list[str] = ["askasdad", "1312312", "/start"]
    direction:list[str] = ["ajklsdjklasd", "!!@#!!@#!", "paid action"]
    paidcomm:list[str] = ["ASDJKLAJKLS", "@#IO$U@#$I@", "paided"]
    lang = testSelectSomthingColumn(738070596, "language")
    i:int = 0
    while i < 2:
        user_id = tools.CreateUser()
        game_id = tools.HeadOfCreateFutureGames()
        tools.RegistrationUserToGames(user_id, game_id)
        user_ids:list[str] = ["ASJKLDIASJKL", "!@#!@$!#$$%!#$", f"{user_id}"]
        game_ids:list[str] = ["ASDJKLASKDJL", "!@#L!@#J!", f"{game_id}"]
        alloflist = [first_message, direction, user_ids, paidcomm]
        j:int = 0
        if i == 1:
            alloflist.append(game_ids)
            while j < 3:
                game_id = tools.HeadOfCreateFutureGames()
                tools.RegistrationUserToGames(user_id, game_id)
                j += 1
        counter:int = 0          
        while counter < len(alloflist):
            moneyDirectionOfActionActivities(alloflist[counter], lang, counter)
            counter += 1
        tools.DeleteAllWaitGames()
        tools.DeleleAllGamesInSchedule()
        tools.DeleteAllUsers()
        i += 1

def CheckAdditionalButtonsClientsAndGames():
    ChangeDir(738070596)
    ResetAllLaunchPoints(738070596)
    game_ids:list[int] = []
    user_ids:list[int] = []
    example_userid:int = -1
    i:int = 0
    while i < 16:
        game_id = tools.HeadOfCreateFutureGames()
        user_id = tools.CreateUser()
        tools.RegistrationUserToGames(user_id, game_id)
        game_ids.append(game_id)
        user_ids.append(user_id)
        i += 1
    i = 0
    example_userid = user_ids[random.randint(0, 15)]
    while i < len(game_ids):
        tools.RegistrationUserToGames(example_userid, game_ids[i])
        i += 1

    first_message:list[str] = ["qweqw dqw","12311231", "asdasae"]
    directions:list[str] = ["1231313", "adadewq", "paid action"]
    example:list[str] = ["AJKLDSKL", "!@#!$AWEQW%!#", f"{example_userid}"]
    example2:list[str] = ["ASDKL:ASL:", "!@#L:!KL:@", "paided"]
    next:list[str] = ["ajklsdjklasjkld", "!#@#!!@#", "next page"]
    previous:list[str] = ["ASNDJKAJKS", "!#!@#!@%SDASD", "previous page"]
    buttons:list[list[str]] = [next, previous]
    lang = testSelectSomthingColumn(738070596, "language")

    moneyDirectionOfActionActivities(first_message, lang, 0)
    moneyDirectionOfActionActivities(directions, lang, 1)

    i = 0
    while i < 2:
        moneyDirectionOfActionActivities(buttons[i], lang, 2)
        i += 1
    moneyDirectionOfActionActivities(example, lang, 2)
    moneyDirectionOfActionActivities(example2, lang, 3)
    i = 0
    while i < 2:
        moneyDirectionOfActionActivities(buttons[i], lang, 4)
        i += 1

    i = 0
    while i < len(game_ids):
        tools.DeleteWaitGame(game_ids[i], example_userid)
        i += 1

    i = 0
    while i < 16:
        tools.DeleteWaitGame(game_ids[i], user_ids[i])
        tools.DeleteGameInSchedule(game_ids[i])
        tools.DeleteUsers(user_ids[i])
        i += 1

def ChangeLanguage():
    first_message:list[str] = ["askasdad", "1312312", "/start"]
    directions: list[str] = ["alsdklasda", "!#JK#!@J#", "change language"]
    languagesbutton:list[str] = ["ASJKLDAOSKLD", "@#!@#W!#W"]
    languages:list[str] = ["en", "tur", "ru"]
    alloflist:list[list[str]] = []
    j:int = 0
    i:int = 0

    while i < len(languages):
        languagesbutton.append(languages[i])
        alloflist = [first_message, directions, languagesbutton]
        j = 0
        ChangeDir(738070596)
        lang = testSelectSomthingColumn(738070596, "language")
        while j < len(alloflist):
            DirectionOfActionSettings(alloflist[j], lang, j)
            j += 1
        languagesbutton.pop()
        i += 1


def Welcome():

    first_message:list[str] = ["askasdad", "1312312", "/start"]
    reg:list[str] = ["asdasdww", "13123aa", "start reg"]
    password:list[str] = ["jkasjkdjk", "1231231", "111"]
    main_menu:list[str] = ["asdadfaeqw", "31231", "Main_Menu"]


    tools.ResetAdmin(738070596)
    lang = testSelectSomthingColumn(738070596, "language")
    FirstMessage(first_message, lang)
    EnterPassword(reg, lang)
    ShowRules(password, lang)
    ShowMenu(main_menu, lang)

def Games():
    tools.ChangeAdmin(738070596, 'action', 'game', 'str')

    game_id = CreateGame()
    tools.DeleteGameInSchedule(game_id)

    game_id = tools.HeadOfCreateFutureGames()
    ChangeGame(game_id)
    tools.DeleteGameInSchedule(game_id)

    game_id = tools.HeadOfCreateFutureGames()
    RemoveGame(game_id)
    tools.DeleteGameInSchedule(game_id)

    CheckAdditionalButtonsGames()


def Clients():
    tools.ChangeAdmin(738070596, 'action', 'clients', 'str')

    CreateClient()
    ChangeClient()
    DeleteClient()
    RegToGame()
    CheckAdditionalButtonsClientsWithGames()
    CheckAdditionalButtonsClients()

def Activities():
    tools.ChangeAdmin(738070596, 'action', 'activities', 'str')

    ChatGame()
    ActiveGame()
    CheckAdditionalButtonsChatsAndGames()
    CheckAdditionalButtonsGamesInActivities()

def Money():
    tools.ChangeAdmin(738070596, 'action', 'money', 'str')

    Statistic()
    PaidAction()
    CheckAdditionalButtonsClientsAndGames()

def Settings():
    tools.ChangeAdmin(738070596, 'action', 'settings', 'str')

    ChangeLanguage()

def GlobalTest():
    mainConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    Welcome()
    Games()
    Clients()
    Activities()
    Money()
    Settings()