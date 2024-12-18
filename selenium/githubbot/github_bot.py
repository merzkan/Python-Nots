import gitfollowers 

name = input("Kullanıcı adını giriniz:")

print("Takipçiler aranıyor...")
github = gitfollowers.Github(name)

github.signIn()
github.getFollowers()

print(f"florisboard kullanıcısını:{len(github.followers)} takipçisi var.\n")
print("*************************Takipçi listesi*************************************")

github.followers.sort(key=str.lower)

for follower in github.followers:
    print(follower)
print("*************************Takipçi listesi*************************************")
print(f"florisboard kullanıcısını:{len(github.followers)} takipçisi var.\n")

github.textFile()

github.close()

input("Program tamamlandı. Çıkmak için bir tuşa basın...")
