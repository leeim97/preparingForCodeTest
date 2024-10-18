def solution(phone_book):
    
    hash_m = {}
    
    for i in phone_book:
        hash_m[i]=1
        
    for sts in phone_book:
        arr= ""
        for s in sts:
            arr+=s
            if arr in hash_m and arr != sts:
                return False
        
    
    return True