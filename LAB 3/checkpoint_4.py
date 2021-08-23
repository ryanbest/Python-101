def space_adjust(max_length,name):
    space_diff=max_length-len(name)
    space_r=space_diff/2+1
    space_l=space_diff/2+space_diff%2+1
    return "*"*2+" "*(space_r)+name+" "*(space_l)+"*"*2

def framed_greeting():
    first_name=raw_input("Please enter your first name:")
    last_name=raw_input("Please enter your last name:")+"!"
    
    welcome_phase="Hello,"
    
    max_word_lens=max(len(first_name),len(last_name),len(welcome_phase))
    
    welcome_phase=space_adjust(max_word_lens,welcome_phase)
    first_name=space_adjust(max_word_lens,first_name)
    last_name=space_adjust(max_word_lens,last_name)
    
    max_word_lens+=6
    
    print "*"*max_word_lens
    print welcome_phase
    print first_name
    print last_name
    print "*"*max_word_lens
    
    
framed_greeting()