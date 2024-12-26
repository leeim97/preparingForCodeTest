-- 코드를 작성해주세요
SELECT 
    E.ID, COALESCE(B.CNT,0) AS CHILD_COUNT
FROM
    ECOLI_DATA E
    LEFT JOIN 
    (   SELECT
            PARENT_ID, COUNT(*) AS CNT 
         FROM 
            ECOLI_DATA
         GROUP BY
            PARENT_ID
         HAVING CNT IS NOT NULL
    ) AS B
ON 
    B.PARENT_ID = E.ID
ORDER BY ID ASC;

# SELECT * FROM ECOLI_DATA;