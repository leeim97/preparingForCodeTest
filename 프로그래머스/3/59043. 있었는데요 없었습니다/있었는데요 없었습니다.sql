-- 코드를 입력하세요
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_OUTS A
JOIN ANIMAL_INS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE
    B.DATETIME > A.DATETIME
ORDER BY 
    B.DATETIME

