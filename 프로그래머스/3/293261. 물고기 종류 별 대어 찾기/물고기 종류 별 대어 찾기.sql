-- 코드를 작성해주세요
# 제일 큰놈의 ID와 길이를 알아오자
SELECT A.ID, B.FISH_NAME, A.LENGTH
FROM FISH_INFO A
JOIN FISH_NAME_INFO B
ON A.FISH_TYPE = B.FISH_TYPE
WHERE 
    (A.FISH_TYPE, LENGTH) IN 
                        (SELECT FISH_TYPE, MAX(LENGTH)
                            FROM FISH_INFO
                            GROUP BY FISH_TYPE
                        )
    
# GROUP BY B.FISH_TYPE
# HAVING A.LENGTH = MAX(A.LENGTH)
# ORDER BY ID ASC;








# SELECT 
#     ID, FISH_NAME, LENGTH
# FROM
#     FISH_INFO A
# JOIN
#     FISH_NAME_INFO B
# ON
#     A.FISH_TYPE = B.FISH_TYPE
# WHERE (A.FISH_TYPE, A.LENGTH) IN (
#     SELECT 
#         FISH_TYPE, MAX(LENGTH)
#     FROM 
#         FISH_INFO
#     GROUP BY FISH_TYPE
#         );