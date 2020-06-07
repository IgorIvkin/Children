-- Table: public.users

-- DROP TABLE public.users;

CREATE SEQUENCE public.users_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.users_id_seq
    OWNER TO children;

-- Table: public.users

-- DROP TABLE public.users;

CREATE TABLE public.users
(
    id bigint NOT NULL DEFAULT nextval('users_id_seq'::regclass),
    login character varying(255) COLLATE pg_catalog."default" NOT NULL,
    id_oauth character varying(255) COLLATE pg_catalog."default",
    password character varying(255) COLLATE pg_catalog."default" NOT NULL,
    title character varying(255) COLLATE pg_catalog."default",
    created timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    updated timestamp with time zone DEFAULT CURRENT_TIMESTAMP,
    status boolean NOT NULL DEFAULT true,
    type integer NOT NULL DEFAULT 1,
    CONSTRAINT users_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.users
    OWNER to children;
-- Index: users_id_oauth_idx

-- DROP INDEX public.idx_id_oauth;

CREATE UNIQUE INDEX users_idx_id_oauth
    ON public.users USING btree
    (id_oauth COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: idx_login

-- DROP INDEX public.idx_login;

CREATE UNIQUE INDEX users_idx_login
    ON public.users USING btree
    (login COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;