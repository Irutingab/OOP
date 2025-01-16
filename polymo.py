class French:
    def Say_Hello(self):
        print("Bonjour")
        
class Chinese:
    def Say_Hello(self):
        
        print("你好")

def intro(lang):
    if hasattr(lang, 'Say_Hello'):#to check if the attribute lang has an attribute named hesay_hello
        lang.Say_Hello()
    else:
        print("The object does not have a Say_Hello method.")

#instances of French and Chinese
Raissa = French()
Lydie = Chinese()

#Call the intro function
intro(Raissa)
intro(Lydie)
