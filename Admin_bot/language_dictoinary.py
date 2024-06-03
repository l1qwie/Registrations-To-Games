ru = {
#FORALL
    "onlysport": "<b>Вид спорта:</b> %s",
    "sport+date": "<b>Вид спорта:</b> %s\n<b>Дата:</b> %s",
    "sport+date+time": "<b>Вид спорта:</b> %s\n<b>Дата:</b> %s\n<b>Время:</b> %s",
    "sport+date+time+seats": "<b>Вид спорта:</b> %s\n<b>Дата:</b> %s\n<b>Время:</b> %s\n<b>Всего свободных мест:</b> %d",
    "sport+date+time+seats+price+currency": "<b>Вид спорта:</b> %s\n<b>Дата:</b> %s\n<b>Время:</b> %s\n<b>Всего свободных мест:</b> %d\n<b>Цена на одно место:</b> %d %s",
    "sport+date+time+seats+price+currency+link": "<b>Вид спорта:</b> %s\n<b>Дата:</b> %s\n<b>Время:</b> %s\n<b>Всего свободных мест:</b> %d\n<b>Цена на одно место:</b> %d %s\n<b>Ссылка на место проведения:</b> https://www.google.com/maps?q=%s,%s",
    "sport+date+time+seats+price+currency+link+nameaddress": "<b>Вид спорта:</b> %s\n<b>Дата:</b> %s\n<b>Время:</b> %s\n<b>Всего свободных мест:</b> %d\n<b>Цена на одно место:</b> %d %s\n<b>Ссылка на место проведения:</b> https://www.google.com/maps?q=%s,%s\n<b>Название адреса:</b> %s\n",
#Welcome act
    #Messages
    "first_message": "Добро пожаловать в нашего бота! Этот бот может пригодиться вам, если вы приобрели его первую часть и вам требуется административная часть. Если это ваш случай, то нажмите на кнопку снизу",
    "enter_password": "Введите пароль (На данный момент пароль: 111)",
    "global_rules": "Вот пара рекомендаций для того, как пользоваться этим ботом:\n\n1. <b>Игры</b>\n          Тут вы сможете сделать все что угодно с вашими играми (создание, настройка, удаление и тд.)\n2. <b>Клиенты</b>\n          Тут вы сможете сделать все со своими клиентами (создать, поменять, удалить)\n3. <b>Активность</b>\n          Тут вы сможете сделать своеобразную игру для чата ваших клиентов (суть игры в том, что ваши клиенты должны будут наперегонки регистрироваться на игру). А так же тут вы сможете посмотреть куда и кто записался, а так же найти контакты нужного вам человека\n4. <b>Деньги</b>\n        Здесь вы сможете посмотреть кто вам должен за игры, от кого ожидается оплата, а кто уже оплатил. Так же именно тут вы сможете увидеть небольшую статистику по всей финансовым оборотам в бот\n5. <b>Настройки</b>\n          Тут вы сможете изменить настрйоки бота. Например язык",
    "wrong_pass": "Пароль не верный! Попробуйте еще... (тестовый пароль: 111)",
    #Keyboard
    "hello": "Зарегестрироваться",
#Game act
    #Preface
        #Message
        "games_directions": "Выберите направление связаное с играми",
        #Keyboard
        "change_games": "Изменить игру",
        "create_games": "Создать игру",
        "delete_games": "Удалить игру",
    #Create
        #Message 
        "start_create_game": "Выберите вид спорта",
        "writedate": "\n\n\nВведите дату проведения игры в формате ДДММГГГГ используя любой разделитель",
        "whitetime": "\n\n\nВведите время проведения игры в формате ЧЧММ используя любой разделитель",
        "writeseats": "\n\n\nВведите количество свободных мест на эту игру",
        "writeprice": "\n\n\nВведите цену за одно место в формате цифры на эту игру",
        "writecurrency": "\n\n\nВведите имя валюты. Я не никак не контралирую то название, которое вы введете, так что советую вводить так, чтобы все понимали. Пример: USD EURO TL и тд",
        "writelink": "\n\n\nПршлите ссылку с Google Maps с тем местом, где будет проходить игра. Очень важно, чтоб в ссылке были координаты. Если у вас не будет получатся коректная ссылка, то могу предложить скопировать пример ссылки и вписать на место пропусков координаты вручную. https://www.google.com/maps?q=(<i>Тут место для широты</i>),(<i>Тут место для долготы</i>)",
        "writeaddress": "\n\n\nВведите название адреса",
        "clarification": "Вы закончили заполнять информацию для создания новой игры. Сохраните эту игру, если все данные верны\n\n",
        "gamewassave": "Игра сохранена и теперь доступна вашим клиентам для регистрации\n\n",
        #Keyboard
        "savegame": "Сохранить",
        "changegame": "Изменить",
    #Change Or Delete
        #Message
        "choose_game": "Выберите игру", 
        "game_inf": "<b>Вид спорта:</b> %s\n<b>Дата:</b> %s\n<b>Время:</b> %s\n<b>Всего свободных мест:</b> %d\n<b>Цена на одно место:</b> %d %s\n<b>Ссылка на место проведения:</b> https://www.google.com/maps?q=%s,%s\n<b>Название адреса:</b> %s",
        "choose_change": "\n\nВыберите что хотите изменить",
        "data_changed": "Данные изменены. Желаете изменить что то еще?",
        "game_removed": "Игра удалена. Желаете сделать что-то еще?",
        #Keyboard
        "sport": "Спорт",
        "date": "Дата",
        "time": "Время",
        "seats": "Места",
        "price": "Цена (цифра)",
        "currency": "Валюта",
        "link": "Ссылка",
        "nameaddress": "Название адреса",
#Clients act
    #Preface
        #Message
        "choose_cl_dir": "Выберите направление связаное с клиентами",
        "chose_your_client": "Выберите клиента",
        "no_clients": "У Вас нет ни одного клиента! Рекомендую что-то сделать с этим :)",
        #Keyboard
        "create_client": "Создать клиента",
        "change_client": "Изменить данные клиента",
        "delete_client": "Удалить клиента",
        "reg_client": "Зарегистрировать клиента на игру",
    #Create
        #Message
        "choose_fromwhere": "Выберите мессенджер вашего клиента",
        "fromwhere": "<b>Способ связи:</b> %s\n",
        "fromwhere+name": "<b>Способ связи:</b> %s\n<b>Имя:</b> %s",
        "fromwhere+name+last_name": "<b>Способ связи:</b> %s\n<b>Имя:</b> %s\n<b>Фамилия:</b> %s",
        "fromwhere+name+last_name+phonenum": "<b>Способ связи:</b> %s\n<b>Имя:</b> %s\n<b>Фамилия:</b> %s\n<b>Номер телефона:</b> %s",
        "writename": "\n\n\nНапишите имя вашего клиента",
        "writelastname": "\n\n\nНапишите фамилию вашего клиента",
        "writephonenum": "\n\n\nНапишите номер телефна вашего клиента. Только цифры и без какиз либо промежуточных символов",
        "saveorchange": "\n\n\nВы закончили заполнять информацию про своего клиента. Желаете ее сохранить или что то изменить?",
        "data_save": "\n\n\nНовый клиент создан",
        #Keybaord
        "teledirectionary": "Из телефонной книжки",
    #Change
        #Message
        "user_inf": "<b>Имя:</b> %s\n<b>Фамилия:</b> %s\n<b>Номер телефона:</b> %s\n<b>Способ связи через:</b> %s\n<b>Язык:</b> %s",
        "choose_dir_for_change": "Выберите что хотите изменить",
        "inf_saved": "Информация сохранена\n",
        #Keyboard
        "fromwhere_kb": "Способ связи",
        "name_kb": "Имя",
        "last_name_kb": "Фамилия",
        "phonenum_kb": "Телефон",
    #Delete
        #Message
        "client_delete": "Ваш клиент удален!",
    #RegToGame
        #Message
        "type_seats": "Введите количество свободных мест, которые планирует занять ваш клиент",
        "choose_paymethod": "Выберите способ оплаты для вашего клиента",
        "client_reged": "Клиент был зарегестрирован на эту игру. Сообщите ему что конечная стоимость его посещения будет сосавлять %s %s\n",
        #Keyboard
        "online": "Картой (онлайн)",
        "cash": "Наличкой",
#Activities
    #Preface
        #Message
        "Choose_dir_of_activities": "Выберите направление связанное с активностями",
        "rules_for_chat_game": "\n\n\nP.S. Чтобы начать игру в чате вам сначало нужно добавить меня в чат, сделать администратором и намисать в чат команду /add. И только после этого я помогу вам сделать игру в чате",
        #Keyboard
        "reg_game": "Создать игру в чате",
        "activ_game": "Активные игры",
    #Chat Game
        #Message
        "no_chats": "Бот не добавлен ни в один чат!\n",
        "no_games": "Сначала создайте игру!\n",
        "game_rules": """Я предлагаю вам сделать игру в вашем чате или группе. Суть игры следующая: вы выбираете чат, выбираете игру, и я присылаю сообщение с кнопкой "Участвовать!". Ваши клиенты смогут нажимать на эту кнопку и автоматически записываться. Главное в этой игре - успеть нажать на эту самую заветную кнопочку\n\n""",
        "foundchats": "Вот чаты которые я нашел:",
        "no_new_chats": "Я не нашел ни одного чата! Пожалуйста добавьте меня в какой нибудь чат, дайте права администратора и тогда повторите эту процедуру",
        "choose_game_for_chatgame": "Выберите игру на которую будут записываться ваши клиенты из чата",
        "choose_language": "Выберите язык сообщения которое будет отправелно в чат",
        "example_of_chat_game": "Вот пример того сообщения, которое будет в группе/чате:\n\n\n",
        "start_chatgame": """Всем привет!\nМы начинаем игру "Кто успел тот и съел"! Ниже небольшая информация по игре на которую открыта регистрация, а так же список уже записавшихся! Скорее жми на кнопку "Учавствовать", если не хочешь пролететь!\n\n\n""",
        "seats_counter": "%d. %s\n",
        "theseatsisfree": "Место свободно!",
        "chatgame_sended": "Сообщение отправлено! Игра началась!\n",
        #Keyboard
        "show_chats": "Показать уже обнаруженные чаты",
        "new_chat": "Обнаружить новые чаты",
        "send": "Отправить",
        "participate": "Участвовать!",
    #Active Game
        #Message
        "active_games": "Выберите активую игру, чтобы увидеть более детальную информацию о клиентах, котоые ее ждут",
        "waiting_cl": "Ожидают игру:",
        "no_active_games": "Пока что у вас не ожидают ни одну игру!\n",
        "all_of_client_on_game": "Вот все ваши кленты, которые ожидают эту игру. Выберите любого для просмотра информации по клиенту, для связи с ним или для удаления клиента с этой игры",
        "disclaimer": """\n\nP.S. Если клиент был зарегестрирован в боте, то в низу будет кнопочка "Связаться". Нажав на нее вы перейдете в диалог с этим человеком""",
        "client_removed": "Запись клиента наа эту игру была удалена!\n",
        #Keyboard
        "removeforgame": "Удалить с игры",
        "call": "Связаться",
#Finances
    #Preface
        #Message
        "choose_money_dir": "Выберите направление связанное с финансами",
        #Keyboard
        "money_stat": "Статистика финансов",
        "money_paid_act": "Посмотреть должников",
    #See statistic
        #Message
        "see_stat1": "Вся статистика финансов все время пользования ботом:\n1. <b>Вы заработали за все время:</b> ",
        "see_stat2": "2. <b>Вам должны:</b>",
        "no_stat": "Статистика отсутсвует!\n",
        "money_have": "%s %s",
    #Paid Action
        #Message
        "choose_your_debtor": "Вот все кто вам должен. Выберите любого",
        "no_debtors": "У вас еще нет ни одного должника!\n",
        "cl_game_inf": "Игра на которую зарегестрирован клиент:\n1. <b>Спорт:</b> %s\n2. <b>Дата:</b> %s\n3. <b>Время:</b> %s\n4. <b>Должен заплатить:</b> %s %s\n5. <b>Занимаемые места:</b> %s\n6. <b>Способ оплаты:</b> %s\n\n",
        "client_paided": "Данные обновлены! Клент оплатил!\n",
        #Keyboard
        "paided": "Оплачено",
#Settings
    #Preface
        #Message
        "choose_dir_set": "Выберите направления в настройках бота (пока что только одно)",
        #Keyboard
        "change_lang": "Изменить язык бота",
    #Change Language
        #Message
        "choose_your_language": "Выберите на какой язык переключиться",
        "language_changed": "Язык переключен\n",
        #Keyboard
        "ru": "Русский",
        "en": "Английский",
        "tur": "Турецкий", 


#For All
    #Messages
    #Keyboard
    "first_option": "Игры",
    "second_option": "Клиенты",
    "third_option": "Активность",
    "fourth_option": "Деньги",
    "fifth_option": "Настройки",
    "yes": "Да",
    "no": "Нет",
    

}

