def rot(arr):
    for i in range(len(arr)-1):
        temp = arr.pop(0)  # 첫 번째 요소를 추출하여 temp에 저장
        arr.append(temp)  # 추출한 요소를 배열의 끝에 추가
        print(*arr) #바뀐 배열들을 출력

a = int(input())
arr = list(map(int, input().split()))

print(*arr)
rot(arr)  #배열 회전
