#coding=utf-8
import os
site_title = 'plum.J'
site_description = '\'s blog'
#site_url = 'https://github.com/whtsky/catsup'
site_url = 'http://plumj.com'
static_url = 'static'
theme_name = 'sealscript'
google_analytics = ''  # optional

catsup_path = os.path.dirname(__file__)
posts_path = os.path.join(catsup_path, '_posts')
theme_path = os.path.join(catsup_path, 'themes', theme_name)
common_template_path = os.path.join(catsup_path, 'template')
deploy_path = os.path.join(catsup_path, 'deploy')

twitter = '_plumJ'
weibo = 'dobbyfree'
github = 'plumJ'
disqus_shortname = 'catsup'

feed = 'feed.xml'
post_per_page = 3

links = (
    ('whtsky', 'http://whouz.com', 'whouz write catsup'),
    ('catsup', 'https://github.com/whtsky/catsup', 'the source of this blog'),
)

if site_url.endswith('/'):
    site_url = site_url[:-1]
if static_url.endswith('/'):
    static_url = static_url[:-1]

settings = dict(static_path=os.path.join(theme_path, 'static'),
    template_path=os.path.join(theme_path, 'template'),
    gzip=True,
    site_title=site_title,
    site_description=site_description,
    site_url=site_url,
    twitter=twitter,
    weibo=weibo,
    github=github,
    feed=feed,
    post_per_page=post_per_page,
    disqus_shortname=disqus_shortname,
    links=links,
    static_url=static_url,
    google_analytics=google_analytics,
)
