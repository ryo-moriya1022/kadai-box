
class Car:
    def __init__(self):
        self.fuel =0
    def run(self):
        if self.fuel>0:
            self.fuel=self.fuel-1
            print("燃料を1消費して走りました")
        else:
            print("燃料がないため走れません")
class GasStation:
    def refuel(self,car): 
        car.fuel=car.fuel+20
        print("給油したことによりfuelが20増えました")
class Bus(Car):
    def __init__(self, max_p):
        super().__init__()  # 親クラスの__init__メソッドを呼び出す
        self.max_passenger = max_p
        self.passenger = 0

    def run(self):
        if self.fuel > 0:
            self.fuel -= 1
            print("燃料を1消費して走りました")
        else:
            print("燃料がないため走れません")

    def load(self, human):
        maxs = ""
        word = ""
        self.now_passenger = self.passenger + human
        if human < 0:
            if self.now_passenger < 0:
                human = self.passenger
                self.passenger = 0
                word = "すべて"
            print("{}人{}の乗客をおろしました 現在の乗客人数{}".format(-human, word, self.passenger))
        elif human >= 0:
            if self.now_passenger > self.max_passenger:
                human = self.max_passenger - self.passenger
                self.passenger = self.max_passenger
                maxs = "定員オーバー"
            print("{}{}人の乗客を乗せました。現在の乗客人数{}".format(maxs, human, self.passenger))

bus = Bus(50)
gasstation = GasStation()
bus.run()
