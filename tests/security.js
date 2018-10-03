mport requests
import scrapy

for i in range(200):
    print(i)
    response = requests.get(f'https://autopapa.ge/ge/search?&s%5Bcountry_id%5D=2&s%5Bengine_type%5D%5B%5D=0&s%5Bgearbox%5D%5B%5D=0&s%5Blegal_status%5D%5B%5D=&s%5Brudder%5D%5B%5D=&order=date&page={i}&short_form=0&utf8=%E2%9C%93')
    html_tree = scrapy.selector(response)
    page_links = html_tree.xpath("""/html/head/link[6]/@href""").exttract()
    print(page_links)
    for link in page_links:
        response = requests.get(link)
        html_tree = scrapy.selector(response)