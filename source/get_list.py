
def this_list():
    with open('comment_list.txt', 'r') as file:
        comment_list = file.read().split('\n')
        print(comment_list)
        comment_list = filter(None, comment_list)
        print(list(comment_list))
    return comment_list

this_list_raw = this_list()