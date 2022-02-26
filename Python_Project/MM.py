import itertools as its if __name__ == '__main__':     
words_num = "1234567890"     
words_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"     
r = its.product(words_num, repeat=8)     
dic = open("password-8Î»Êý×Ö.txt", "w")     
for i in r:         
dic.write("".join(i))         
dic.write("".join("\n"))    
dic.close()
