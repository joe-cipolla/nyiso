CREATE TABLE public.dim_quarter
(
    id integer NOT NULL DEFAULT nextval('dim_quarter_id_seq'::regclass),
    quarter character(256) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT quarter_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.dim_quarter
    OWNER to admin;