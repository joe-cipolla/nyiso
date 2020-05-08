CREATE TABLE public.dim_state
(
    id integer NOT NULL DEFAULT nextval('dim_state_id_seq'::regclass),
    state character(256) COLLATE pg_catalog."default" NOT NULL,
    iso_id integer NOT NULL,
    timezone_id integer NOT NULL,
    CONSTRAINT state_pkey PRIMARY KEY (id),
    CONSTRAINT fk_iso FOREIGN KEY (iso_id)
        REFERENCES public.dim_iso (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_timezone FOREIGN KEY (timezone_id)
        REFERENCES public.dim_timezone (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE public.dim_state
    OWNER to admin;