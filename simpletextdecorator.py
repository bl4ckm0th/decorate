x = (input("Write something! \n"))
def decor(func):
      def wrap(text):
          print("\n"+"=*"*(len(text)//2))
          func(text)
          print("=*"*(len(text)//2)+"\n")
      return wrap

def print_text(text):
      print(text)

print_text = decor(print_text)
print_text(x)
y = (input("Wanna write again?(y/n)"))
while True:
    if y == "y":
       x = (input("Write something! \n"))
       print_text(x)
       y = (input("Wanna write again?(y/n))
    elif y == "n":
     break
    else:
     print("Only type \"y\" or \"n\"!")
     y = (input("Wanna write again?(y/n)"))
