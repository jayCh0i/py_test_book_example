n = input()

arr = []
# keyword = ''
result = 1000

# 키워드가 문자열의 절반 길이보다 길 경우 압축의 의미가 없다
for key_len in range(1, len(n)//2 +1):
    # 
    compressed_word = ''
    # 처음 들어갈 키워드 설정
    keyword = n[0:key_len]
    count = 1

    # 처음 키워드 다음부터 반복 시작
    for i in range(key_len, len(n), key_len):
        # 아래 Array slicing에서 오버플로우가 안나는 이유
        ## Array slicing 사용할때 step이 양수인 경우 start나 end가 배열 길이를 넘어도 값은 len(array)로 처리되어 동작한다
        next_keyword = n[i:i+key_len]

        if keyword == next_keyword:
            count += 1
        else:
            compressed_word += str(count) + keyword if count > 1 else keyword
            keyword = next_keyword
            count = 1

    # 남은 문자열까지 더해서 완성
    compressed_word += str(count) + keyword if count > 1 else keyword

    # 더 적은 값을 선택해서 저장 
    result = min(result, len(compressed_word))

# 결과 출력
print(result)