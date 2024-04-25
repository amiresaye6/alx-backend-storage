-- Context: Calculate/compute something is always power intensive… better to distribute the load!
SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;
