-- Ranks country origins of bands ordered by number of fans

-- Select origin and the total number of fans per country
SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;
