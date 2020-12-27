import requests as res
from bs4 import BeautifulSoup
import csv, os

page_names=[]
page_likes=[]


def Page_Names():
    with open('names.csv') as csv_file:
        csv_reader = csv.reader(csv_file ,delimiter=',')

        line_count = 0
        
        for row in csv_reader:

            if line_count == 0:
                line_count +=1
            else:
                page_names.append(row[0]) 

        return page_names

def Page_Likes(page_Names):

    for page_name in page_Names:
        source_code = res.get("https://www.facebook.com/"+page_name+"/likes")
        soup = BeautifulSoup(source_code.content,"html.parser")
        likes = soup.select_one("div._3xom").text
        page_likes.append(likes)
       
    return page_likes

def Write_Info(page_Names, page_Likes):

    with open('names_with_likes.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(["Pages","Likes"])
        for page in range(len(page_Names)):
            csv_writer.writerow([(page_Names[page]),(page_Likes[page])])
                                

def main():
    print("Loading./n",)

    names = Page_Names()
    likes= Page_Likes(names)
    Write_Info(names, likes)




if __name__ == "__main__":
        main()