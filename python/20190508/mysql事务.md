-- 买家
create table buyer(
	id int not null auto_increment primary key,
	name varchar(20) not null,
	money float default 0
)engine=innodb charset=utf8;

insert into buyer
(name, money)
values
("张三",10000),
("李四",100);

-- 中介
create table intermediary(
	id int not null auto_increment primary key,
	name varchar(20) not null,
	money float default 0
)engine=innodb charset=utf8;

insert into intermediary
(name, money)
values
("jack",0),
("tom",0);

-- 卖家 
create table seller(
	id int not null auto_increment primary key,
	name varchar(20) not null,
	money float default 0
)engine=innodb charset=utf8;

insert into seller
(name, money)
values
("jerry",0),
("alex",0);


-- 中介和卖家的分成比例为 1:9

-- 事务正常执行
begin;

update buyer set money = 9000 where name = "张三";

update intermediary set money = 100 where name = "jack";

update seller set money = 900 where name = "alex";

commit;


-- 事务回滚
begin;

update buyer set money = 90 where name = "李四";

update intermediary set money = 2 where name = "tom";

update seller set money = 8 where name = "jerry";

rollback;

commit;



-- 设置保存点

begin;

update buyer set money = 90 where name = "李四";

update intermediary set money = 2 where name = "tom";

savepoint bawangtiaokuan;

update seller set money = 8 where name = "jerry";

rollback to bawangtiaokuan;

commit;
