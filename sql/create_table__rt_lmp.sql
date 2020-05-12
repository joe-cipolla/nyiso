CREATE TABLE public.rt_lmp
(
    id SERIAL,
    date_id integer NOT NULL,
    zone_id integer NOT NULL,
    he01 numeric(7,2),
    he02 numeric(7,2),
    he03 numeric(7,2),
    he04 numeric(7,2),
    he05 numeric(7,2),
    he06 numeric(7,2),
    he07 numeric(7,2),
    he08 numeric(7,2),
    he09 numeric(7,2),
    he10 numeric(7,2),
    he11 numeric(7,2),
    he12 numeric(7,2),
    he13 numeric(7,2),
    he14 numeric(7,2),
    he15 numeric(7,2),
    he16 numeric(7,2),
    he17 numeric(7,2),
    he18 numeric(7,2),
    he19 numeric(7,2),
    he20 numeric(7,2),
    he21 numeric(7,2),
    he22 numeric(7,2),
    he23 numeric(7,2),
    he24 numeric(7,2),
    CONSTRAINT rt_lmp_pkey PRIMARY KEY (id),
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

ALTER TABLE public.rt_lmp
    OWNER to admin;