INSERT INTO Users (user_id, username, name, last_name, level, action, language) VALUES (738070596, 'l1qwie', 'Bogdan', 'Dmitriev', 3, 'divarication', 'ru');
INSERT INTO Schedule (game_id, sport, date, time, seats, latitude, longitude, address, price, currency, status) VALUES 
    (999, 'volleyball', 20241212, 1210, 66, 36.893445, 30.709591, 'Alye, da?', 18, 'USDT', 1);
INSERT INTO Schedule (game_id, sport, date, time, seats, latitude, longitude, address, price, currency, status) VALUES 
    (9122, 'football', 20241112, 1010, 16, 36.893445, 30.709591, 'Alye, da?', 99, 'POUNDS', 1);
INSERT INTO Schedule (game_id, sport, date, time, seats, latitude, longitude, address, price, currency, status) VALUES 
    (434, 'volleyball', 20241012, 1230, 86, 36.893445, 30.709591, 'Alye, da?', 20, 'RUB', 1);
INSERT INTO Schedule (game_id, sport, date, time, seats, latitude, longitude, address, price, currency, status) VALUES 
    (665, 'football', 20241217, 1900, 46, 36.893445, 30.709591, 'Alye, da?', 19, 'USDT', 1);

INSERT INTO Schedule (game_id, sport, date, time, seats, latitude, longitude, address, price, currency, status) VALUES 
    (88888, 'football', 20241222, 1700, 46, 36.893445, 30.709591, 'Al, da?', 19, 'UT', -1);
INSERT INTO Admins_password (password) VALUES ('111');
INSERT INTO Users (user_id, username, name, last_name, level, action, language, user_admin) VALUES (-1, 'l1qwie', 'nataniel', 'sahar', 3, 'divarication', 'ru', true);
INSERT INTO WatingForGamesUsers (user_id, game_id, seats, payment) VALUES ( -1, 9122, 6, 'card');