CREATE VIEW dst AS
SELECT d.id, s.date as start_date, d.start_time_he, e.date as end_date, d.end_time_he
FROM dim_dst AS d
JOIN dim_date AS s on d.start_date_id = s.id
JOIN dim_date AS e on d.end_date_id = e.id
