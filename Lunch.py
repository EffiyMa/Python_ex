

class Food(object):    #菜单
        def __init__(self):
                pass              
        def MenuDict(self):
                x={'crepe':10, 'pudding':5,"cake":15,"juice":20,"tart":3 }
                return x

class Employee(Food):

        def TurnMenu(self):
                x=super(Employee,self).MenuDict()
                self.fdmenu=x
                return self.fdmenu
                
        def takeOrder(self):#下单
                self.order={}
                self.bill=0
                print("\n这是您要的菜单-价格：")
                print( self.TurnMenu() )
                print("\n开始下单,输入#时退出点单")
                while True:
                        print("选择的食物：")
                        fd=input()
                        if fd=="#":
                                break
                        if fd not in self.fdmenu.keys():
                                print("Sorry,No Such Food")
                                continue
                        print("食物的份数：")
                        num=eval( input() )
                        self.order[fd]=num
                        self.bill+=self.fdmenu.get(fd)*num
                                              
        def GetOrder(self):
                return self.order

        def GetBill(self):
                return self.bill
                            
        
class Customer(Employee):
        def __init__(self,tele,nm):
                self.tel=tele#顾客电话
                self.name=nm #顾客姓名
                self.FoodOder={}
                self.pay=0
        def placeOrder(self):
                super(Customer,self).takeOrder()#向waiter点单
                self.FoodOder=super(Customer,self).GetOrder()
                self.pay=super(Customer,self).GetBill()
        def PrintOrder(self):
                print("====OrderInfo==")
                print("电话",self.tel)
                print("姓名",self.name)
                print("订单",self.FoodOder)
                print("金额",self.pay)
                print("================\n See you next time!")


class Lunch(Customer):
        def __init__(self,telephone,nme):
                super(Lunch,self).__init__(telephone,nme)#Customer的init
        def order(self):
                super(Lunch,self).placeOrder()
        def result(self):
                super(Lunch,self).PrintOrder()
                

if __name__=='__main__':
        #欢迎界面
        print("*"*53)
        print("*"," "*49,"*")
        print("*"," "*49,"*")
        print("*",' '*12,"WElCOME TO ORDER SYSTEM",' '*12, "*")
        print("*"," "*49,"*")
        print("*"," "*49,"*")
        print("*"*53,'\n')

        #注册人信息
        print("=======Please Log in First====== \n","Your Tel: ",end='')
        t=eval( input() )
        print("Your Name:",end='')
        n= input()
        print("================================")

        #下订单
        print("\n")
        lnh=Lunch(t,n)
        lnh.order()
        lnh.result()
                
                
                
                
