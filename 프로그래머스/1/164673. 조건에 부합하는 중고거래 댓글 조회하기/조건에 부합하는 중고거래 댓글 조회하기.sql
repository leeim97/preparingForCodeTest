-- 코드를 입력하세요
# SELECT A.TITLE, A.BOARD_ID, B.REPLY_ID, B.WRITER_ID, B.CONTENTS,
# DATE_FORMAT(B.CREATED_DATE,'%Y-%m-%d') as CREATED_DATE
# FROM USED_GOODS_BOARD AS A
# JOIN USED_GOODS_REPLY AS B
# ON A.BOARD_ID = B.BOARD_ID
# WHERE B.CREATED_DATE BETWEEN '2022-10-01' AND '2022-10-31'
# ORDER BY B.CREATED_DATE ASC , A.TITLE ASC;

SELECT A.TITLE, b.BOARD_ID,  b.REPLY_ID, b.WRITER_ID, b.CONTENTS, 
DATE_FORMAT(b.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from USED_GOODS_BOARD AS A
join USED_GOODS_REPLY AS b
on  A.BOARD_ID = b.BOARD_ID 
where  SUBSTR(A.CREATED_DATE,1,7) = '2022-10'
ORDER BY b.CREATED_DATE ASC , A.TITLE ASC ;