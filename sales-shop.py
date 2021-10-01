# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 23:08:45 2021

@author: ukouc
"""
import pandas as pd

class phoneTabletShop:
    
    global shopItems, x_phonetablets, x_simcards, x_case, x_charger
    global itemPrice, totalPrice, x_itemsPurchases, listPhoneTabletPrice
    
    """Mobiles devices, SIM Cards and Accessories Sales price calculation"""
    
# =============================================================================
#       Your program or programs must include appropriate prompts for the entry of data; 
#     data must be validated on entry.
# =============================================================================
    
    shopItems = {
        
           "Category": [
               "Phone", "Phone", "Phone", "Phone", "Phone", "Phone", "Tablet",
               "Tablet", "Tablet", "Tablet", "SIM card", "SIM card", "Case",
               "Case", "Charger", "Charger"
           ],
           "Item code": [
               "BPCM", "BPSH","RPSS", "RPLL", "YPLS", "YPLL", "RTMS", "RTML",
               "YTLM", "YTLL", "SMNO", "SMPG", "CSST", "CSLX", "CGCR", "CGHM"
           ],
           "Description": [
               "Compact", "Clam shell", "Robo phone - 5inch 64GB memory",
               "Robo phone - 6inch 256GB memory",
               "Y-phone standard 6inch 64GB memory", "Y-phone deluxe 6inch 256GB memory",
               "RoboTab - 8inch screen 64GB memory", "RoboTab - 10inch screen 128GB memory",
               "Y-tab standard - 10inch screen 128GB memory", "Y-tab delxue - 10inch screen 256GB memory",
               "Sim free (no Sim card)", "Pay as you go (with Sim card)", "Standard", "Luxury", "Car", "Home"
           ],
           "Price ($)": [
               29.99, 49.99, 199.99, 499.99, 549.99, 649.99, 149.99, 299.99, 
               499.99, 599.99, 0.00, 9.99, 0.00, 50.00, 19.99, 15.99
           ]
       }
    
# =============================================================================
#     Generating a dictionary of keys = Item code and values = phone / tablet
#     
# =============================================================================        
    phoneTab = shopItems["Category"][0:10]
    itemCode = shopItems["Item code"][0:10]
        
    x_phonetablets = {}
    for itCode, phonTab in zip(itemCode, phoneTab):
        x_phonetablets[itCode] = phonTab
    #print(x_phonetablets) # uncomment this line to print
    
    
# =============================================================================
#     Generating a dictionary of keys = Item code and values = SIM Card
#     
# =============================================================================
    smCard = shopItems["Category"][10:12]
    itemCode = shopItems["Item code"][10:12]
        
    x_simcards = {}
    for itCode, sCard in zip(itemCode, smCard):
        x_simcards[itCode] = sCard
    #print(x_simcards) # uncomment this line to print
        
# =============================================================================
#     Generating a dictionary of keys = Item code and values = case
#     
# =============================================================================    
    case = shopItems["Category"][12:14]
    itemCode = shopItems["Item code"][12:14]    
    x_case = {itCode:cs for (itCode, cs) in zip(itemCode, case)}
    #print(x_case) # uncomment this line to print
    

# =============================================================================
#     Generating a dictionary of keys = Item code and values = charger
#     
# =============================================================================

    charger = shopItems["Category"][14:16]
    itemCode = shopItems["Item code"][14:16]
    x_charger = {itCode:chg for (itCode, chg) in zip(itemCode, charger)}
    #print(x_charger) # uncomment this line to print
    
    
    listPhoneTabletPrice = []
    itemPrice = []
    x_itemsPurchases = []
    def selectPhoneTabletAccessory(self):
        
        def phTablet(self):
            phoneTablet = input("Enter phone or tablet code here: ").upper()
            x_itemsPurchases.append(phoneTablet)
            return phoneTablet
        
        
        def simCard(self):
            siCard = input("Enter sim card code here: ").upper()
            x_itemsPurchases.append(siCard)
            return siCard 
        
        
        def case(self):
            phoneTabCase = input("Enter case code here: ").upper()
            x_itemsPurchases.append(phoneTabCase)
            return phoneTabCase 
        
        
        def charger(self):
            phoneTabCharger = input("Select none, charger code or both here: ").upper()
            if phoneTabCharger == "BOTH":
                x_itemsPurchases.append(shopItems["Item code"][14:16])
            elif phoneTabCharger in shopItems["Item code"][14:16]:
                x_itemsPurchases.append(phoneTabCharger)    
                
            return phoneTabCharger 

        
        while True:
            x = phTablet(self)            
            if x in x_phonetablets:
                p = shopItems["Price ($)"][shopItems["Item code"].index(x)]
                #print(p) # uncomment this line to print
                itemPrice.append(p)
                listPhoneTabletPrice.append(p)
                break
            else:
                print("You have entered incorrect item code.")
            
        while True:
            y = simCard(self)
            if y in x_simcards:
                py = shopItems["Price ($)"][shopItems["Item code"].index(y)]
                #print(py) # uncomment this line to print
                itemPrice.append(py)
                break
            else:
                print("You have entered incorrect item code.")
            
        while True:
            z = case(self)
            if z in x_case:
                pz = shopItems["Price ($)"][shopItems["Item code"].index(z)]
                #print(pz) # uncomment this line to print
                itemPrice.append(pz)
                break
            else:
                print("You have entered incorrect item code.")


        while True:
            w = charger(self)
            if w in x_charger:
                pw = shopItems["Price ($)"][shopItems["Item code"].index(w)]
                #print(pw) # uncomment this line to print
                itemPrice.append(pw)
            elif w == "BOTH":
                charger_1 = shopItems["Price ($)"][shopItems["Item code"].index("CGCR")]
                charger_2 = shopItems["Price ($)"][shopItems["Item code"].index("CGHM")]
                itemPrice.append(charger_1)
                itemPrice.append(charger_2)
            
            break
        #print(itemPrice) # uncomment this line to print
        
       
        def priceSum(self):
            totalPrice = 0
            for x in itemPrice:
                totalPrice += x
            return(totalPrice)
        #print(priceSum(self)) # uncomment this line to print 
        
# =============================================================================
# When this function p.selectPhoneTabletAccessory() is invoked, please uncomment
# this blocks to print.
#         print("------------------------------------------------------------")
#         print("List of Items purchased: ",  x_itemsPurchases)
#         print("The total price of items purchased: " + "$", priceSum(self))
#         print("------------------------------------------------------------")
# =============================================================================
        return priceSum(self)
        
    
    
    def multiplePhoneTablet(self): #2
        numberPhoneTablet = int(input("Enter number of phone or tablet for purchase:"))
        
        #listPriceSum = []
        for i in range(numberPhoneTablet):
            price_sum = phoneTabletShop.selectPhoneTabletAccessory(self)
            #listPriceSum.append(price_sum)
            
            
        
# =============================================================================
# =============================================================================
#         def discount(self):
#             discounts = ((10/100) * (price_sum))
#             return discounts
# =============================================================================
        
        def discount(self):
            discounts = 0
            for i in range(1, len(listPhoneTabletPrice)):
                discounts += ((10/100) * (listPhoneTabletPrice[i]))
            return discounts

    
        if numberPhoneTablet == 1: #3
            print("------------------------------------------------------------")
            print("The total price of items purchased: " + "$",price_sum)
            print("List of Items purchased: ",  x_itemsPurchases)
        
        else:
            print("------------------------------------------------------------")
            print("The new price of 10% off: ", (price_sum - (discount(self))))
            #print("The new price of 10% off: ", (price_sum - (discount(self) * (numberPhoneTablet - 1))))
            print("List of Items purchased: ",  x_itemsPurchases)
# =============================================================================

# =============================================================================
#         print("The total price of items purchased: " + "$",price_sum)
#         print("List of Items purchased: ",  x_itemsPurchases)  
# =============================================================================
        return price_sum
             



def main():
    p = phoneTabletShop()
    
    #p.selectPhoneTabletAccessory() # Option for only one Phone / Tablet 
    
    p.multiplePhoneTablet() # Option to buy more than one Phone / Tablet




if __name__ == "__main__":
    df = pd.DataFrame(shopItems)
    print(df)
    print("====================================================================")
    print("Attention!!! Please, read the comments to understand the program.")
    print("Enter number of phones or tablets to place an order!")
    print("====================================================================")
    main()