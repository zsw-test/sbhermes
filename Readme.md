mysql
docker run -d -p 3306:3306 --privileged=true -v /usr/local/mysql/log:/var/log/mysql -v /usr/local/mysql/data:/var/lib/mysql -v /usr/local/mysql/conf:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=123456 --name mysql mysql:5.7

1、pip install -r requirements.txt
2、docker-compose up