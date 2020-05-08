CREATE TABLE public.dim_iso
(
    id integer NOT NULL DEFAULT nextval('dim_iso_id_seq'::regclass),
    iso character(256) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT iso_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.dim_iso
    OWNER to admin;