-- 코드를 작성해주세요
# 점수가 가장 높은 사원의 점수, 사번, 성명, 직책, 이메일
# HR_GRADE에서 사번, 점수
# HR_EMPLOYEES에서 사번, 성명, 직책, 이메일
SELECT
    B.SCORE, A.EMP_NO, A.EMP_NAME, A.POSITION, A.EMAIL
FROM 
    HR_EMPLOYEES AS A
JOIN 
    (SELECT 
        EMP_NO, SUM(SCORE) AS SCORE
    FROM 
        HR_GRADE
    GROUP BY EMP_NO
    ORDER BY SCORE DESC) AS B
ON B.EMP_NO = A.EMP_NO
ORDER BY B.SCORE DESC
LIMIT 1;
