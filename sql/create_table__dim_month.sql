CREATE TABLE public.dim_month
(
    id integer NOT NULL DEFAULT nextval('dim_month_id_seq'::regclass),
    month character(256) COLLATE pg_catalog."default" NOT NULL,
    season_id integer NOT NULL,
    quarter_id integer NOT NULL,
    CONSTRAINT month_pkey PRIMARY KEY (id),
    CONSTRAINT fk_quarter FOREIGN KEY (quarter_id)
        REFERENCES public.dim_quarter (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_season FOREIGN KEY (season_id)
        REFERENCES public.dim_season (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.dim_month
    OWNER to admin;