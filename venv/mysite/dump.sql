--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 13.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO admin;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO admin;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO admin;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO admin;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO admin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO admin;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO admin;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO admin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO admin;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO admin;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO admin;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO admin;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO admin;

--
-- Name: kintai_touroku_info; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.kintai_touroku_info (
    syaincd character varying(8) NOT NULL,
    syainname character varying(8) NOT NULL,
    ymd date NOT NULL,
    starttime time(4) without time zone NOT NULL,
    endtime time(6) without time zone NOT NULL,
    worktime numeric(8,2) NOT NULL,
    overtime numeric(8,2) NOT NULL,
    mntime numeric(8,2),
    mnovertime numeric(8,2),
    morning numeric(8,2),
    paidtime numeric(8,2),
    resttime numeric(8,2),
    attkbn integer NOT NULL,
    holidaykbn integer,
    holidayriyu character varying(32),
    todokekbn integer NOT NULL,
    todoke_tikoku integer,
    todoke_soutai integer,
    todoke_midnight integer,
    todoke_hayade integer,
    todoke_irregular integer,
    todoke_holiwork integer,
    id smallint,
    projectname1 character varying(16),
    kouteiname1 character varying(16),
    workname1 character varying(32),
    start1 time(6) without time zone,
    end1 time(6) without time zone,
    rest1 numeric(8,2),
    projectname2 character varying(16),
    kouteiname2 character varying(16),
    workname2 character varying(32),
    start2 time(6) without time zone,
    end2 time(6) without time zone,
    rest2 numeric(8,2),
    projectname3 character varying(16),
    kouteiname3 character varying(16),
    workname3 character varying(32),
    start3 time(6) without time zone,
    end3 time(6) without time zone,
    rest3 numeric(8,2),
    projectname4 character varying(16),
    kouteiname4 character varying(16),
    workname4 character varying(32),
    start4 time(6) without time zone,
    end4 time(6) without time zone,
    rest4 numeric(8,2),
    projectcd1 character varying(8),
    kouteicd1 character varying(8),
    workcd1 character varying(8),
    projectcd2 character varying(8),
    kouteicd2 character varying(8),
    workcd2 character varying(8),
    projectcd3 character varying(8),
    kouteicd3 character varying(8),
    workcd3 character varying(8),
    projectcd4 character varying(8),
    kouteicd4 character varying(8),
    workcd4 character varying(8)
);


ALTER TABLE public.kintai_touroku_info OWNER TO admin;

--
-- Name: project_work; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.project_work (
    projectname character varying(16) NOT NULL,
    kouteicd character varying(8) NOT NULL,
    kouteiname character varying(32) NOT NULL,
    workcd character varying(8) NOT NULL,
    workname character varying(32) NOT NULL,
    id smallint,
    projectcd character varying(8)
);


ALTER TABLE public.project_work OWNER TO admin;

--
-- Name: syain_info; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.syain_info (
    syaincd character varying(8) NOT NULL,
    syainname character varying(16),
    password character varying(12),
    id smallint
);


ALTER TABLE public.syain_info OWNER TO admin;

--
-- Name: syukketsu_info; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.syukketsu_info (
    att_kbn character varying(8) NOT NULL,
    holiday_kbn integer NOT NULL,
    holiday_riyu character varying(8) NOT NULL
);


ALTER TABLE public.syukketsu_info OWNER TO admin;

--
-- Name: todoke_info; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.todoke_info (
    todoke_tikoku integer,
    todoke_soutai integer,
    todoke_midnight integer,
    todoke_hayade integer,
    todoke_irregular integer,
    todoke_holiwork integer
);


ALTER TABLE public.todoke_info OWNER TO admin;

--
-- Name: torihikisaki_list; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.torihikisaki_list (
    customname character varying(16) NOT NULL,
    id smallint
);


ALTER TABLE public.torihikisaki_list OWNER TO admin;

--
-- Name: trans_info; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.trans_info (
    tourokuno character varying(8) NOT NULL,
    tourokukbn character varying(8) NOT NULL,
    syaincd character varying(8) NOT NULL,
    syainname character varying(16) NOT NULL,
    tourokudate date NOT NULL,
    startdate date NOT NULL,
    enddate date,
    homon character varying(16) NOT NULL,
    kamoku character varying(8) NOT NULL,
    syudan character varying(8) NOT NULL,
    transport integer NOT NULL,
    k_seikyu character varying(1) NOT NULL,
    customname character varying(16) NOT NULL,
    seisan_kbn character varying(8) NOT NULL,
    id smallint
);


