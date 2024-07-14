def finder(str1, word):
    x = str1.lower()
    ans = x.count(word)
    print(ans)

finder("Welcome to USA. usa awesome, isn't it?", "usa")