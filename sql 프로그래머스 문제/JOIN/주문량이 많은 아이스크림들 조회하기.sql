select F.flavor
from FIRST_HALF F join (select flavor , sum(TOTAL_ORDER) as t from JULY
                       group by flavor) J
                       on F.flavor = J.flavor
                       order by F.TOTAL_ORDER + J.t desc
                       limit 3;


--  깨달은 점 FIRST_HALF가 join할 J는 정확히 JULY가 아닌
-- flavor,t 로 이루어진 테이블 인것 같다
-- 왜냐하면 order by F.TOTAL_ORDER + J.t desc 여기서
-- J.TOTAL_ORDER을 했는데 column이 존재 하지 않았기 때문이다.
-- 만약 JULY 그 자체 였다면 J.TOTAL_ORDER가 존재해야된다.(JULY 테이블에
-- TOTAL_ORDER 열이 있음)
-- 결국 flavor 와 t 로 이루어진 테이블 J인 것이다.
