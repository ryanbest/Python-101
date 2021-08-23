def count_letter(sen,letter):
    sen=" "+sen
    print sen
    letter=" "+letter
    print letter
    removed_letter_sen=sen.replace(letter," ")
    print removed_letter_sen
    print "Number of Words that starts with %s:%d"%("s",len(sen)-len(removed_letter_sen))


def decipher():
    sentence=raw_input("Please enter a sentence ==> ")
    print sentence
    sentence=sentence.replace("rxr","a")
    sentence=sentence.replace("bb","he")
    sentence=sentence.replace("he","an")
    sentence=sentence.replace("xx","th")
    sentence=sentence.replace("az az","e")
    sentence=sentence.replace("yyy","u")
    sentence=sentence.replace("twt","o")
    print "Deciphered as==> %s"%sentence
    count_letter(sentence,"s")
    count_letter(sentence,"a")
    count_letter(sentence,"c")
    
decipher()
    
    
    