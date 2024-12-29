-- 코드를 작성해주세요
# 스킬 코드에서 언어들 확인 후 PYTHON, C#에 해당하는 사람
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE 
    SKILL_CODE & (SELECT CODE
                  FROM SKILLCODES
                  WHERE 
                    NAME ='C#')
                  OR 
                      SKILL_CODE & (SELECT CODE
                  FROM SKILLCODES
                  WHERE 
                    NAME ='PYTHON')
ORDER BY ID









# SELECT 
#     ID,EMAIL,FIRST_NAME, LAST_NAME
# FROM 
#     DEVELOPERS A 
# WHERE
#     A.SKILL_CODE & (SELECT CODE FROM SKILLCODES 
#                    WHERE NAME = 'PYTHON')
#     OR  A.SKILL_CODE & (SELECT CODE FROM SKILLCODES 
#                    WHERE NAME = 'C#')
# ORDER BY ID;


# SELECT 
#     ID,EMAIL,FIRST_NAME, LAST_NAME
# FROM 
#     DEVELOPERS A 
# WHERE
#     A.SKILL_CODE & (
#     SELECT CODE FROM SKILLCODES
#     WHERE NAME IN ('Python','C#'))
# ORDER BY ID;