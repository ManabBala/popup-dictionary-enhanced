import requests


def wordMeaning(word):
    meaningContent = ""
    try:
        api_json = requests.get(
            f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()[0]

        for meaning in api_json['meanings']:
            print('loop')
            if meaningContent:
                meaningContent += "<hr>"
            meaningContent += "\n" + meaning['partOfSpeech'].capitalize() + ":"
            for definition in meaning['definitions']:
                # print('definition:', definition['definition'])
                meaningContent += "\n<br>=>" + definition['definition']
                # if definition['synonyms']:
                #     print('Similar: ', " ".join(definition['synonyms']))
                #     meaningContent += "\n" + " ".join(definition['synonyms'])
                # if definition['antonyms']:
                #     print('Opposite: ', "    ".join(definition['antonyms']))
                print()
            print()
        print(meaningContent)
    except Exception as e:
        print("Error while getting definition.")
        print(e)
    return meaningContent
