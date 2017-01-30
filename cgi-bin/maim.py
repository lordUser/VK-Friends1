# -*- coding: UTF-8 -*-
import os
import http.cookies
import urllib2, json, sys
import cgi
import html

form = cgi.FieldStorage()
cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")

def get_friends(uid):
    url  = u'https://api.vk.com/method/friends.get?fields=connections&uid=%s&access_token=token' %(uid)
    res  = urllib2.urlopen(url).read()
    data = json.loads( res )
    if 'error' in data :
        print data
        data = list()
    return data[u'response']

def get_info():
    user1 = []
    for user in [i for i in friends_id]:
        user1.append(user)
    return user1

def max_user():
        for user in friends[0:5]:
            print"<li><a href='https://vk.com/id%s'>%s %s</a></li>" % (user[u'user_id'], user[u'first_name'].encode("utf-8"), user[u'last_name'].encode("utf-8"))
def name_is_none():
    print "Set-cookie: name=value; expires=Wed May 18 03:33:20 2033; path=/cgi-bin/; httponly"
    print "Content-type: text/html\n"
    print """<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>title</title>
            <script src="https://vk.com/js/api/openapi.js?139" type="text/javascript"></script>
        </head>
        <body>"""
    print "<script type='text/javascript'>"
    print"VK.init({apiId: 5849778})"
    print "</script>"
    print "<div id='vk_auth'></div>"
    print "<script type='text/javascript'>"
    print "VK.Widgets.Auth('vk_auth', {});"
    print "</script>"
    print "</body></html>"

def name_is():
    uid = form.getfirst("uid", "не задано")

    friends_id = get_friends(uid)
    friends  = get_info()
    uid = html.escape(uid)
    print "Content-type: text/html\n"
    print """<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Обработка данных форм</title>
            </head>
            <body>"""

    print "<h1>Здравствуйте, {} {}!</h1>".format(form.getfirst("first_name", "не задано"), form.getfirst("last_name", "не задано"))
    print "<div>"
    print "<p>ваши друзья соскучились за вами:</p>"
    print "<div>"
    print "<ul>"
    print "{}".format(max_user())
    print "</ul>"
    print "</div>"
    print "<p>скорее свяжитесь с ними</p>"
    print "</div>"
    print "</body></html>"

if name is None:
    name_is_none()




else:
    name_is_none()
