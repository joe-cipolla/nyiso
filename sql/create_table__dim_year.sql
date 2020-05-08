CREATE TABLE public.dim_year
(
    year_id integer NOT NULL DEFAULT 1,
    year character varying(256) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT year_pkey PRIMARY KEY (year_id)
)

TABLESPACE pg_default;

ALTER TABLE public.dim_year
    OWNER to admin;