ALTER TABLE public.trans_info OWNER TO admin;

--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add sample db	7	add_sampledb
26	Can change sample db	7	change_sampledb
27	Can delete sample db	7	delete_sampledb
28	Can view sample db	7	view_sampledb
29	Can add sample d b2	8	add_sampledb2
30	Can change sample d b2	8	change_sampledb2
31	Can delete sample d b2	8	delete_sampledb2
32	Can view sample d b2	8	view_sampledb2
33	Can add projectwork	9	add_projectwork
34	Can change projectwork	9	change_projectwork
35	Can delete projectwork	9	delete_projectwork
36	Can view projectwork	9	view_projectwork
37	Can add project_work	10	add_project_work
38	Can change project_work	10	change_project_work
39	Can delete project_work	10	delete_project_work
40	Can view project_work	10	view_project_work
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
2	pbkdf2_sha256$216000$trKgLMn5ewpA$huRhPiRwAnWoBpzlq84kSfl8pno2aw9bQsJwC2EKkSA=	2020-11-20 18:54:56.086277+09	t	FOSNET				t	t	2020-11-20 18:51:51.303399+09
3	pbkdf2_sha256$216000$Ng1GRzINxsot$+y52iqFmYjMgGPAMyZzlrUR3OGaE4fKscchEcpgRODM=	2021-02-01 10:57:26.629817+09	t	kitaizumi				t	t	2021-02-01 10:21:23.843107+09
1	pbkdf2_sha256$216000$V7mXEbFvmmaT$KxePuDZvHt/+cKKDcF6sVhrZfkPMVko1P/sFNRR5TZY=	2021-02-01 13:43:01.449519+09	t	fosnet				t	t	2020-11-20 18:32:35.574728+09
4	pbkdf2_sha256$216000$m9Bi3vC036T7$e9MTyK6xWX7SaUOCQ6W2Q1vNjgDSCLDrhVPxK82o3Ek=	\N	f	kitaizumikento			j1409032@gmail.com	f	f	2021-02-01 16:14:02.991002+09
5	pbkdf2_sha256$216000$mZHf4JL3UlO3$vPgAW4LsGzHz83utzfofyA/IFpN8MQLX/ayW/KIC1uc=	\N	f	kitaizumikento2			j1409032@gmail.com	f	f	2021-02-01 16:17:29.637275+09
6	pbkdf2_sha256$216000$ehAFmjL5iWZr$1aIa8TzPqhWX+LpECBgvH+6KqQyETMdHUVzeevPtCVU=	\N	f	kitaizumikento3			j1409032@gmail.com	f	f	2021-02-01 16:19:05.674867+09
7	pbkdf2_sha256$216000$lQZy9lbCArkb$5VLAWOaZDgzKuK7gzAM3mz5avHRkKztp2aCbvOhRYko=	\N	f	kitaizumikento4			j1409032@gmail.com	f	f	2021-02-01 16:20:42.006187+09
8	pbkdf2_sha256$216000$8pOtOaNpYWby$vjd6yeaGMQeEVG0MADi7p+CfWvoQ69WxtTU+BRr8bqM=	\N	f	kitaizumikento5			j1409032@gmail.com	f	f	2021-02-01 16:26:16.010832+09
9	pbkdf2_sha256$216000$wtVnO8LJlrpA$AdbmuZOX+QR42v0x5CrI40HD05kg4wYXx3nRXUALlPI=	\N	f	kitaizumikento55			j1409032@gmail.com	f	f	2021-02-01 16:42:56.889812+09
10	pbkdf2_sha256$216000$HeThl1H3ehmj$Jyxgm/RqJ+gS0mImDq75NcdByNoHVaPCsMybwcxZA54=	\N	f	kitaizumikento552			j1409032@gmail.com	f	f	2021-02-01 18:02:13.92242+09
11	pbkdf2_sha256$216000$7lsApLJURR8H$dd8HHYTa24rge6vUGfudwBVZuOAXWdftxsFEwchGT2U=	\N	f	fosnet33333			kitaizumi-kento@fosnet.co.jp	f	f	2021-02-01 19:00:25.575328+09
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2020-11-27 13:21:10.343398+09	1	SampleDB object (1)	1	[{"added": {}}]	7	1
2	2020-11-27 13:21:45.740002+09	1	SampleDB object (1)	2	[]	7	1
3	2020-11-27 13:21:52.827896+09	2	SampleDB object (2)	1	[{"added": {}}]	7	1
4	2020-11-27 14:48:51.858964+09	3	SampleDB object (3)	1	[{"added": {}}]	7	1
5	2020-11-27 14:52:38.325205+09	3	SampleDB object (3)	3		7	1
6	2020-11-27 14:52:38.327202+09	2	SampleDB object (2)	3		7	1
7	2020-11-27 14:52:56.644907+09	4	SampleDB object (4)	1	[{"added": {}}]	7	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	app_folder	sampledb
8	app_folder	sampledb2
9	app_folder	projectwork
10	app_folder	project_work
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2020-11-20 18:30:47.508948+09
2	auth	0001_initial	2020-11-20 18:30:47.563295+09
3	admin	0001_initial	2020-11-20 18:30:47.631228+09
4	admin	0002_logentry_remove_auto_add	2020-11-20 18:30:47.64433+09
5	admin	0003_logentry_add_action_flag_choices	2020-11-20 18:30:47.651489+09
6	contenttypes	0002_remove_content_type_name	2020-11-20 18:30:47.667448+09
7	auth	0002_alter_permission_name_max_length	2020-11-20 18:30:47.675405+09
8	auth	0003_alter_user_email_max_length	2020-11-20 18:30:47.683386+09
9	auth	0004_alter_user_username_opts	2020-11-20 18:30:47.690016+09
10	auth	0005_alter_user_last_login_null	2020-11-20 18:30:47.696+09
11	auth	0006_require_contenttypes_0002	2020-11-20 18:30:47.698994+09
12	auth	0007_alter_validators_add_error_messages	2020-11-20 18:30:47.708143+09
13	auth	0008_alter_user_username_max_length	2020-11-20 18:30:47.724102+09
14	auth	0009_alter_user_last_name_max_length	2020-11-20 18:30:47.73208+09
15	auth	0010_alter_group_name_max_length	2020-11-20 18:30:47.741054+09
16	auth	0011_update_proxy_permissions	2020-11-20 18:30:47.748036+09
17	auth	0012_alter_user_first_name_max_length	2020-11-20 18:30:47.757019+09
18	sessions	0001_initial	2020-11-20 18:30:47.765481+09
19	app_folder	0001_initial	2020-11-20 18:50:53.647821+09
20	app_folder	0002_auto_20201127_1443	2020-11-27 14:44:48.843325+09
21	app_folder	0003_auto_20201127_2030	2020-11-27 20:31:41.28554+09
22	app_folder	0004_auto_20201127_2046	2020-11-28 11:51:18.544439+09
23	app_folder	0002_auto_20201211_2044	2020-12-11 21:14:40.987245+09
24	app_folder	0003_auto_20201211_2104	2020-12-11 21:14:40.995045+09
25	app_folder	0004_auto_20201211_2222	2020-12-11 22:22:58.473873+09
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
8tn4ve4v6ejw5ojrku17ar4yj1iahj8g	.eJxdkNFugzAMRf8lz6sUQtfSfsVe-lYJGWJKBiRVEuhY1X-fSdBY9mL53GtfyX6yh_oGK8ve3JQuJ4UPdn4y5_HOzgxG37K3QKUED2S9VmxUjy4yfnkLf_wJekWEskwWybk4tBTLOc8o9gMcJbBM5Pv3w7EgZdly2GPtSRdcZDsudjwnpzOjR6VhwIys61gUjbyOJy54YgoyEyH_L-yjAJWLTd2qznRjhBZmkBh7RyugVh21-x0alNTq1vrVMsuxcwJdpSNbNa9LzoP1Xg1rOGq5gZnQbnS35pMeEM_MeX1YanUKfbFUeVwqyqAHBYICTZzZMkSSmCcU_vD6AWs6ngE:1lA0M6:aDKVYdYvKTyX88YGjeKzAh1JoYG8grH7M7KQcaCqiFs	2021-02-25 10:01:14.318539+09
jco9tx3htmjqv43mo9wlf48xcue3ib53	.eJxdkMsKwyAQRf_FdQOjSduku-66Lu0uGxOnEPIQdCyE0n-vj0Com4vnKFfHD3taNOzCAICzAyPtjB4d92Yn4al1JfSnkF0T13VIdQ6JKvpoZDTylc74jmtncaGxW1LlTU-Dkmti8OKhlR5RIWTMMxYZlxlXGR833mYo0_X3YXVppSShxQl78ixA8AJ4wRu_M2pHOCxyjm9oXS2FCglhHEvSEA0zphZc1A76jWanvUbkosxF9fffkb4_Y1l54w:1l2FCi:C3EUEIN-NsLQ7NMKSC75Cvu6CQJjYX1Kf6VoxylXXAU	2021-02-04 00:15:28.78879+09
guvi2tavg5nktw6eyyrwdufijrodbgkj	.eJxVjMsOwiAQRf-FtSE8Bgou3fsNZGBAqgaS0q6M_65NutDtPefcFwu4rTVsIy9hJnZmkp1-t4jpkdsO6I7t1nnqbV3myHeFH3Twa6f8vBzu30HFUb_1ZGMEax2oLB2pZDRInIwrNpmSirWEQsYMZLzXCoQnAS6BQk3kQBf2_gDRaTd8:1kkPjS:l2mOMpZNPD0cZytbpUBWJIXfqBXbHWTOp1wCJ6K1dRA	2020-12-16 19:51:34.072198+09
ck3szip72fj4prjwg5ao812fav5y2z57	eyJVc2VyIjoiMDAwMSIsIlBhc3MiOiJNYW1va2EwNDgifQ:1l42hN:prL68gYHxx-l1OGr0L9lJQigFzVzWGf8X2y_rcXqgNk	2021-02-08 23:18:33.579946+09
0l53qyuva9wi9u4baclfhrg4q34n77dw	.eJxlkU1uxCAMhe_Ceirxk0yT2fUKo3Y3Gyc4DcoMSAEqRVXvXgOpWlIJWf6enecYPtmbx5VdGOdcsBPzAdYQzAOzdOGcNLT6oLgPXHeJKLi4uiUKoltUfDynOPQ571LUzymiznpWICswlZ5fD1k5qoqaQouLAY2FB5aBXTeRcc8lr4ry2K2Owu6nIaDHO46BWHIpnjidM1VeBo82LINNmxNfzRbzyFY1tEU7dWPO4RabSaTbe3XaLaiR57aeNy01SDX8KYky9QdljarGpsa2IAy-_IaYIPlT24mNs1nokv4PnmEDvb-Up-XBlHxG68sHBA-jrXmfw15yd6NhS_D1DeNGoG0:1l3axY:UhellznjWXF-Atr1CKejlG4cULkTv-Zzn4-XSr2yseE	2021-02-07 17:41:24.405811+09
945ic1aqkegh7i5oqg8grkqmpzktcp8f	.eJxdjEsOwjAMRO-SNQs-3cAdkNhwAJcYYoXYUuwiRRV3J1ICqN3Ne-Px7K6K2Z3cXZTR3MZdQLXyGZJE2A7HqqJMhsSQcFebhdivxWEthiZg1BZugaLEqUGAAh5b1joB6h5Zf0eJPNMjWK_kSR7KAuLIjTOVPlKDbEapP0f2f5AX5i-9P-qITk8:1l6OMw:uexa0XL04KKU0cfVmLVfXGayfTVQkpu-AUquaFTYhZA	2021-02-15 10:51:10.563639+09
ypqkfypozj9zl380lfkpdh3kcvtq8wg3	.eJx9UU1LxDAQ_S89uyVfTVOPnrwIIngTlkkm3cbuJtCkwiL-d5O27FIPXoZ5H_NCX7-r92in6rEihNDqoQIdM8iLGdwYxnkFA1wB7brHMCdwG299vJkuDr07DWmTwtkhXLebBFNK7rJFWI93EL7sdEcpzFNOpDvEMvqYOTGyTN0tuyoT2zItLvzCwMJAv3rYPYTvIsWKxvwx1nm4WLq8oYBhmUTtRPafyP9GbdkIyUZ7tqY0wgijB0IPrMnKK8TSMmVcNLItac9rW6P26-2bu867Hm_KdFOOMKfhOOffd3RY4vacBjPmorOAn-BPoTbBp8npuljqTY31S0B7ftq8u4AB4pCvW6m1kFIJZqlCZhouKLSN6qVpetNLiUCotgKbruNMkA6JUEYw4IhK8L76-QX19bm1:1l5QSH:hTyQDUOqjhkuyWKYY2iE_hZf6b2dRGN0Rp2HIYoJ4Kk	2021-02-12 18:52:41.455364+09
a15po5r68e58dsca2mqrez3qwkj7cw11	e30:1l6R3F:h_j0bNiGBat7sQATZH2WkB-ZgF3wcWyZprO_PoOWME0	2021-02-15 13:43:01.431548+09
\.


