# 클래스 생성
class Person:
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    # 1. 생성자 추가
    # def __init__(self):
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'AB'

    def __init__(self, name = '홍길동', height = 170, gender = 'male') -> None:
        self.name = name
        self.height = height
        self.gender = gender
        

    def walk(self):
        print(f'{self.name}이(가) 걷습니다.')

    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다!!')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다!!')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')

    # 2. 생성자외 매직메서드(펑션) __str__
    def __str__(self) -> str:
        return f'출력 : 이름은 {self.name}, 성별은 {self.gender}'


myunggun = Person('숭뮹군', 178, 'male') # 객체생성 instance
#myunggun.name = '숭뮹군'
#myunggun.height = '178'
#myunggun.gender = 'male'
#myunggun.blood_type = 'RH+ B'

print(f'{myunggun.name}의 혈액형은 {myunggun.blood_type}입니다.')

myunggun.run('Fast')
print(myunggun)

# 1. 초기화 후 객체생성
hong = Person()
hong.run('Slow')
print(hong)

print('====================')
# 2. 파라미터를 받는 생성자 실행
ashely = Person('애슐리', 165, 'female')
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely)
