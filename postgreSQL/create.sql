CREATE SEQUENCE adminuser_id
    INCREMENT -1
    START 1
    MINVALUE -9223372036854775807
    MAXVALUE 9223372036854775807
    CACHE 1;

CREATE SEQUENCE chats_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

CREATE SEQUENCE game_id_schedule
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

CREATE SEQUENCE id_db
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

CREATE SEQUENCE mediarepository_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

CREATE TABLE admins
(
    user_id bigint NOT NULL,
    name text COLLATE pg_catalog."default",
    last_name text COLLATE pg_catalog."default",
    username text COLLATE pg_catalog."default",
    action text COLLATE pg_catalog."default",
    level integer,
    last_time_use timestamp without time zone,
    name_address_schedule text COLLATE pg_catalog."default",
    price_schedule text COLLATE pg_catalog."default",
    currency_schedule text COLLATE pg_catalog."default",
    language text COLLATE pg_catalog."default",
    custom_language boolean DEFAULT false,
    game_launch_point integer DEFAULT 0,
    game_sport text COLLATE pg_catalog."default",
    game_date integer,
    game_time integer,
    game_seats integer,
    game_price integer,
    game_currency text COLLATE pg_catalog."default",
    game_latitude double precision,
    game_longitude double precision,
    game_nameaddress text COLLATE pg_catalog."default",
    status integer DEFAULT 0,
    game_change_direction text COLLATE pg_catalog."default",
    game_game_id integer,
    game_change_create boolean DEFAULT false,
    game_typeofchange text COLLATE pg_catalog."default",
    client_fromwhere text COLLATE pg_catalog."default",
    client_name text COLLATE pg_catalog."default",
    client_last_name text COLLATE pg_catalog."default",
    client_phonenum bigint,
    client_user_id bigint,
    client_change_option text COLLATE pg_catalog."default",
    client_changeddata_str text COLLATE pg_catalog."default",
    client_changeddata_int bigint,
    client_launch_point integer DEFAULT 0,
    client_changedata_str text,
    client_changedata_int INTEGER,
    newchats boolean DEFAULT false,
    activities_actwithchats text COLLATE pg_catalog."default",
    activities_launch_point integer DEFAULT 0,
    activities_chat_id bigint,
    activities_game_id integer,
    client_game_id integer,
    client_seats integer,
    client_paymethod text COLLATE pg_catalog."default",
    finances_user_id integer,
    exmess integer DEFAULT '-1'::integer,
    direction text COLLATE pg_catalog."default",
    activities_chat_language text COLLATE pg_catalog."default",
    CONSTRAINT admins_pkey PRIMARY KEY (user_id)
);

CREATE TABLE admins_password
(
    password text COLLATE pg_catalog."default"
);

CREATE TABLE chats
(
    chat_id bigint,
    title text COLLATE pg_catalog."default",
    id integer NOT NULL DEFAULT nextval('chats_id_seq'::regclass),
    message_id bigint,
    language_of_message text COLLATE pg_catalog."default",
    CONSTRAINT chats_pkey PRIMARY KEY (id)
);

CREATE TABLE clients
(
    user_id bigint NOT NULL,
    db_name text COLLATE pg_catalog."default" NOT NULL,
    reg_time timestamp without time zone,
    connection text COLLATE pg_catalog."default",
    status text COLLATE pg_catalog."default",
    CONSTRAINT clients_pkey PRIMARY KEY (user_id, db_name)
);

CREATE TABLE schedule
(
    game_id integer NOT NULL,
    sport text COLLATE pg_catalog."default",
    date integer,
    "time" integer,
    seats integer,
    latitude double precision,
    longitude double precision,
    address text COLLATE pg_catalog."default",
    price integer,
    currency text COLLATE pg_catalog."default",
    status integer DEFAULT 0,
    CONSTRAINT schedule_pkey PRIMARY KEY (game_id)
);

CREATE TABLE users
(
    user_id bigint NOT NULL,
    name text COLLATE pg_catalog."default",
    last_name text COLLATE pg_catalog."default",
    username text COLLATE pg_catalog."default",
    from_where text COLLATE pg_catalog."default",
    language text COLLATE pg_catalog."default",
    user_admin boolean,
    action text COLLATE pg_catalog."default",
    setup_reg text COLLATE pg_catalog."default",
    actionwithmes text COLLATE pg_catalog."default" DEFAULT 'DEL'::text,
    level integer,
    game_id_reg_to_game integer,
    launch_point_reg_to_game integer DEFAULT 0,
    sport_reg_to_game text COLLATE pg_catalog."default",
    seats_reg_to_game integer,
    payment_reg_to_game text COLLATE pg_catalog."default",
    media_time_interval text COLLATE pg_catalog."default",
    media_direction text COLLATE pg_catalog."default",
    media_limit integer,
    media_launch_point integer DEFAULT 0,
    del_game_game_id integer,
    id_mediagroup text COLLATE pg_catalog."default" DEFAULT '0'::text,
    counter_mediagroup integer DEFAULT 0,
    us_set_lanuch_point integer DEFAULT 0,
    us_set_what_set text COLLATE pg_catalog."default",
    us_set_game_id integer,
    us_set_act_game text COLLATE pg_catalog."default",
    us_set_what_we_will_change text COLLATE pg_catalog."default",
    us_set_new_pay text COLLATE pg_catalog."default",
    notifgameid integer,
    last_time_use timestamp without time zone,
    custom_language boolean DEFAULT false,
    phone_number bigint,
    status integer DEFAULT 1,
    exmess integer DEFAULT '-1'::integer,
    CONSTRAINT users_pkey PRIMARY KEY (user_id)
);

CREATE TABLE mediarepository
(
    game_id integer,
    user_id integer,
    file_id text COLLATE pg_catalog."default",
    typeoffile text COLLATE pg_catalog."default",
    counter integer DEFAULT 0,
    status integer DEFAULT 0,
    id integer NOT NULL DEFAULT nextval('mediarepository_id_seq'::regclass),
    CONSTRAINT mediarepository_pkey PRIMARY KEY (id),
    CONSTRAINT fk_game_id FOREIGN KEY (game_id)
        REFERENCES public.schedule (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_user_id FOREIGN KEY (user_id)
        REFERENCES public.users (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE waitingfornotification
(
    game_id integer,
    admin_id bigint,
    user_id bigint,
    status text COLLATE pg_catalog."default",
    setup text COLLATE pg_catalog."default",
    whonotif text COLLATE pg_catalog."default",
    user_answer text COLLATE pg_catalog."default",
    counter_notif integer DEFAULT 0,
    for_tests text COLLATE pg_catalog."default",
    last_time_notif timestamp without time zone
);

CREATE TABLE watingforgamesusers
(
    user_id bigint,
    game_id integer,
    seats integer,
    payment text COLLATE pg_catalog."default",
    status_payment integer DEFAULT 0,
    status integer DEFAULT 0,
    CONSTRAINT watingforgamesusers_game_id_fkey FOREIGN KEY (game_id)
        REFERENCES public.schedule (game_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT watingforgamesusers_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public.users (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);