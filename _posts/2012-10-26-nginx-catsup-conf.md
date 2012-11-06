#Nginx纯静态化配置 on catsup
- tags: nginx,  urlrewrite, catsup

----
####当前配置:
```xml
server {
    listen 80;
    server_name  plumj.com;
    root /usr/local/catsup/deploy;
    error_page 404 = http://plumj.com/404.html;
	
    add_header     Nginx-Cache     "HIT from plumj.com";
    add_header     Vary            Accept-Encoding;

    if ($host != 'plumj.com') {
        rewrite ^/(.*)$ http://plumj.com/$1 permanent;
    }

    location ~^/static/ {
            expires 2d;
    }
}
```