en = {
#FORALL
    "onlysport": "<b>Sport type:</b> %s",
    "sport+date": "<b>Sport type:</b> %s\n<b>Date:</b> %s",
    "sport+date+time": "<b>Sport type:</b> %s\n<b>Date:</b> %s\n<b>Time:</b> %s",
    "sport+date+time+seats": "<b>Sport type:</b> %s\n<b>Date:</b> %s\n<b>Time:</b> %s\n<b>Total available seats:</b> %d",
    "sport+date+time+seats+price+currency": "<b>Sport type:</b> %s\n<b>Date:</b> %s\n<b>Time:</b> %s\n<b>Total available seats:</b> %d\n<b>Price for one seat:</b> %d %s",
    "sport+date+time+seats+price+currency+link": "<b>Sport type:</b> %s\n<b>Date:</b> %s\n<b>Time:</b> %s\n<b>Total available seats:</b> %d\n<b>Price for one seat:</b> %d %s\n<b>Location link:</b> https://www.google.com/maps?q=%s,%s",
    "sport+date+time+seats+price+currency+link+nameaddress": "<b>Sport type:</b> %s\n<b>Date:</b> %s\n<b>Time:</b> %s\n<b>Total available seats:</b> %d\n<b>Price for one seat:</b> %d %s\n<b>Location link:</b> https://www.google.com/maps?q=%s,%s\n<b>Address name:</b> %s\n",

#Welcome act
    #Messages
    "first_message": "Welcome to our bot! This bot can be useful if you have purchased its first part and need the administrative section. If this is your case, then click the button below",
    "enter_password": "Enter the password (Current password: 111)",
    "global_rules": "Here are a couple of recommendations on how to use this bot:\n\n1. <b>Games</b>\n          Here, you can do anything with your games (create, configure, delete, etc.)\n2. <b>Clients</b>\n          Here, you can manage everything related to your clients (create, modify, delete)\n 3. <b>Activity</b>\n          Here you can create a unique game for your clients in the chat (the essence of the game is that your clients will have to register for the game as quickly as possible). Also, here you can see where and who has registered, as well as find the contacts of the person you need\n4. <b>Finances</b>\n          Here you can see who owes you for the games, who payment is expected from, and who has already paid. Also, right here you can view a small statistics on all financial transactions in the bot\n5. <b>Settings</b>\n          Here, you can change the bot settings. For example, the language",
    "wrong_pass": "Invalid password! Try again... (test password: 111)",
    #Keyboard
    "hello": "Register", 
#Game act
    #Preface
        #Message
        "games_directions": "Choose the option related to games",
        
        #Keyboard
        "change_games": "Modify game",
        "create_games": "Create game",
        "delete_games": "Delete game",
    #Create
        #Message 
        "start_create_game": "Choose a sport",
        "writedate": "\n\n\nEnter the game date in the format DDMMYYYY using any separator",
        "whitetime": "\n\n\nEnter the game time in the format HHMM using any separator",
        "writeseats": "\n\n\nEnter the number of available seats for this game",
        "writeprice": "\n\n\nEnter the price for one seat in numeric format for this game",
        "writecurrency": "\n\n\nEnter the currency name. I have no control over the name you enter, so I advise entering it in a way that everyone understands. Example: USD, EURO, TL, etc",
        "writelink": "\n\n\nSend a link from Google Maps with the location of the game. It is very important that the link contains coordinates. If you cannot generate a correct link, I can suggest copying the example link and manually entering the coordinates in the placeholders. https://www.google.com/maps?q=(<i>Here goes latitude</i>),(<i>Here goes longitude</i>)",
        "writeaddress": "\n\n\nEnter the name of the address",
        "clarification": "You have finished filling out the information for creating a new game. Save this game if all the data is correct\n\n<b>Sport type:</b> %s\n",
        "gamewassave": "The game has been saved and is now available for registration by your clients\n\n",
        #Keyboard
        "savegame": "Save",
        "changegame": "Modify",
    #Change Or Delete
        #Message
        "choose_game": "Choose a game",
        "game_inf": "<b>Sport:</b> %s\n<b>Date:</b> %s\n<b>Time:</b> %s\n<b>Total available seats:</b> %d\n<b>Price for one seat:</b> %d %s\n<b>Location link:</b> https://www.google.com/maps?q=%s,%s\n<b>Address name:</b> %s",
        "choose_change": "\n\nChoose what you want to modify",
        "data_changed": "The data has been modified. Do you want to change anything else?",
        "game_removed": "The game has been deleted. Do you want to do anything else?",
        #Keyboard
        "sport": "Sport",
        "date": "Date",
        "time": "Time",
        "seats": "Seats",
        "price": "Price (number)", 
        "currency": "Currency", 
        "link": "Link",
        "nameaddress": "Address Name",
#Clients act
    #Preface
        #Message
        "choose_cl_dir": "Choose the option related to clients",
        "chose_your_client": "Choose a client",
        "no_clients": "You don't have any clients yet! I recommend doing something about it :)",
        #Keyboard
        "create_client": "Create a client",
        "change_client": "Modify client data",
        "delete_client": "Delete a client",
        "reg_client": "Register the client for the game",
    #Create
        #Message
        "choose_fromwhere": "Choose your client's messenger",
        "fromwhere": "<b>Method of communication:</b> %s\n",
        "fromwhere+name": "<b>Method of communication:</b> %s\n<b>Name:</b> %s\n",
        "fromwhere+name+last_name": "<b>Method of communication:</b> %s\n<b>Name:</b> %s\n<b>Surname:</b> %s\n",
        "fromwhere+name+last_name+phonenum": "<b>Method of communication:</b> %s\n<b>Name:</b> %s\n<b>Surname:</b> %s\n<b>Phone Number:</b> %s\n",
        "writename": "Write your client's name",
        "writelastname": "Write your client's last name",
        "writephonenum": "Write your client's phone number. Only digits and no intermediate symbols",
        "saveorchange": "You have finished filling out information about your client. Do you want to save it or make any changes?",
        "data_save": "A new client has been created",
        #Keybaord
        "teledirectionary": "From the phone book",
    #Change
        #Message
        "user_inf": "<b>Name:</b> %s\n<b>Last Name:</b> %s\n<b>Phone Number:</b> %s\n<b>Communication Method:</b> %s\n<b>Language</b> %s\n",
        "choose_dir_for_change": "Choose what you want to modify",
        "inf_saved": "The information has been saved\n",
        #Keyboard
        "fromwhere_kb": "Communication Method",
        "name_kb": "Name",
        "last_name_kb": "Last Name",
        "phonenum_kb": "Phone Number",
    #Delete
        #Message
        "client_delete": "Your client has been deleted!",
    #RegToGame
        #Message
        "type_seats": "Enter the number of available spots your client plans to occupy",
        "choose_paymethod": "Choose a payment method for your client",
        "client_reged": "The client has been registered for this game. Inform them that the final cost of their visit will be %s %s\n",
        #Keyboard
        "online": "Card (online)",
        "cash": "Cash",
#Activities
    #Preface
        #Message
        "Choose_dir_of_activities": "Choose a direction related to activities",
        "rules_for_chat_game": "\n\n\nP.S. To start a game in the chat, you first need to add me to the chat, make me an administrator, and then type the command /add in the chat. Only after that, I will help you create a game in the chat",
        #Keyboard
        "reg_game": "Create a chat game",
        "activ_game": "Active games",
    #Chat Game
        #Message
        "no_chats": "The bot has not been added to any chat!\n",
        "no_games": "First, create a game!\n",
        "game_rules": """I suggest creating a game in your chat or group. The essence of the game is as follows: you choose the chat, select the game, and I send a message with the button 'Участвовать!' (Participate!). Your clients can click on this button and automatically register. The main thing in this game is to manage to press this coveted button in time\n\n""",
        "foundchats": "Here are the chats I found:",
        "no_new_chats": "I couldn't find any chats! Please add me to a chat, grant administrator rights, and then repeat this procedure",
        "choose_game_for_chatgame": "Choose a game for your clients to register from the chat",
        "choose_language": "Choose the language for the message to be sent in the chat",
        "example_of_chat_game": "Here is an example of the message that will be in the group/chat:\n\n\n",
        "start_chatgame": """Hello everyone!\nWe are starting the game "Whoever is quick, eats!" Below is some information about the game with open registration, as well as a list of those who have already signed up! Hurry up and click the "Participate" button if you don't want to miss out!\n\n\n""",
        "seats_counter": "%d. %s\n",
        "theseatsisfree": "A spot is available!",
        "chatgame_sended": "Message sent! The game has started!\n",
        #Keyboard
        "show_chats": "Show already detected chats",
        "new_chat": "Detect new chats",
        "send": "Send",
        "participate": "Participate!",
    #Active Game
        #Message
        "active_games": "Choose an active game to see more detailed information about the clients waiting for it",
        "waiting_cl": "Waiting for the game:",
        "no_active_games": "At the moment, no games are being awaited!\n",
        "all_of_client_on_game": "Here are all your clients who are waiting for this game. Choose any of them to view client information, contact them, or remove the client from this game",
        "disclaimer": """\n\nP.S. If the client is registered with the bot, there will be a "Contact" button at the bottom. By clicking on it, you will enter a dialogue with this person""",
        "client_removed": "The client's registration for this game has been removed!\n",
        #Keyboard
        "removeforgame": "Remove from the game",
        "call": "Contact",
#Finances
    #Preface
        #Message
        "choose_money_dir": "Choose a finance-related direction",

        #Keyboard
        "money_stat": "Financial statistics",
        "money_paid_act": "View debtors",
    #See statistic
        #Message
        "see_stat1": "All-time financial statistics:\n1. <b>You have earned:</b>",
        "see_stat2": "2. <b>You are owed:</b>",
        "no_stat": "No statistics available!\n",
        "money_have": "%s %s",
    #Paid Action
        #Message
        "choose_your_debtor": "Here are those who owe you. Choose anyone",
        "no_debtors": "You don't have any debtors yet!\n",
        "cl_game_inf": "The game the client is registered for:\n1. <b>Sport:</b> %s\n2. <b>Date:</b> %s\n3. <b>Time:</b> %s\n4. <b>Amount Due:</b> %s %s\n5. <b>Occupied Spots:</b> %s\n6. <b>Payment Method:</b> %s\n\n",
        "client_paided": "Data updated! The client has paid!\n",
        #Keyboard
        "paided": "Paid",
#Settings
    #Preface
        #Message
        "choose_dir_set": "Choose directions in the bot settings (currently only one available)",
        #Keyboard
        "change_lang": "Change the bot language",
    #Change Language
        #Message
        "choose_your_language": "Choose the language to switch to",
        "language_changed": "Language switched\n",
        #Keyboard
        "ru": "Russian",
        "en": "English",
        "tur": "Turkish", 





#For All
    #Messages
    #Keyboard
    "first_option": "Games",
    "second_option": "Clients",
    "third_option": "Activity",
    "fourth_option": "Finances",
    "fifth_option": "Settings",
    "yes": "Yes",
    "no": "No",
 
}

