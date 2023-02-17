# for each in range(0,10):
#     print(each)
count = 1
is_true = False
while is_true ==False:
    if count ==15:
        amazon_url = f"https://www.amazon.com/Hunger-Games-Trilogy-Catching-Mockingjay/product-reviews/0545670314/ref=cm_cr_dp_d_show_all_btm{count}?ie=UTF8&reviewerType=all_reviews"
        print(amazon_url)
        is_true=True
    else:
        amazon_url = f"https://www.amazon.com/Hunger-Games-Trilogy-Catching-Mockingjay/product-reviews/0545670314/ref=cm_cr_dp_d_show_all_btm{count}?ie=UTF8&reviewerType=all_reviews"
        print(amazon_url)
    count+= 1
# list = [each for each in range(0,10)]
# print(list)