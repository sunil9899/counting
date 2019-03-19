from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, "Home.html")


def interaction(request):
    return render(request, "interaction.html")


def output(request):
    data = request.GET['interaction']
    data_list = data.split()
    data_length = len(data_list)
    letters = []
    for e1 in data:
        letters.append(e1)
    characters = len(letters)
    word_dictionary = {}

    for words in data_list:
        if words in word_dictionary:
            word_dictionary[words] += 1
        else:
            word_dictionary[words] = 1
    sorted_word_dictionary = sorted(word_dictionary.items(), key= operator.itemgetter(1), reverse= True)

    return render(request, "output.html", {"para": data, "data_len":data_length, "letter_count":characters, "repeated_words":sorted_word_dictionary})


def abt(request):
    return render(request, "abt.html")