--
-- Data for Name: kintai_touroku_info; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.kintai_touroku_info (syaincd, syainname, ymd, starttime, endtime, worktime, overtime, mntime, mnovertime, morning, paidtime, resttime, attkbn, holidaykbn, holidayriyu, todokekbn, todoke_tikoku, todoke_soutai, todoke_midnight, todoke_hayade, todoke_irregular, todoke_holiwork, id, projectname1, kouteiname1, workname1, start1, end1, rest1, projectname2, kouteiname2, workname2, start2, end2, rest2, projectname3, kouteiname3, workname3, start3, end3, rest3, projectname4, kouteiname4, workname4, start4, end4, rest4, projectcd1, kouteicd1, workcd1, projectcd2, kouteicd2, workcd2, projectcd3, kouteicd3, workcd3, projectcd4, kouteicd4, workcd4) FROM stdin;
0001	北泉賢人	2021-01-14	09:00:00	17:30:00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	1	1		0	0	0	0	0	0	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
0001	北泉賢人	2021-01-11	09:00:00	17:30:00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0	0		0	0	0	0	0	0	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
0001	北泉賢人	2021-01-19	13:13:00	19:15:00	5.53	0.00	0.00	0.00	0.00	0.00	0.50	0	5	午前半休	1	1	0	0	0	0	0	\N	テストプロジェクト	設計	基本設計	13:13:00	19:15:00	0.50				00:00:00	00:00:00	0.00				00:00:00	00:00:00	0.00				00:00:00	00:00:00	0.00	0000	0001	0000									
	北泉賢人	2020-11-20	09:00:00	17:30:00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0	0		0	0	0	0	0	0	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
