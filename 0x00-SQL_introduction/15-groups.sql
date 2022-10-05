-- lists number of records with same score in second_table
SELECT score 'score' COUNT(score)
FROM second_table
GROUP BY score
ORDER BY COUNT(score) DESC
