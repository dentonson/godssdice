import random

words = { #대체할 문자 
    "신도": ["하나님도", "부처도", "준성쌤도", "주님도"],
    "주사위": ["윷", "홀짝", "롤체", "롤"],
    "놀이를": ["놀이를 하며", "놀며", "놀이를 즐기며", "즐겁게"]
}

sentence = "신도 주사위 놀이를 한다."
obfuscated_sentence = "" #obfuscated = 애매한, 혼란스러운

for word in sentence.split(): #문장 배치
    if word in words:
        replacement = random.choice(words[word])
        obfuscated_sentence += replacement
    else:
        obfuscated_sentence += word
    obfuscated_sentence += " "

print(obfuscated_sentence)

