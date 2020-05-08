CREATE TABLE public.dim_season
(
    id integer NOT NULL DEFAULT nextval('dim_season_id_seq'::regclass),
    season character(256) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT season_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.dim_season
    OWNER to admin;