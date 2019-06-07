import requests
# import lxml
from extensions import text_processor
from .clean_html import clean_html
from bs4 import BeautifulSoup


class Scrape:

    def __init__(self, seed='url'):

        self.url = seed

    def page_scrape(self):
        links = {self.url}
        s = requests.Session()
        s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        r = s.get(self.url)
        data = r.content
        soup = BeautifulSoup(data, "lxml")
        for link in soup.find_all("a"):
            link_data = link.get("href")
            if link_data is None:
                pass
            elif link_data[:5] == "https":
                row = link_data + "/"
                links.add(row)
            elif link_data[:4] == "http":
                row = link_data + "/"
                links.add(row)
            else:
                pass
        return r.text, links

    def parse_scrape(self, text):
        clean = clean_html(text).lower()
        clean = clean.replace('\n', '')
        clean = clean.replace('\\n', '')
        clean = clean.replace('\r', '')
        clean = clean.replace('\\r', '')
        clean = clean.replace('\t', '')
        clean = clean.replace('\\t', '')

        strip_clean = clean.split('   ')
        clean = [i for i in strip_clean if len(i) > 0]
        clean = ' '.join(clean)
        strip_clean = clean.split('  ')
        clean = [i for i in strip_clean if len(i) > 0]
        clean = ' '.join(clean)

        text_process.load_sequence(clean)
        text_process.tokenize()
        t = [text_process.extract_tokens_pos()]
        return t

    def crawl(self, path_to_dict, path_to_model):
        result = self.page_scrape()
        bow = [self.parse_scrape(result[0])]
        links = {self.url}
        for i in sorted(result[1]):
            if i != self.url:
                self.url = i
                new_result = self.page_scrape()
                bow.append(self.parse_scrape(new_result[0]))
                for j in sorted(new_result[1]):
                    if j in links:
                        pass
                    else:
                        links.add(j)
            else:
                pass
        dictionary, corpus = text_process.custom_corpora(bow, path_to_dict, path_to_model)
        return dictionary, corpus, sorted(links)

    def parse_topics(self, text):
        clean = clean_html(text).lower()
        clean = clean.replace('\n', '')
        clean = clean.replace('\\n', '')
        clean = clean.replace('\r', '')
        clean = clean.replace('\\r', '')
        clean = clean.replace('\t', '')
        clean = clean.replace('\\t', '')

        strip_clean = clean.split('   ')
        clean = [i for i in strip_clean if len(i) > 0]
        clean = ' '.join(clean)
        strip_clean = clean.split('  ')
        clean = [i for i in strip_clean if len(i) > 0]
        clean = ' '.join(clean)

        text_process.load_sequence(clean)
        text_process.tokenize()
        t = text_process.rank_words_phrases()
        return t

    def topic_crawl(self):
        result = self.page_scrape()
        bow = [self.parse_topics(result[0])]
        links = {self.url}
        for i in sorted(result[1]):
            if i != self.url:
                self.url = i
                new_result = self.page_scrape()
                bow.append(self.parse_topics(new_result[0]))
                for j in sorted(new_result[1]):
                    if j in links:
                        pass
                    else:
                        links.add(j)
            else:
                pass
        return bow, sorted(links)
