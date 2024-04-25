-- Rank the countries by the number of fans
SELECT origin, nb_fans,
       RANK() OVER (ORDER BY nb_fans DESC) AS country_rank
FROM band_fans_count
ORDER BY nb_fans DESC;
