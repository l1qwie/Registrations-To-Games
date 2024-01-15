import used_by_everyone as forall
from User_bot.Notifications.notification_database import HowMuthGamesChanged, HowKnowWhatChanged, HowMuchIsLeft, LeaveANote, DelMyRec, CheckUsersWhoNeedNotif
from User_bot.Notifications.notification_keyboard import AgreeOrDesagree

def WhatHeppend(S: dict[str, str], uid: int) -> tuple[int, str, int, str, object, str]:

    games_id:list[int] = []
    sport:str = ''
    date:int = -1
    time:int = -1
    latitude:float = -1
    longitude:float = -1
    address:str = ''
    prmode:str = ''
    notifgameid:int = -1
    act:str = "we decide what to do"

    games_id = HowMuthGamesChanged(uid)

    if len(games_id) > 0:
        sport, date, time, latitude, longitude, address = HowKnowWhatChanged(games_id[0])
        sport = S[sport]
        date_str = forall.CreateDateStr(date)
        time_str = forall.CreateTimeStr(time)     
        text = S["notif_text"] % (HowMuchIsLeft(uid), sport, date_str, time_str, address, latitude, longitude)
        kbd = AgreeOrDesagree(S["agree"], S["desagree"])
        prmode = 'HTML'
        level = 0
        notifgameid = games_id[0]
    else:
        text = S["no_notifications"]
        kbd = forall.Options(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"])
        level = 3
        act = "divarication"
    return level, act, notifgameid, text, kbd, prmode

def IrreversibleDecision(S: dict[str, str], uid:int, phrase: str, game_id: int) -> tuple[int, str, str, object, bool, str]:

    halt:bool = False
    text:str = ''
    kbd: object = None
    text_str:str = ''
    prmode:str = ''
    level:int = -1
    _notifgameid_: int = -1
    act:str = "we decide what to do"

    if phrase in ("leave a note", "Del my record"):
        halt = True
        if phrase == "leave a note":
            text = S["iyi_akshamlar"]
            LeaveANote(uid, game_id)
        else:
            text = "Мне очень жаль. Но я искрине надеюсь, что вы к нам вернетесь и все таки поиграете в футбол или волейбол...Буду ждать вас!\n\n\n"
            DelMyRec(uid, game_id)
        CheckUsersWhoNeedNotif(game_id)
        level, act, _notifgameid_, text, kbd, prmode = WhatHeppend(S, uid)
        text += text_str
    else:
        level, act, _notifgameid_, text, kbd, prmode = WhatHeppend(S, uid)
    return level, act, text, kbd, halt, prmode