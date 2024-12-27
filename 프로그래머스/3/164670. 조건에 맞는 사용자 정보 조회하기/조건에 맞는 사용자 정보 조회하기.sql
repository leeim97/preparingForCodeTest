-- 코드를 입력하세요
SELECT 
    A.USER_ID, A.NICKNAME, CONCAT(CITY,' ',STREET_ADDRESS1,' ',STREET_ADDRESS2) AS '전체주소',
    CONCAT(SUBSTR(A.TLNO,1,3),'-',SUBSTR(A.TLNO,4,4),
           '-', SUBSTR(A.TLNO,8,4)) AS '전화번호'
FROM 
    USED_GOODS_USER A
WHERE 
    USER_ID IN 
    (SELECT 
        WRITER_ID
    FROM 
        USED_GOODS_BOARD
    GROUP BY
        WRITER_ID
    HAVING 
         COUNT(*)  >= 3)
ORDER BY 
    USER_ID DESC;

 # SELECT 
 #        WRITER_ID
 #    FROM 
 #        USED_GOODS_BOARD
 #    GROUP BY
 #        WRITER_ID
 #    HAVING 
 #         COUNT(*)  >= 3