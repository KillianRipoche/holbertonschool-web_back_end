-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT band_name,
       IFNULL(split, 2022) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
