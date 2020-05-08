CREATE TABLE public.da_asp
(
)

TABLESPACE pg_default;

ALTER TABLE public.da_asp
    OWNER to admin;
COMMENT ON TABLE public.da_asp
    IS 'day-ahead ancillary service prices';



CREATE TABLE public.da_lmp
(
    id integer NOT NULL DEFAULT nextval('da_lmp_id_seq'::regclass),
    date_id integer NOT NULL,
    zone_id integer NOT NULL,
    he01 numeric,
    he02 numeric,
    he03 numeric,
    he04 numeric,
    he05 numeric,
    he06 numeric,
    he07 numeric,
    he08 numeric,
    he09 numeric,
    he10 numeric,
    he11 numeric,
    he12 numeric,
    he13 numeric,
    he14 numeric,
    he15 numeric,
    he16 numeric,
    he17 numeric,
    he18 numeric,
    he19 numeric,
    he20 numeric,
    he21 numeric,
    he22 numeric,
    he23 numeric,
    he24 numeric,
    CONSTRAINT da_lmp_pkey PRIMARY KEY (id),
    CONSTRAINT fk_date FOREIGN KEY (date_id)
        REFERENCES public.dim_date (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_zone FOREIGN KEY (zone_id)
        REFERENCES public.dim_zone (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE public.da_lmp
    OWNER to admin;
COMMENT ON TABLE public.da_lmp
    IS 'day-ahead locational marginal prices';