my_dict = {
    "Local Coffee 78215": {
        "address" : "302 Pearl Pkwy, San Antonio, TX 78215",
        "summary" : "Buzzy coffeehouse offering a changing selection of brews in an intimate, industrial-chic setting."
    },
    "Bakery Lorraine at the Pearl 78215" : {
     "address" : "306 Pearl Pkwy Ste 110, San Antonio, TX 78215",
    "summary" : "Bakeshop with a patio serving sandwiches & an array of cookies, tarts & muffins, plus coffee."
    }
}

def find_shop_by_zip(zip):
    out_report=""
    for shop , shop_info in my_dict.items():
        if shop.count(zip):
            out_report += shop 
            out_report += f"\n{shop_info['address']}"
            out_report += f"\n{shop_info['summary']}"
            out_report += f"\n------------------------------\n"
    return out_report

print('start')
print(find_shop_by_zip('78247'))
print('end')

coffee_shops ={
    "Local Coffee 78215": {
        "address" : "302 Pearl Pkwy, San Antonio, TX 78215",
        "summary" : "Buzzy coffeehouse offering a changing selection of brews in an intimate, industrial-chic setting."
    },
    "Bakery Lorraine at the Pearl 78215" : {
     "address" : "306 Pearl Pkwy Ste 110, San Antonio, TX 78215",
    "summary" : "Bakeshop with a patio serving sandwiches & an array of cookies, tarts & muffins, plus coffee."
    }
}