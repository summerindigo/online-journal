name = '홍길동'
age = '30'

hello = f'제 이름은 {name}입니다. 나이는 {age}입니다'
print(hello)

from datetime import datetime

today = datetime.now()
mytime = today.strftime('%Y-%m-%d-%H-%M-%S')

filename = f'file-{mytime}'

print(mytime)