from random import *

# 총 탑승 승객 수 카운트 변수
cnt = 0 

for i in range(1, 51): # 1 ~ 50이라는 승객 번호
    time = randrange(5, 51) # 5분 ~ 50분 사이의 소요 시간 생성
    
    # 매칭 조건 확인: 5분 이상 15분 이하인 경우
    if 5 <= time <= 15:
        print(f"[O] {i}번째 승객 (소요시간 : {time}분)")
        cnt += 1 # 탑승 승객 수 증가
    else:
        print(f"[ ] {i}번째 승객 (소요시간 : {time}분)")

print(f"\n전체 탑승 승객 : {cnt} 명")