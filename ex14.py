from sys import argv
script,user_name = argv


print(f"Hi {user_name}. I am {script} script")
prompt = '>'

print("Do you like me?")
likes = input(prompt)

print("Which country do you live in ?")
lives = input(prompt)

print("which computer system do you use?")
computer=input(prompt)

print(f"""So you said {likes} to liking  me. 
You live in a country called {lives}
And you have a {computer} computer
""")