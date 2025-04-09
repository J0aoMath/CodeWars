def sum_strings(x, y):
    algarisms = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,
                 '6':6,'7':7,'8':8,'9':9}
    ans = 0
    for i, (value,value_) in enumerate(zip(x[::-1],y[::-1])):
        ans += algarisms[value] * 10**i
        ans += algarisms[value_] * 10**i
        print(ans)
    print(f'ans: {ans}')


sum_strings('1000','1001')
sum_strings('1023','0932')
sum_strings('489345','219382931')
sum_strings('0129038','9328932')
