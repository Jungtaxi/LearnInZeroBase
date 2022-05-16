import random
def quick_sort(array,start,end):
    if start >= end :                                     # 원소가 1개일 경우 종료
        return
    pivot = start                                         # pivot은 첫번째 요소
    left = start + 1                                      # left는 pivot 다음 요소부터 시작
    right = end                                           # right 끝에서 반대방향으로 시작
    while (left <= right):                                # left와 right가 엇갈리면 종료
        while ((left <= end) and (array[left] <= array[pivot])): # pivot vlaue 보다 큰 left를 발견하기 전까지 left 증가
            left += 1
        while ((right>start) and (array[right]>= array[pivot])): # pivot value 보다 작은 right 발견하기 전까지 right 감소 
            right -= 1
        if left > right:                                          # left와 right가 엇깔리면 right 자리에 pivot을 넣는다.
            array[right],array[pivot] = array[pivot],array[right] # right과 left가 엇깔린 상태이기 때문에, right 자리에 pivot보다 작은 값이 있을거기 때문
        else :
            array[left],array[right] = array[right],array[left] # pivot 보다 큰 요소가 right에 있고, 작은 요소가 left에 있다면, 위치를 스위치 한다.
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)
mylist = [random.choice(range(1,101)) for _ in range(20) ]
quick_sort(mylist,0,len(mylist)-1)
print(mylist)