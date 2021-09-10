--
-- PostgreSQL database dump
--

-- Dumped from database version 11.11
-- Dumped by pg_dump version 13.2

-- Started on 2021-09-10 11:00:47

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

--
-- TOC entry 202 (class 1259 OID 106487)
-- Name: actors; Type: TABLE; Schema: public; Owner: velda_admin
--

CREATE TABLE public.actors (
    id integer NOT NULL,
    name character varying,
    age integer,
    gender character varying
);


ALTER TABLE public.actors OWNER TO velda_admin;

--
-- TOC entry 203 (class 1259 OID 106493)
-- Name: actors_id_seq; Type: SEQUENCE; Schema: public; Owner: velda_admin
--

CREATE SEQUENCE public.actors_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actors_id_seq OWNER TO velda_admin;

--
-- TOC entry 4245 (class 0 OID 0)
-- Dependencies: 203
-- Name: actors_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: velda_admin
--

ALTER SEQUENCE public.actors_id_seq OWNED BY public.actors.id;


--
-- TOC entry 200 (class 1259 OID 106455)
-- Name: movies; Type: TABLE; Schema: public; Owner: velda_admin
--

CREATE TABLE public.movies (
    id integer NOT NULL,
    title character varying,
    release_date timestamp without time zone NOT NULL
);


ALTER TABLE public.movies OWNER TO velda_admin;

--
-- TOC entry 201 (class 1259 OID 106461)
-- Name: movies_id_seq; Type: SEQUENCE; Schema: public; Owner: velda_admin
--

CREATE SEQUENCE public.movies_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movies_id_seq OWNER TO velda_admin;

--
-- TOC entry 4246 (class 0 OID 0)
-- Dependencies: 201
-- Name: movies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: velda_admin
--

ALTER SEQUENCE public.movies_id_seq OWNED BY public.movies.id;


--
-- TOC entry 4108 (class 2604 OID 106495)
-- Name: actors id; Type: DEFAULT; Schema: public; Owner: velda_admin
--

ALTER TABLE ONLY public.actors ALTER COLUMN id SET DEFAULT nextval('public.actors_id_seq'::regclass);


--
-- TOC entry 4107 (class 2604 OID 106463)
-- Name: movies id; Type: DEFAULT; Schema: public; Owner: velda_admin
--

ALTER TABLE ONLY public.movies ALTER COLUMN id SET DEFAULT nextval('public.movies_id_seq'::regclass);


--
-- TOC entry 4238 (class 0 OID 106487)
-- Dependencies: 202
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: velda_admin
--

COPY public.actors (id, name, age, gender) FROM stdin;
2	Vin Diesel	53	M
6	Ryan Gosling	40	M
3	Will ferrell	53	M
5	Halle Berry	54	F
9	Jim Parsons	47	M
7	Thomas Brodie-Sangster	30	M
1	Jamie Lee Curtis	62	F
11	dwayne Johnson	48	M
10	Kiera Knightly	35	F
8	Whoopi Goldberg	65	F
\.


--
-- TOC entry 4236 (class 0 OID 106455)
-- Dependencies: 200
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: velda_admin
--

COPY public.movies (id, title, release_date) FROM stdin;
2	Willow	1988-05-20 00:00:00
4	The Goonies	1985-12-06 00:00:00
6	The Princess Bride	1987-10-09 00:00:00
3	Labyrinth	1986-11-28 00:00:00
5	Back to the Future	1985-12-20 00:00:00
9	The Dark Crystal	1982-12-17 00:00:00
7	Legend	1985-12-13 00:00:00
1	Driving Miss Daisy	1990-05-08 00:00:00
11	Gremlins	1984-06-08 00:00:00
10	Cocoon	1985-06-21 00:00:00
8	The Never Ending Story	1985-04-06 00:00:00
\.


--
-- TOC entry 4247 (class 0 OID 0)
-- Dependencies: 203
-- Name: actors_id_seq; Type: SEQUENCE SET; Schema: public; Owner: velda_admin
--

SELECT pg_catalog.setval('public.actors_id_seq', 12, true);


--
-- TOC entry 4248 (class 0 OID 0)
-- Dependencies: 201
-- Name: movies_id_seq; Type: SEQUENCE SET; Schema: public; Owner: velda_admin
--

SELECT pg_catalog.setval('public.movies_id_seq', 12, true);


--
-- TOC entry 4112 (class 2606 OID 106497)
-- Name: actors actors_pkey; Type: CONSTRAINT; Schema: public; Owner: velda_admin
--

ALTER TABLE ONLY public.actors
    ADD CONSTRAINT actors_pkey PRIMARY KEY (id);


--
-- TOC entry 4110 (class 2606 OID 106465)
-- Name: movies movies_pkey; Type: CONSTRAINT; Schema: public; Owner: velda_admin
--

ALTER TABLE ONLY public.movies
    ADD CONSTRAINT movies_pkey PRIMARY KEY (id);


-- Completed on 2021-09-10 11:01:00

--
-- PostgreSQL database dump complete
--

