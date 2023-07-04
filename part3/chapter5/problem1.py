"""
[1] create table registered_member(
    -> id int primary key,
    -> name varchar(20) not null,
    -> age int not null,
    -> gender varchar(10) not null,
    -> address varchar(10),
    -> grade int not null,
    -> datetime datetime not null
);

    create table retired_member(
    -> id int primary key,
    -> name varchar(20) not null,
    -> age int not null,
    -> gender varchar(10) not null,
    -> address varchar(100),
    -> grade int not null,
    -> datetime datetime not null
);

[2] insert into registered_member(id, name, age, gender, address, grade, datetime) values(2, '홍길동', 20, '남성', '경기', 4, '2012-06-12 15:00:00');
    insert into retired_member(id, name, age, gender, address, grade, datetime) values(1, '나동빈', 30, '남성', '경기', 4, '2012-08-03 13:00:00');

[3] select * from registered_member order by name asc;

[4] select name from registered_member where age >= 30 order by name;

[5] select name, datetime from registered_member order by datetime desc limit 1;

[6] select * from registered_member order by grade desc, datetime;

[7] select grade from registered_member order by grade limit 1;

[8] select count(*) from registered_member;

[9] select count(distinct grade) from registered_member;

[10] select grade, count(grade) from registered_member group by grade order by grade;

[11] select grade, count(grade) from registered_member group by grade having count(grade)>=2 order by grade;

[12] select * from registered_member where datetime between '2012-07-01' and '2012-09-30' order by datetime;

[13] select month(datetime), count(datetime) from registered_member where datetime between '2012-07-01' and '2012-09-30' group by month(datetime);

[14] mysql> select month(datetime), count(datetime) from registered_member where datetime between '2012-01-01' and '2012-08-31' group by month(datetime);
    -> set 으로 변수를 생성해서 컬럼을 생성하고, 데이터를 추가해야 한다.

[15] select id from registered_member where address is null order by id;

[16] select id from registered_member where address is not null order by id;

[17] select name, (case when address is null then '지역 정보 없음' else address end) as address , grade from registered_member order by name;
    -> select name, IFNULL(address, '지역정보없음') as address, grade from registered_member order by name;

[18] select name, address, gender, datetime from registered_member where address = '경기' order by name;

[19] select name, (case when age >= 30 then 'old' else 'young' end) as age from registered_member order by name;

[20] select registered_member.id, registered_member.name from registered_member, retired_member where registered_member.datetime > retired_member.datetime and registered_member.id = retired_member.id;

[21] select retired_member.id, retired_member.name from retired_member where retired_member.id not in (select registered_member.id from registered_member) order by retired_member.id;
    // 차집합
    -> select * from retired_member left join registered_member on retired_member.id = registered_member.id where registered_member.id in null

[22] select registered_member.name, registered_member.age, registered_member.datetime from registered_member where registered_member.id not in (select retired_member.id from retired_member) order by registered_member.datetime limit 2;

[23] select registered_member.name, retired_member.datetime, retired_member.grade from registered_member, retired_member where retired_member.id = registered_member.id and registered_member.grade > retired_member.grade order by registered_member.name;

[24] select gender, avg(age), avg(grade) from registered_member group by gender order by avg(grade); // group by 는 해당 속서으로 데이터를 묶음을 의미, 성별로 묶으면 여성, 남성에 맞는 데이터 끼리 묶임 ㅋ

[25] select name, grade, age, datetime from registered_member where name like '_동빈' or name like '_길동' or name like '_민정' or name like '_성민' order by datetime;

[26] select name, grade, age, datetime from registered_member where name like '홍길동' or name like '이순신' or name like '김성민' order by datetime;
    -> select name, grade, age, datetime from registered_member where name in ('이순신', '홍길동', '김성민') order by datetime;

[27] ?오타? select name, grade, age, datetime from registered_member where name like '%민%' and gender='남성' order by datetime;

[28] select name, grade from registered_member order by datetime limit 3;
    -> 오랜기간 다녔다는 것은 (등록날짜 - 탈퇴날짜) DESC 이다.

[29] select name, date_format(datetime, '%Y-%m-%d') as date from registered_member where gender='남성' order by datetime;

"""