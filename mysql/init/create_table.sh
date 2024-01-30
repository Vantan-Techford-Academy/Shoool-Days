#!/bin/sh

# MySQLに接続するためのコマンド
CMD_MYSQL="mysql -u${MYSQL_USER} -p${MYSQL_PASSWORD} ${MYSQL_DATABASE}"

# ユーザーテーブルの作成
$CMD_MYSQL -e "create table if not exists User(
    id int AUTO_INCREMENT NOT NULL primary key,
    user_name varchar(50) NOT NULL,
    mail_address varchar(255) NOT NULL UNIQUE,
    password char(128) NOT NULL,
    profile_image varchar(255)
    );"

# カテゴリーテーブルの作成
$CMD_MYSQL -e "create table if not exists Category(
    id int AUTO_INCREMENT NOT NULL primary key,
    category_name varchar(50) NOT NULL UNIQUE
    );"

# 投稿情報テーブルの作成
$CMD_MYSQL -e "create table if not exists Postinformation(
    id int AUTO_INCREMENT NOT NULL primary key,
    post_title varchar(255) NOT NULL,
    post_details longtext NOT NULL,
    post_date datetime default current_timestamp,
    poster_id int,
    tag varchar(128),
    category_id int,
    foreign key (poster_id) references User(id),
    foreign key (category_id) references Category(id)
);"

# コメントテーブルの作成
$CMD_MYSQL -e "create table if not exists Comment(
    id int AUTO_INCREMENT NOT NULL primary key,
    commenter_id int,
    post_id int,
    foreign key (commenter_id) references User(id),
    foreign key (post_id) references Postinformation(id)
);"

# いいねテーブルの作成
$CMD_MYSQL -e "create table if not exists Good(
    id int AUTO_INCREMENT NOT NULL primary key,
    gooder_id int,
    post_id int,
    foreign key (gooder_id) references User(id),
    foreign key (post_id) references Postinformation(id)
)"
