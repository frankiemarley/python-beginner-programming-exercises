# ✅↓ Write your code here ↓✅

def sing():
    lyrics = ""
    for i in range(10):  
        if i == 4:
            lyrics += "there will be an answer,\n"
        if i == 9:
            lyrics += "whisper words of wisdom, let it be"
        else:
            lyrics += "let it be,\n"  
    return lyrics
print(sing())

