def SplitSentences(Text):
    import numpy as np
    if type(Text) == str:
        Text = Text.split('.')
    elif type(Text) == list:
        for index, value in enumerate(Text):
            Text[index] = value.split('.')
    elif type(Text) == np.ndarray:
        print("numpy array")
    return Text

def SplitWords(Text):
    import numpy as np
    if type(Text) == str:
        return Text.split(" ")
    if type(Text) == list:
        for index, value in enumerate(Text):
            Text[index] = value.split(' ')
        return Text
    if type(Text) == np.ndarray():
        return Text.split(" ")

def PurificationText(Text, sperator = [",",".","  "]):
    for element in sperator:
        if type(Text) == str:
            Text = Text.replace(element)
        if type(Text) == list:
            for index, value in enumerate(Text):
                Text[index] = value.replace(element)
    return Text