0001	北泉賢人	2020-11-21	09:00:00	20:37:00	11.00	3.00	0.00	0.00	0.00	0.00	1.00	0	0		0	0	0	0	0	0	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
0001	北泉賢人	2020-12-28	09:43:00	20:43:00	10.00	3.00	0.00	0.00	0.00	0.00	1.00	0	0		0	0	0	0	0	0	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
0001	北泉賢人	2020-12-20	09:46:00	19:57:00	9.00	2.00	0.00	0.00	0.00	0.00	1.00	0	0		0	0	0	0	0	0	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
0001	北泉賢人	2020-12-06	09:51:00	20:56:00	10.00	3.00	0.00	0.00	0.00	0.00	1.00	0	0		0	0	0	0	0	0	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
0001	北泉賢人	2020-12-01	09:00:00	18:20:00	8.33	0.33	0.00	0.00	0.00	0.00	1.00	0	0		0	0	0	0	0	0	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
0001	北泉賢人	2021-01-01	09:00:00	18:00:00	7.50	0.00	0.00	0.00	0.00	0.00	1.50	0	0		0	0	0	0	0	0	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
0001	北泉賢人	2021-01-07	09:19:00	19:19:00	8.50	1.31	0.00	0.00	0.00	0.00	1.50	1	1		0	0	0	0	0	0	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
0001	北泉賢人	2021-01-08	09:00:00	17:30:00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	1	1		0	0	0	0	0	0	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
0001	北泉賢人	2021-01-05	09:00:00	17:30:00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	1	1		0	0	0	0	0	0	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
0001	北泉賢人	2021-01-15	09:00:00	17:30:00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	1	1		0	0	0	0	0	0	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
0001	北泉賢人	2021-01-09	09:00:00	18:59:00	8.48	0.98	0.00	0.00	0.00	0.00	1.50	0	0		0	0	0	0	0	0	0	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
0001	北泉賢人	2021-01-04	09:03:00	18:03:00	7.50	0.05	0.00	0.00	0.00	0.00	1.50	0	0		1	1	0	1	0	0	0	\N	テストプロジェクト	製造	プログラム作成(バグ修正)	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	0000	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
0001	北泉賢人	2021-01-28	09:00:00	17:30:00	7.50	0.00	0.00	0.00	0.00	0.00	1.00	0	0		0	0	0	0	0	0	0	\N	テストプロジェクト	製造	プログラム作成(新規)	09:00:00	17:30:00	1.00				00:00:00	00:00:00	0.00				00:00:00	00:00:00	0.00				00:00:00	00:00:00	0.00	0000	0002	0001									
0001	北泉賢人	2021-01-26	09:00:00	17:30:00	8.50	1.00	0.00	0.00	0.00	0.00	0.00	0	0		0	0	0	0	0	0	0	\N	テストプロジェクト	製造	プログラム作成(バグ修正)	09:00:00	17:30:00	0.00				00:00:00	00:00:00	0.00				00:00:00	00:00:00	0.00				00:00:00	00:00:00	0.00	0000	0002	0002									
0001	北泉賢人	2021-02-03	13:00:00	02:00:00	11.00	3.50	4.93	4.93	0.00	0.00	2.00	0	0		1	0	0	0	0	1	0	\N	テストプロジェクト	製造	プログラム作成(バグ修正)	13:00:00	02:00:00	2.00				00:00:00	00:00:00	0.00				00:00:00	00:00:00	0.00				00:00:00	00:00:00	0.00	0000	0002	0002									
0001	北泉賢人	2021-01-27	09:34:00	18:41:00	0.00	0.68	0.00	0.00	0.00	0.00	1.50	0	0		0	0	0	0	0	0	0	\N	テストプロジェクト	製造	プログラム作成(バグ修正)	09:34:00	18:41:00	1.50				00:00:00	00:00:00	0.00				00:00:00	00:00:00	0.00				00:00:00	00:00:00	0.00	0000	0002	0002									
0001	北泉賢人	2021-01-17	09:33:00	18:36:00	7.55	0.05	0.00	0.00	0.00	0.00	1.50	0	0		1	1	0	0	0	0	0	\N				00:00:00	00:00:00	0.00	テストプロジェクト	製造	プログラム作成(バグ修正)	09:33:00	18:36:00	1.50				00:00:00	00:00:00	0.00				00:00:00	00:00:00	0.00				0000	0002	0002						
\.


