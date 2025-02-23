-- 코드를 작성해주세요
# 부서 ID, 영문 부서명, 평균 연봉
SELECT 
    B.DEPT_ID, A.DEPT_NAME_EN , B.AVG_SAL
FROM 
    HR_DEPARTMENT A
JOIN
    (SELECT 
        DEPT_ID , ROUND(AVG(SAL),0) AS AVG_SAL
    FROM
        HR_EMPLOYEES
    GROUP BY DEPT_ID) AS B
ON A.DEPT_ID = B.DEPT_ID
ORDER BY B.AVG_SAL DESC;