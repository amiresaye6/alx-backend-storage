-- Context: Calculate/compute something is always power intensive… better to distribute the load!
SELECT origin, SUM(fan) AS nb_fans
    FROM metal_bands
    ORDER BY origin
    ORDER BY nb_fans DESC;
