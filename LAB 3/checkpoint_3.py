def framed():
    string=raw_input("Enter a word:")
    string_lens=len(string)
    print "*"*string_lens+"*"*6
    print "*"*2,string,"*"*2
    print "*"*string_lens+"*"*6
    
framed()