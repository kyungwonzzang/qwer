def go():
    print("간다")

def stop():
    print("안간다")

# 만약 my 가 1이면 간다 2면 안간다.
my = 1

# 여기를 잘라낸다
def gogo():
    if my == 1:
        go()
    else:
        stop()

# 돈을 넣으면 2배가 뻥튀기
# m = 1000
def coin(m):
    return m * 2
    print("내 돈은 {0}".format(m))

# mym = coin(1000)
# print("내 돈은 {0}".format(mym)).

def ck_idpw(id, pw):
    if id == 'a' and pw == '123':
        return '로그인 성공'
    else:
        return '로그인 실패'