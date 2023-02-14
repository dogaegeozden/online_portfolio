# ONLINE PORTFOLIO

![OnlinePortfolio](https://raw.githubusercontent.com/dogaegeozden/online_portfolio/master/github_images/web_page_main_pic.png)

This is the source code my online portfolio production state. I wrote this web application using Python, Django, HTML, CSS, JavaScript and, MySQL. It's allowing me to keep a blog, display my projects, accomplishments, certificates and talents. You can see it's deployed version online at https://www.dogaegeozden.com. It's deployed from a VPS on Linode. I used Gunicorn as my WSGI. I created a service called gunicorn which simply starts gunicorn with the configuration that I define in a custom configuration file. And, I used NGINX as a reverse proxy server and as a load balancer. It's a better option than APACHE. I generated my own SSL certification with Let's Encrypt certbot and used cron jobs to automate the certification renewal job.