--
-- Data for Name: project_work; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.project_work (projectname, kouteicd, kouteiname, workcd, workname, id, projectcd) FROM stdin;
テストプロジェクト	0002	製造	0002	プログラム作成(バグ修正)	\N	0000
テストプロジェクト	0002	製造	0003	プログラム作成(機能追加)	\N	0000
テストプロジェクト	0002	製造	0001	プログラム作成(新規)	\N	0000
テストプロジェクト	0001	設計	0000	基本設計	\N	0000
テストプロジェクト2	0001	設計	0000	基本設計	\N	0001
\.


--
-- Data for Name: syain_info; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.syain_info (syaincd, syainname, password, id) FROM stdin;
0002	佐藤一郎	Mamoka050	\N
0000	佐藤	12345678	\N
		12345678	\N
0001	北泉賢人	12345678	\N
\.


--
-- Data for Name: syukketsu_info; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.syukketsu_info (att_kbn, holiday_kbn, holiday_riyu) FROM stdin;
\.


--
-- Data for Name: todoke_info; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.todoke_info (todoke_tikoku, todoke_soutai, todoke_midnight, todoke_hayade, todoke_irregular, todoke_holiwork) FROM stdin;
\.


--
-- Data for Name: torihikisaki_list; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.torihikisaki_list (customname, id) FROM stdin;
nec	\N
\.


