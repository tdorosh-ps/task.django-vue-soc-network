import random

init_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
            dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex 
            ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
            nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit 
            anim id est laborum."""


def gen_random_sentence(words_num, text=init_text):
    init_words_list = text.split(' ')
    final_words_list = [random.choice(init_words_list) for i in range(words_num)]
    final_words_list[0] = final_words_list[0].capitalize()
    return ' '.join(final_words_list) + '.'


def gen_random_post_body(sentences_num):
    post_body = ''
    for i in range(sentences_num):
        post_body += gen_random_sentence(random.randint(5, 10))
    return post_body
