#pseudo code

#creating a main function
def main():
    msg = input()
    #this is the input for anything
    outcome = convert(msg)
    #create an outcome variable and apply to convert function. Why I write msg? It is because I want the msg input to pass through the convert.
    #if convert(), then what it is converting?
    print(outcome)

#the msg within the convert is another varaible that is not linked to the main().
def convert(msgs):
    msgs1 = msgs.replace (":)", "🙂")
    #in creating this variable msgs1 is just another varaible to call it. take the variable from convert(msgs). Because the msgs entering the function will flow into msgs1.
    #Use the replace function
    msgs2 = msgs1.replace(":(", "🙁")
    #Okay so initially I though that I needed to use the if,elif and else function.
    #But because it is just replacing the text then there is no need to. Replace function does not affect the str.
    #so by continuing the msgs1 as a variable. Just repeat the step by creating a msgs2 to repace the sad face.
    return msgs2
    #Why return msgs2?
    #It is because msgs2 is the latest variable.
main()

#Limitation
#if i type :)) or :(( then the code break. I want to find out why? Because it is using the replace method and only :) should be affected. Why does :)) being read?cd ..

