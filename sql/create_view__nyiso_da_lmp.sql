CREATE VIEW vw_nyiso_da_lmp AS
SELECT t.date, z.zone, d.he01, d.he01, d.he02, d.he03, d.he04, d.he05, d.he06, d.he07, d.he08,
d.he09, d.he10, d.he11, d.he12, d.he13, d.he14, d.he15, d.he16, d.he17, d.he18, d.he19, d.he20,
d.he21, d.he22, d.he23, d.he24 FROM da_lmp AS d
JOIN dim_date as t on d.date_id = t.id
JOIN dim_zone as z on d.zone_id = z.id