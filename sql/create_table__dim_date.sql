CREATE TABLE public.dim_date
(
    id integer NOT NULL DEFAULT nextval('dim_date_id_seq'::regclass),
    date date NOT NULL,
    weekday_id integer NOT NULL,
    month_id integer NOT NULL,
    year_id integer NOT NULL,
    season_id integer NOT NULL,
    quarter_id integer NOT NULL,
    CONSTRAINT date_pkey PRIMARY KEY (id),
    CONSTRAINT fk_month FOREIGN KEY (month_id)
        REFERENCES public.dim_month (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_quarter FOREIGN KEY (quarter_id)
        REFERENCES public.dim_quarter (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_season FOREIGN KEY (season_id)
        REFERENCES public.dim_season (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT fk_weekday FOREIGN KEY (weekday_id)
        REFERENCES public.dim_weekday (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_year FOREIGN KEY (year_id)
        REFERENCES public.dim_year (year_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.dim_date
    OWNER to admin;