tur = {
#FORALL
    "onlysport": "<b>Spor türü:</b> %s",
    "sport+date": "<b>Spor türü:</b> %s\n<b>Tarih:</b> %s",
    "sport+date+time": "<b>Spor türü:</b> %s\n<b>Tarih:</b> %s\n<b>Saat:</b> %s",
    "sport+date+time+seats": "<b>Spor türü:</b> %s\n<b>Tarih:</b> %s\n<b>Saat:</b> %s\n<b>Toplam boş koltuk sayısı:</b> %d",
    "sport+date+time+seats+price+currency": "<b>Spor türü:</b> %s\n<b>Tarih:</b> %s\n<b>Saat:</b> %s\n<b>Toplam boş koltuk sayısı:</b> %d\n<b>Bir koltuk için fiyat:</b> %d %s",
    "sport+date+time+seats+price+currency+link": "<b>Spor türü:</b> %s\n<b>Tarih:</b> %s\n<b>Saat:</b> %s\n<b>Toplam boş koltuk sayısı:</b> %d\n<b>Bir koltuk için fiyat:</b> %d %s\n<b>Yer bağlantısı:</b> https://www.google.com/maps?q=%s,%s",
    "sport+date+time+seats+price+currency+link+nameaddress": "<b>Spor türü:</b> %s\n<b>Tarih:</b> %s\n<b>Saat:</b> %s\n<b>Toplam boş koltuk sayısı:</b> %d\n<b>Bir koltuk için fiyat:</b> %d %s\n<b>Yer bağlantısı:</b> https://www.google.com/maps?q=%s,%s\n<b>Adres adı:</b> %s\n",
#Welcome act
    #Messages
    "first_message": "Hoş geldiniz! Botumuza hoş geldiniz! Bu bot, eğer ilk bölümünü satın aldıysanız ve yönetim bölümüne ihtiyacınız varsa, size yardımcı olabilir. Eğer durumunuz bu ise, o zaman aşağıdaki düğmeye tıklayın",
    "enter_password": "Şifreyi girin (Şu anki şifre: 111)",
    "global_rules":"İşte bu botu nasıl kullanacağınıza dair birkaç öneri:\n\n1. <b>Oyunlar</b>\n          Burada oyunlarınızla ilgili her şeyi yapabilirsiniz (oluşturmak, yapılandırmak, silmek vb.)\n2. <b>Müşteriler</b>\n         Burada müşterilerinizle ilgili her şeyi yönetebilirsiniz (oluşturmak, değiştirmek, silmek)\n3. <b>Aktivite</b>\n         Burada müşterileriniz için sohbet içinde özgün bir oyun oluşturabilirsiniz (oyunun özü, müşterilerinizin oyuna mümkün olan en kısa sürede kaydolmaları gerektiğidir). Ayrıca, burada kimin ve nereye kaydolduğunu görebilir, aynı zamanda ihtiyacınız olan kişinin iletişim bilgilerini bulabilirsiniz\n4. <b>Finans</b>\n         Burada size oyunlar için kim borçlu, kimden ödeme bekleniyor ve kim ödeme yaptı, görebilirsiniz. Ayrıca, tam burada, bot içindeki tüm finansal işlemlere ait küçük bir istatistiği görebilirsiniz\n5. <b>Ayarlar</b>\n          Burada botun ayarlarını değiştirebilirsiniz. Örneğin, dil.",
    "wrong_pass": "Hatalı şifre! Tekrar deneyin... (test şifresi: 111)",
    #Keyboard
    "hello": "Kayıt Ol",
#Game act
    #Preface
        #Message
        "games_directions": "Oyunlarla ilgili bir seçenek seçin",
        #Keyboard
        "change_games": "Oyunu değiştir",
        "create_games": "Oyun oluştur", 
        "delete_games": "Oyunu sil",
    #Create
        #Message 
        "start_create_game": "Bir spor seçin",
        "writedate": "\n\n\nHerhangi bir ayırıcı kullanarak oyun tarihini DDMMYYYY formatında girin",
        "whitetime": "\n\n\nHerhangi bir ayırıcı kullanarak oyun saati HHMM formatında girin",
        "writeseats": "\n\n\nBu oyun için mevcut koltuk sayısını girin",
        "writeprice": "\n\n\nBu oyun için bir koltuk için fiyatı sayısal formatta girin",
        "writecurrency": "\n\n\nPara birimi adını girin. Girdiğiniz isim üzerinde kontrolüm yok, bu yüzden herkesin anlayabileceği bir şekilde girmenizi öneririm. Örnek: USD, EURO, TL, vb",
        "writelink": "\n\n\nOyunun gerçekleşeceği yerin Google Haritalar'dan bir bağlantısını gönderin. Bağlantının koordinatlar içermesi çok önemlidir. Eğer doğru bir bağlantı oluşturamazsanız, örnek bağlantıyı kopyalayıp yer tutuculara koordinatları el ile girmeyi önerebilirim. https://www.google.com/maps?q=(<i>Buraya enlem</i>),(<i>Buraya boylam</i>)",
        "writeaddress": "\n\n\nAdresin adını girin",
        "clarification": "Yeni bir oyun oluşturmak için bilgileri doldurmayı tamamladınız. Eğer tüm veriler doğru ise, bu oyunu kaydedin\n\n",
        "gamewassave": "Oyun kaydedildi ve şimdi müşterileriniz tarafından kayıt için kullanılabilir\n\n",
        #Keyboard
        "savegame": "Kaydet",
        "changegame": "Değiştir",
    #Change Or Delete
        #Message
        "choose_game": "Bir oyun seçin",
        "game_inf": "<b>Spor türü:</b> %s\n<b>Tarih:</b> %s\n<b>Saat:</b> %s\n<b>Toplam boş koltuk sayısı:</b> %d\n<b>Bir koltuk için fiyat:</b> %d %s\n<b>Yer bağlantısı:</b> https://www.google.com/maps?q=%s,%s\n<b>Adres adı:</b> %s",
        "choose_change": "\n\nDeğiştirmek istediğiniz şeyi seçin",
        "data_changed": "Veriler değiştirildi. Başka bir şeyi değiştirmek ister misiniz?",
        "game_removed": "Oyun silindi. Başka bir şey yapmak ister misiniz?",
        #Keyboard
        "sport": "Spor",
        "date": "Tarih",
        "time": "Saat",
        "seats": "Koltuklar",
        "price": "Fiyat (sayı)",
        "currency": "Para Birimi",
        "link": "Bağlantı",
        "nameaddress": "Adres Adı",
#Clients act
    #Preface
        #Message
        "choose_cl_dir": "Müşterilerle ilgili bir seçenek seçin",
        "chose_your_client": "Bir müşteri seçin",
        "no_clients": "Henüz hiç müşteriniz yok! Bu konuda bir şeyler yapmanızı öneririm :)",
        #Keyboard
        "create_client": "Bir müşteri oluştur",
        "change_client": "Müşteri verilerini değiştir",
        "delete_client": "Bir müşteriyi sil",
        "reg_client": "Oyuna müşteri kaydet",
    #Create
        #Message
        "choose_fromwhere": "Müşterinizin mesajlaşma uygulamasını seçin",
        "fromwhere": "<b>İletişim yöntemi:</b> %s\n",
        "fromwhere+name": "<b>İletişim yöntemi:</b> %s\n<b>İsim:</b> %s\n",
        "fromwhere+name+last_name": "<b>İletişim yöntemi:</b> %s\n<b>İsim:</b> %s\n<b>Soyisim:</b> %s\n",
        "fromwhere+name+last_name+phonenum": "<b>İletişim yöntemi:</b> %s\n<b>İsim:</b> %s\n<b>Soyisim:</b> %s\n<b>Telefon Numarası:</b> %s\n",
        "writename": "Müşterinizin adını yazın",
        "writelastname": "Müşterinizin soyadını yazın",
        "writephonenum": "Müşterinizin telefon numarasını yazın. Sadece rakamlar ve herhangi bir ara sembol olmadan",
        "saveorchange": "Müşterinizle ilgili bilgileri doldurmayı tamamladınız. Kaydetmek ister misiniz yoksa bir değişiklik yapmak mı istersiniz?",
        "data_save": "Yeni bir müşteri oluşturuldu",
        #Keybaord
        "teledirectionary": "Telefon rehberinden",
    #Change
        #Message
        "user_inf": "<b>İsim:</b> %s\n<b>Soyisim:</b> %s\n<b>Telefon Numarası:</b> %s\n<b>İletişim Yöntemi</b> %s\n<b>Dil:</b> %s\n",
        "choose_dir_for_change": "Değiştirmek istediğiniz şeyi seçin",
        "inf_saved": "Bilgiler kaydedildi\n",
        #Keyboard
        "fromwhere_kb": "İletişim Yöntemi",
        "name_kb": "İsim",
        "last_name_kb": "Soyisim",
        "phonenum_kb": "Telefon Numarası",
    #Delete
        #Message
        "client_delete": "Müşteriniz silindi!",
    #RegToGame
        #Message
        "type_seats": "Müşterinizin planladığı boş yer sayısını girin",
        "choose_paymethod": "Müşteriniz için ödeme yöntemini seçin",
        "client_reged": "Müşteri bu oyun için kaydedildi. Ona şunu bildirin - ziyareti için toplam maliyet %s %s olacaktır\n",
        #Keyboard
        "online": "Kart (online)",
        "cash": "Nakit",

#Activities
    #Preface
        #Message
        "Choose_dir_of_activities": "Tutumlarıyla ilgili bir yönlendirme seçin",
        "rules_for_chat_game": "\n\n\nP.S. Sohbet içinde bir oyun başlatmak için beni önce sohbete eklemeniz, ardından beni yönetici yapmanız ve sonrasında /add komutunu sohbete yazmanız gerekiyor. Ancak o zaman size sohbet içinde oyun oluşturmanıza yardımcı olabilirim",
        #Keyboard
        "reg_game": "Chat oyunu oluştur",
        "activ_game": "Aktif oyunlar",
    #Chat Game
        #Message
        "no_chats": "Bot hiçbir sohbete eklenmemiş!\n",
        "no_games": "Önce bir oyun oluşturun!\n",
        "game_rules": """Size sohbet veya grubunuzda bir oyun yapma önerisinde bulunuyorum. Oyunun özü şu: bir sohbet seçersiniz, bir oyun seçersiniz ve ben 'Katıl!' düğmesi içeren bir mesaj gönderirim. Müşterileriniz bu düğmeye tıklayarak otomatik olarak kayıt olabilirler. Bu oyundaki anahtar, bu özel düğmeye zamanında basabilmekte\n\n""",
        "foundchats": "Evee bulduğum sohbetler",
        "no_new_chats": "Hiçbir sohbet bulamadım! Lütfen beni bir sohbete ekleyin, yönetici yetkileri verin ve ardından bu işlemi tekrarlayın",
        "choose_game_for_chatgame": "Çatınızdan kaydolacak olan oyunu seçin",
        "choose_language": "Mesajın gönderileceği dilinizi seçin",
        "example_of_chat_game": """İşte grupta/sohbette görünecek bir örnek mesaj:\n\n\n""",
        "start_chatgame": """Merhaba herkese!\n"Kim önce yetişirse, o yer!" adlı oyunumuza başlıyoruz! Kayıtların açık olduğu oyun hakkında kısa bir bilgi ve zaten kayıt yaptıranların listesi aşağıda! Eğer kaçırmak istemiyorsan hemen 'Katıl' düğmesine bas!\n\n\n""",
        "seats_counter": "%d. %s\n",
        "theseatsisfree": "Boş yer var!",
        "chatgame_sended": "Mesaj gönderildi! Oyun başladı!\n",
        #Keyboard
        "show_chats": "Zaten bulunan sohbetleri göster",
        "new_chat": "Yeni sohbetleri tespit et",
        "send": "Gönder",
        "participate": "Katıl!",
    #Active Game
        #Message
        "active_games": "Aktif bir oyun seçin ve bekleyen müşterilerle ilgili daha fazla bilgi alın",
        "waiting_cl": "Oyunu Bekliyorlar:",
        "no_active_games": "Şu anda hiçbir oyun beklenmiyor!\n",
        "all_of_client_on_game": "İşte bu oyunu bekleyen tüm müşterileriniz. Birini seçerek müşteri bilgilerini görüntüleyebilir, onlarla iletişime geçebilir veya müşteriyi bu oyundan çıkarabilirsiniz",
        "disclaimer": """\n\nP.S. Eğer müşteri bot'a kayıtlıysa, altta "İletişime Geç" düğmesi bulunacaktır. Buna tıklayarak bu kişiyle iletişim kurabilirsiniz""" ,
        "client_removed": "Bu müşterinin bu oyuna kaydı silindi!\n",
        #Keyboard
        "removeforgame": "Oyundan kaldır",
        "call": "İletişime geç",
#Finances
    #Preface
        #Message
        "choose_money_dir": "Finanslarla ilgili bir yönlendirme seçin",

        #Keyboard
        "money_stat": "Finans istatistikleri",
        "money_paid_act": "Borçluları görüntüle",
    #See statistic
        #Message
        "see_stat1": "Tüm zamanlar için finans istatistiği:\n1. <b>Kazanç sağladınız:</b>",
        "see_stat2": "2. <b>Size borçlu olanlar:</b>",
        "no_stat": "Statistik bulunmuyor!\n",
        "money_have": "%s %s",
    #Paid Action
        #Message
        "choose_your_debtor": "İşte size borçlu olanlar. Herhangi birini seçin",
        "no_debtors": "Henüz hiç borçlu yok!\n",
        "cl_game_inf": "Müşterinin kayıtlı olduğu oyun:\n1. <b>Spor:</b> %s\n2. <b>Tarih:</b> %s\n3. <b>Saat:</b> %s\n4. <b>Ödeme Tutarı:</b> %s %s\n5. <b>Alınan Yer Sayısı:</b> %s\n6. <b>Ödeme Yöntemi:</b> %s\n\n",
        "client_paided": "Veriler güncellendi! Müşteri ödeme yaptı!\n",
        #Keyboard
        "paided": "Ödendi",
#Settings
    #Preface
        #Message
        "choose_dir_set": "Bot ayarlarında yönlendirmeleri seçin (şu anda sadece bir tane mevcut)",
        #Keyboard
        "change_lang": "Bot dilini değiştir",
    #Change Language
        #Message
        "choose_your_language": "Geçmek istediğiniz dili seçin",
        "language_changed": "Dil değiştirildi\n",
        #Keyboard "Rusça, İngilizce, Türkçe"
        "ru": "Rusça",
        "en": "İngilizce",
        "tur": "Türkçe", 




    
#For All
    #Messages
    #Keyboard
    "first_option": "Oyunlar",
    "second_option": "Müşteriler", 
    "third_option": "Aktivite", 
    "fourth_option": "Finans", 
    "fifth_option": "Ayarlar", 
    "yes": "Evet",
    "no": "Hayır",
}





String = {"en": en, "ru": ru, "tur": tur}