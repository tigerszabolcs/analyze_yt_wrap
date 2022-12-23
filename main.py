from bs4 import BeautifulSoup


def write(file, string):
    with open(file, 'w') as filewriter:
        filewriter.write(string)

def read(file):
    with open(file, 'r') as html_file:
        txt = html_file.read()
    return txt

if __name__ == '__main__':

    path = "data.html"
    txt = read(path)
    soup = BeautifulSoup(txt, 'lxml')
    # x = soup.prettify()
    # print(x)
    # write('output.html', x)
    list = soup.findAll('a')
    # print(f"video: {list[0]}\n channel: {list[1]} \n what: {list[2]}")
    i = 1
    n = 0
    dict = {}
    for element in list:
        if i==1:
            print("Video:")
        elif i==2:
            print("Channel:")
        elif i==3:
            print("Take Out This: ")
            n+=1
            i=0
        print(f"{i}: {element} \n")
        for key in dict:
            if element.txt == key:
                dict[key] = dict[key]+1
            else:
                pass
        i+=1
    print(n)
    print(dict)
