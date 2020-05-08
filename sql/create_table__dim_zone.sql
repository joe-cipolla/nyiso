CREATE TABLE public.dim_zone
(
    id integer NOT NULL DEFAULT 1,
    zone character varying(256) COLLATE pg_catalog."default" NOT NULL,
    iso_id integer NOT NULL,
    state_id integer,
    CONSTRAINT zone_pkey PRIMARY KEY (id),
    CONSTRAINT fk_iso FOREIGN KEY (iso_id)
        REFERENCES public.dim_iso (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID,
    CONSTRAINT fk_state FOREIGN KEY (state_id)
        REFERENCES public.dim_state (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public.dim_zone
    OWNER to admin;