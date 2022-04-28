# lose = 0
# p_2 = "パー"

# while True:
#   if p_2 == "グー":
#     p_2 = "チョキ"
#   elif p_2 == "チョキ":
#     p_2 = "パー"
#   else:
#     p_2 = "グー"
  
#   while True:
#     p_1 = str(input())
#     if any((p_1 == "グー", p_1 == "チョキ", p_1 == "パー")):
#       break
#     else:
#       print("再入力してください")
  
#   print("あなたの出した手: {}、相手の出した手: {}".format(p_1,p_2))

#   if p_1 == "グー":
#     if p_2 == "グー":
#       print("あいこ")
#     elif p_2 == "チョキ":
#       print("あなたは勝ちました")
#       break
#     else:
#       lose += 1
#       if lose == 3:
#         print("あなたは負けました")
#         break
#       else:
#         print("あなたの負け、再チャレンジ")
#   elif p_1 == "チョキ":
#     if p_2 == "グー":
#       lose += 1
#       if lose == 3:
#         print("あなたは負けました")
#         break
#       else:
#         print("あなたの負け、再チャレンジ")
#     elif p_2 == "チョキ":
#       print("あいこ")
#     else:
#       print("あなたは勝ちました")
#       break
#   else:
#     if p_2 == "グー":
#       print("あなたは勝ちました")
#       break
#     elif p_2 == "チョキ":
#       lose += 1
#       if lose == 3:
#         print("あなたは負けました")
#         break
#       else:
#         print("あなたの負け、再チャレンジ")
#     else:
#       print("あいこ")
  

lose = 0

def enemy_hands():
  while True:
    yield 1
    yield 2
    yield 3

def janken_win(my_hand, e_hand):
  if my_hand == 1 and e_hand == 2:
    return True
  elif my_hand == 2 and e_hand == 3:
    return True
  elif my_hand == 3 and e_hand == 1:
    return True
  else:
    return False

janken = { 1: "グー", 2: "チョキ", 3: "パー" }
enemy_hand = enemy_hands()

while True:
  my_hand = int(input("何をだしますか？ 1: グー, 2: チョキ, 3: パー"))

  if my_hand not in (1, 2, 3):
    print("再入力してください")
    continue

  e_hands = next(enemy_hand)
  print("あなたの出した手: {}、相手の出した手: {}".format(janken.get(my_hand),janken.get(e_hands)))

  if my_hand == e_hands:
    print("あいこ")
  else:
    if janken_win(my_hand,e_hands):
      print("あなたの勝ちです")
      break
    else:
      lose += 1
      if lose == 3:
        print("あなたの負けです")
        break
      else:
        print("あなたの負け、再チャレンジ")
        
      

