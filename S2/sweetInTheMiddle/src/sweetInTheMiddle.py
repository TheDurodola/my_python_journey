def alpha(user_input, word_to_be_added):
    word_count = len(user_input)
    if word_count % 2 == 1:
        return user_input+ word_to_be_added

    if word_count % 2 == 0:
        first_half = user_input[:word_count // 2]
        second_half = user_input[word_count // 2:]
        return first_half + word_to_be_added + second_half

    return None


