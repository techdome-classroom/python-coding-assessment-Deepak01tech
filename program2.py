def decode_message(message: str, pattern: str) -> bool:
    pattern_len, message_len = len(pattern), len(message)


    dp_table = [[False] * (message_len + 1) for _ in range(pattern_len + 1)]
    dp_table[0][0] = True


    for i in range(1, pattern_len + 1):
        if pattern[i - 1] == '*':
            dp_table[i][0] = dp_table[i - 1][0]


    for i in range(1, pattern_len + 1):
        for j in range(1, message_len + 1):
            if pattern[i - 1] == '*':

                dp_table[i][j] = dp_table[i - 1][j] or dp_table[i][j - 1]
            elif pattern[i - 1] == '?':

                dp_table[i][j] = dp_table[i - 1][j - 1]
            else:

                dp_table[i][j] = pattern[i - 1] == message[j - 1] and dp_table[i - 1][j - 1]


    return dp_table[pattern_len][message_len]


