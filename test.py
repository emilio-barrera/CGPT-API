from gpt_api import gpt_api

if __name__ == '__main__':
    api = gpt_api()

    prompt = (input('Ask ChatGPT: '))
    print('\nPlease wait while the little men figure out your non-sense...\n')
    print(api.ask_gpt(prompt))