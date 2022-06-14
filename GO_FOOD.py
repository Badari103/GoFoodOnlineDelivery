class GoFood:
    def __init__(self):
        self.go_food_items={"Pizza":150,"Burger":100,"Coke":50,"Brownies":60}
        self.special_days=["25th December","4th November","9th December"]
        self.peak_hours=["11am-2pm","6pm-8pm"]
        self.night_charges=["11pm-4am"]
        self.normal_charges=["2.01pm-5.59pm","8.01pm-10.59pm","4.01am-10.59am"]
    def display_items(self):
        print("Items",":","Price",sep=' ')
        for key,values in self.go_food_items.items():
            print(key,values,sep=' ')
    def display_special_days(self):
        print("The Special Days are :- ")
        for day in self.special_days:
            print(day)
    def display_peak_hours(self):
        print("The Peak Hours are :- ")
        for hours in self.peak_hours:
            print(hours)
    def display_night_charges(self):
        print("The Night Charges for the Hours are :- ")
        for hours in self.night_charges:
            print(hours)
    def display_normal_charges(self):
        print("The Normal Hourse are:- ")
        for hours in self.normal_charges:
            print(hours)

class GenerateAmount():
    def __init__(self,input_items,input_special_day,input_peak_hours,input_night_hours,input_normal_charges):
        self.input_items=input_items
        self.input_special_day=input_special_day
        self.input_peak_hours=input_peak_hours
        self.input_night_hours=input_night_hours
        self.input_normal_charges=input_normal_charges
        self.obj_go_food=GoFood()
        self.items_go_food=self.obj_go_food.go_food_items
    def special_day_amount(self):
        self.dict_for_special_day={"yes":50,"no":0}
        self.amount_special_day=self.dict_for_special_day[self.input_special_day]
        return self.amount_special_day
    def peak_hour_amount(self):
        self.dict_for_peak_hour={"yes":30,"no":0}
        self.amount_peak_hour=self.dict_for_peak_hour[self.input_peak_hours]
        return self.amount_peak_hour
    def night_hours_amount(self):
        self.dict_for_night_hours={"yes":20,"no":0}
        self.amount_night_hours=self.dict_for_night_hours[self.input_night_hours]
        return self.amount_night_hours
    def normal_charges_amount(self):
        self.dict_for_normal_charges={"yes":20,"no":0}
        self.amount_normal_charges=self.dict_for_normal_charges[self.input_normal_charges]
        return self.amount_normal_charges
    def amount_gst(self):
        self.gst_amount=0
        self.amount_list=[]
        for items in self.input_items[:len(self.input_items)-1]:
            values=self.items_go_food[items]
            amt=values*0.05
            gst_amount=values+amt
            self.amount_list.append(gst_amount)
        return sum(self.amount_list)
class GenerateBill(GenerateAmount):
    def _init_(self,input_items,input_special_day,input_peak_hours,input_night_hours,input_normal_charges):
        GenerateAmount.__init__(self,input_items,input_special_day,input_peak_hours,input_night_hours,input_normal_charges)
    
    def final_bill(self):
        self.final_amount=self.special_day_amount()+self.peak_hour_amount()+self.night_hours_amount()+self.normal_charges_amount()
        self.gst_amount=self.amount_gst()
        print("The Total Bill Amount is :- ",self.final_amount+self.gst_amount)
def getInput(obj_go_food):
    obj_go_food.display_items()
    print("Select The Items :- ")
    items=[]
    input_value=''
    while input_value!="Done":
        input_value=input().strip()
        items.append(input_value)
    obj_go_food.display_special_days()
    print("Special Day :- ",end=' ' )
    input_special_day=input().strip()
    obj_go_food.display_peak_hours()
    print("Peak Hours :- ",end=' ' )
    input_peak_hours=input().strip() 
    obj_go_food.display_night_charges()
    print("Night Charges :- ",end=' ')
    input_night_hours=input().strip()
    obj_go_food.display_normal_charges()
    print("Normal Charges :- ",end=' ')
    input_normal_charges=input().strip()
    return (items,input_special_day,input_peak_hours,input_night_hours,input_normal_charges)
if __name__=='__main__':
    obj_go_food=GoFood()
    input_items,input_special_day,input_peak_hours,input_night_hours,input_normal_charges=getInput(obj_go_food)
    obj_generate_bill=GenerateBill(input_items,input_special_day,input_peak_hours,input_night_hours,input_normal_charges)
    obj_generate_bill.final_bill()
