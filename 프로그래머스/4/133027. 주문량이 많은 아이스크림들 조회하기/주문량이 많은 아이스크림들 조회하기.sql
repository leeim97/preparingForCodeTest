select F.flavor
from FIRST_HALF F join (select flavor , sum(TOTAL_ORDER) as t from JULY
                       group by flavor) J 
                       on F.flavor = J.flavor
                       order by F.TOTAL_ORDER + J.t desc
                       limit 3;