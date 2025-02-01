input_strs  = ['eat','tea', 'tan','ate','nat','bat']
def group_anagrams(strs):
    anagrm_dict = {}

    for word in strs:
        sorted_word = ''.join(sorted(word))

        if sorted_word in anagrm_dict:
            anagrm_dict[sorted_word].append(word)
        
        else:
            anagrm_dict[sorted_word]=[word]

    return list(anagrm_dict.values())

output_anagrms = group_anagrams(input_strs)
print(output_anagrms)