def countVowelSubstrings(word):
    vowels = set('aeiou')
    c = 0
    n = len(word)
    for i in range(n):
        u = set()
        for j in range(i, n):
            if word[j] in vowels:
                u.add(word[j])
                if len(u) == 5:
                    c += 1
            else:
                break
    return c
print(countVowelSubstrings("aeiouu")) 
print(countVowelSubstrings("unicornarihan"))
