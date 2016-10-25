from BeautifulSoup import BeautifulSoup

def match_class(target):
    target = target.split()
    def do_match(tag):
        try:
            classes = dict(tag.attrs)["class"]
        except KeyError:
            classes = ""
        classes = classes.split()
        return all(c in classes for c in target)
    return do_match

html = """<div class="feeditemcontent cxfeeditemcontent">
<div class="feeditembodyandfooter">
<div class="feeditembody">
<span>The actual data is some where here</span>
</div>
</div>
</div>"""


soup = BeautifulSoup(html)

matches = soup.findAll(match_class("feeditemcontent cxfeeditemcontent"))
for m in matches:
    print m
    print "-"*10

matches = soup.findAll(match_class("feeditembody"))
for m in matches:
    print m
    print "-"*10