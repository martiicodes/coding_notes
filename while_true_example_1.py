def play_game(word_list):
    hand = "deal_hand(HAND_SIZE)"  # random init
    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = "deal_hand(HAND_SIZE)"
            play_hand = (hand.copy(), word_list)
            print()
        elif cmd == 'r':
            play_hand = (hand.copy(), word_list)
            print()
        elif cmd == 'e':
            break
        else:
            print("Invalid command.")