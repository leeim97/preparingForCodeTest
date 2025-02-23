-- 코드를 입력하세요
# 입양간 날짜 - 보호소 들어온 날짜
# 입양간 아이들 아이디 확인
SELECT 
    A.ANIMAL_ID, A.NAME 
FROM 
    ANIMAL_OUTS A
JOIN 
    ANIMAL_INS B
ON 
    A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY 
    (TIMESTAMPDIFF(DAY, B.DATETIME,A.DATETIME)) DESC
LIMIT 2;
    
