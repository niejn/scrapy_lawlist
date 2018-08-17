import re


def main():
    # /cms/cms/commons/downloadaffix.jsp?affix=/cn/rootfiles/2018/08/16/1533011447479860-1533011447613907.pdf
    # m = re.search("javascript:goToPage\('(.*?)'", value)
    value = "/cms/cms/commons/downloadaffix.jsp?" \
            "affix=/cn/rootfiles/2018/08/16/1533011447479860-1533011447613907.pdf"
    m = re.search(r"([\w/]*)", value)
    m = re.search(r"([\S]*)", value)
    # m = re.search(r"/cms/cms/commons/downloadaffix.jsp\?affix=([\S]*)", value)
    m = re.search(r"/cms/cms/commons/downloadaffix.jsp\?affix=(.*)", value)
    # m = re.search(r"(.*)", value)
    if m:
        # print(m.group(0))
        print(m.group(1))
    return


if __name__ == '__main__':
    main()