import requests, docx
from bs4 import BeautifulSoup

BASE_URL = "https://www.edufix.cz"
LINKS_URL = "https://www.edufix.cz/clanky/maturita/cestina"
LINKS_PATH = "/clanky/maturita/cestina"

ARTICLE_CONTAINER_ID = 'Article-Content'
ARTICLE_EXCLUDE_CLASS = 'articleContent articleContent-courseView'
LINKS_CONTAINER_ID = 'Article-Content'
IS_VALID_LINK = "Rozbor"

def is_valid_link(link):
    return link.find(IS_VALID_LINK) != -1

def extract_text_from_url(url):
    response = requests.get(url)
    html_content = response.text
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    container = soup.find(id=ARTICLE_CONTAINER_ID)

    if container:
        elements_to_exclude = container.find_all(class_=ARTICLE_EXCLUDE_CLASS)
        for element_to_exclude in elements_to_exclude:
            element_to_exclude.decompose()
            
        extracted_text = container.get_text(strip=True)
        return extracted_text
    else:
        return None
    
def extract_links(filters=[]):
    response = requests.get(LINKS_URL)
    html_content = response.text
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    container = soup.find(id=LINKS_CONTAINER_ID)

    links = []
    if container:
        anchor_tags = container.find_all('a')
        for anchor_tag in anchor_tags:
            link = anchor_tag.get('href')
            if link and link.startswith(LINKS_PATH):
                inner_text = anchor_tag.get_text(strip=True)

                if is_valid_link(inner_text):
                    if len(filters) == 0:
                        links.append(BASE_URL + link)
                    else:
                        for filter in filters:
                            if inner_text.lower().find(filter.lower()) != -1:
                                links.append(BASE_URL + link)
                                break

    return links

def format_docx(doc=None, path=None):
    if path:
        doc = docx.Document(path)
    elif not doc:
        return
    
    newdoc = docx.Document()

    for paragraph in doc.paragraphs:
        for line in paragraph.text.split("\n"):
            if line.strip().startswith("-"):
                print("starts with -")
                newdoc.add_paragraph("\t\t" + line.strip())
            elif line.strip().startswith("o "):
                newdoc.add_paragraph("\t\t\t" + line.strip())
            else:
                newdoc.add_paragraph(line.strip())

    for p in newdoc.paragraphs:
        print(p.text)

    return newdoc