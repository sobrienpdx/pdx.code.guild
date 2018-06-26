#code_from_others.py

selection=''
while selection.lower() != 'palindrome' and selection.lower() != 'anagram':
    selection = input('Would you like to use the palindrome or anagram checker?  ')
if selection.lower() == 'palindrome':
    word_list = []
    r_word_list = []
    word = input('What word would you like to check?  ')
    for i in word.lower():
        word_list.append(i)
        print(word_list)
        r_word_list.append(i)
    r_word_list.reverse()
    if r_word_list == word_list:
        print(word + ' is a palindrome!')
    else:
        print(word + ' is not a palindrome!')


if selection.lower() == 'anagram':
    word1 = input('What is the first word?  ')
    word2 = input('What is the word you want to check it against?  ')
    if sorted(word1.replace(' ','').lower()) == sorted(word2.replace(' ','').lower()):
        print('The words are anagrams!')
    else:
        print('The words are not anagrams!')


Add CommentCollapse 
phone[0:3]



#[start:stop:skip]
