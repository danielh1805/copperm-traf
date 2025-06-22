import requests
import xml.etree.ElementTree as ET

def get_links_from_sitemap(url):
    resp = requests.get(url)
    root = ET.fromstring(resp.content)
    ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    return [elem.text for elem in root.findall('.//sm:loc', ns)]

if __name__ == '__main__':
    links = get_links_from_sitemap('https://copperm.com/sitemap.xml')
    with open('links.json', 'w', encoding='utf-8') as f:
        import json
        json.dump(links, f, ensure_ascii=False, indent=2)
