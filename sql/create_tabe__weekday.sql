CREATE TABLE public.dim_weekday
(
    id integer NOT NULL DEFAULT nextval('dim_weekday_id_seq'::regclass),
    weekday character(256) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT weekday_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.dim_weekday
    OWNER to admin;