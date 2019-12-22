import re
def main():
    registred_words = ['begin', 'end', 'for', 'if', 'else', 'var', 'while', 'integer', 'double', 'do', 'boolean', 'then', 'true', 'false']
    file = open('text.txt', 'r')
    file2 = open('text2.txt', 'w')
    russian = re.compile("[а-яА-Я]+")
    for line in file:
        words = (re.findall(r"[\w]+", line))
        i = 0
        while i < len(words):
            word = words[i].strip()
            for registred_word in registred_words:
                if (word.lower() == registred_word.lower()):
                    line = line.replace(word, word.upper())
                # elif(russian.match(word)):
                #     line = line.replace(word, word)
                # else:
                #     line = line.replace(word, word.lower())

            i += 1

        file2.write(line)

if __name__ == '__main__':
    main()