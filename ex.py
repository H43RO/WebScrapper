class Car():

    def __init__(self, *args, **kwargs):
        print(kwargs) # dictionary
        self.wheels = 4
        self.doors = 4
        self.window = 4
        self.seats = 4

        # 입력받은 kwargs에서 값을 가져오고, 두번째에 기본 인자 입력
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    # Method - Class 안에 있는 function
    # 반드시 항상 1개 이상의 argument를 갖는데,
    # 이는 메소드를 호출한 인스턴스 자신을 가리킴

    # Overriding (인스턴스 생성 시에 자동 호출)
    def __str__(self):
        return f"Car with {self.wheels} wheels!"


# Extended Class
class Convertible(Car): 
    # 상속하여 메소드 재정의 시 대체됨
    def __init__(self, **kwargs):
        super().__init__(kwargs) # 부모의 init 호출
        self.time = kwargs.get("time", 10)
    def take_off(self):
        return "taking off"

    def __str__(self):
        return f"Car with no roof"

# 아래와 같이 속성을 커스텀할 수도 있다.
porche = Car(color="green", price="$40")
porche.color = "Red"
print(porche.color, porche.price)

# 클래스가 가진 모든 속성, 메소드를 출력함
print(dir(Car))

# 기본 인자가 들어감을 확인할 수 있음
mini = Car()
print(mini.color, mini.price)

ferrari = Convertible(color="yellow")
ferrari.take_off()
print(ferrari.wheels)
