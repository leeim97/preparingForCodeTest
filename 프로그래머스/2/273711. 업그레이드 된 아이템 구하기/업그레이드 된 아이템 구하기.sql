-- 코드를 작성해주세요
# RARE의 다음 업그레이드 아이템의 ID,이름,희귀도를 출력
# PARENT_ITEM_ID에 있는것중에서 RARE를 찾고 
# 부모가 찾은 값인 경우를 찾자
SELECT
    A.ITEM_ID, A.ITEM_NAME,A.RARITY
FROM
    ITEM_INFO A
JOIN 
    ITEM_TREE B
ON A.ITEM_ID = B.ITEM_ID
WHERE
     B.PARENT_ITEM_ID IN (
        SELECT
            ITEM_ID 
        FROM
            ITEM_INFO 
        WHERE
            RARITY = 'RARE')
ORDER BY ITEM_ID DESC;