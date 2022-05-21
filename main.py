import pyfiglet
import os
import random
import time

def money_happiness (money, happiness):
  print("\nMoney:", money)
  print("Happiness:", happiness)

ascii_banner = pyfiglet.figlet_format("Life Happens! \n")
clear = lambda: os.system('clear')
print(ascii_banner)
money = int(100)
happiness = int(100)
name = input("Welcome to Life Happens! What is your name? ")
print("\nHi", name + "!", "In this choose your own adventure game, you will be given a variety of scenarios and 3 options. Each option has its pros and cons and your goal is to balance money and happiness without running out of either!\n")
input("Ready? (Type anything and press enter): ")
print("\nGenerating...")
time.sleep(3)
clear()
print("Let's build your profile! Who are you? Pick from one of the 3 people: \n\n1) You currently live in a nice house, you have a wife and you work at Google as a software engineer. It pays well but you are not satisfied with your current lifestyle and want to move up the ranks at work. Will you choose family or work? 150 money, 50 happiness. \n\n2) You work as an electrician for Enbridge, you have a wife and live in a small house. It pays enough and you are satisfied with your current life. Can you manage the problems that come your way? 100 money, 100 happiness\n\n3) You are a young aspiring social media star that lives with their parents. You work at McDonald's and do not get paid much but you are very excited about pursuing your dream! Will it pay off? 50 money, 150 happiness")
profile = input()
if (profile == "1"):
  money = 150
  happiness = 50
  input("\nYou have chosen #1! Good luck! Type anything to get started!")
  money_happiness(money, happiness)
  
elif (profile == "2"):
  money = 100
  happiness = 100
  input("\nYou have chosen #2! Good luck! Type anything to get started!")
  money_happiness(money, happiness)
else:
  money = 50
  happiness = 150
  input("\nYou have chosen #3! Good luck! Type anything to get started!")
  money_happiness(money, happiness)