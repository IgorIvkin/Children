-- SEQUENCE: public.cities_id_seq

-- DROP SEQUENCE public.cities_id_seq;

CREATE SEQUENCE public.cities_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.cities_id_seq
    OWNER TO children;

-- Table: public.cities

-- DROP TABLE public.cities;

CREATE TABLE public.cities
(
    id bigint NOT NULL DEFAULT nextval('cities_id_seq'::regclass),
    title character varying(255) COLLATE pg_catalog."default" NOT NULL,
    country character varying(2) COLLATE pg_catalog."default" NOT NULL,
    region character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT cities_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.cities
    OWNER to children;
-- Index: cities_idx_region

-- DROP INDEX public.cities_idx_region;

CREATE INDEX cities_idx_region
    ON public.cities USING btree
    (region COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: cities_idx_title

-- DROP INDEX public.cities_idx_title;

CREATE INDEX cities_idx_title
    ON public.cities USING btree
    (title COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;