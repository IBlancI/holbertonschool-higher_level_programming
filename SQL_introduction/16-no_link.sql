-- List all records with non-empty names from second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;