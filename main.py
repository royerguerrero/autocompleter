def autocompete(text, prefix):
    autocompete_words = {}
    for word in text:
        try:
            autocompete_words[word]
            autocompete_words[word] += 1
        except KeyError:
            if len(word) >= len(prefix) and prefix[0] == word[0]:
                counter = 0
                for i in range(len(prefix)):
                    if i <= len(word):
                        if prefix[i] == word[i]:
                            counter += 1

                if counter == len(prefix):
                    autocompete_words[word] = 1

    return autocompete_words


if __name__ == "__main__":
    print("""   
    ___         __                                   __     __           
   /   | __  __/ /_____  _________  ____ ___  ____  / /__  / /____  _____
  / /| |/ / / / __/ __ \/ ___/ __ \/ __ `__ \/ __ \/ / _ \/ __/ _ \/ ___/
 / ___ / /_/ / /_/ /_/ / /__/ /_/ / / / / / / /_/ / /  __/ /_/  __/ /    
/_/  |_\__,_/\__/\____/\___/\____/_/ /_/ /_/ .___/_/\___/\__/\___/_/     
                                          /_/                            
                by R0Y3R @RoyerGuerreroP in Twitter
    """)
    text_file = input(
        'What is the name of the file with the text to be analyzed? ')
    prefix = input('What is the prefix? ')

    with open(text_file) as f:
        words = [word for line in f for word in line.split()]

    result = autocompete(words, prefix)
    print(result)