--
-- Data for Name: trans_info; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.trans_info (tourokuno, tourokukbn, syaincd, syainname, tourokudate, startdate, enddate, homon, kamoku, syudan, transport, k_seikyu, customname, seisan_kbn, id) FROM stdin;
104	登録	0001	北泉賢人	2021-01-31	2020-12-31	2020-12-31	東京	交通費	電車	1000	有		口座振込	\N
1027	登録	0001	佐藤	2021-01-24	2020-11-01	2020-11-01	会社	交通費	電車	1200	無	0	口座振込	\N
1015	登録	0001	北泉賢人	2021-01-28	2020-11-20	2020-11-20	あいうえお	交通費	電車	1200	有	customname	口座振込	\N
1010	登録	0001	北泉賢人	2021-01-30	2020-11-20	2020-11-20	あいうえお	交通費	電車	1200	無		口座振込	\N
1011	登録	0001	北泉賢人	2021-01-30	2020-11-20	2020-11-20	あいうえお	交通費	電車	1200	無		口座振込	\N
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 40, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 11, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 7, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 10, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 25, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: kintai_touroku_info kintai_touroku_info_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.kintai_touroku_info
    ADD CONSTRAINT kintai_touroku_info_pkey PRIMARY KEY (syaincd, syainname, ymd);


--
-- Name: syukketsu_info syukketsu_info_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.syukketsu_info
    ADD CONSTRAINT syukketsu_info_pkey PRIMARY KEY (att_kbn);


--
-- Name: syain_info table_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.syain_info
    ADD CONSTRAINT table_key PRIMARY KEY (syaincd);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

