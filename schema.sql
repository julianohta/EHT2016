drop table if exists users;
drop table if exists reports;
drop table if exists reports;
create table users (
  id integer primary key autoincrement,
  username text unique not null,
  password text not null
);
create table reports (
	id integer primary key autoincrement,
	location text not null,
	time text,
	date text not null,
	venue_name text,
	venue_type text,
	media text,
	victims text,
	suspects text
);
create table persons (
	id integer primary key autoincrement,
	type integer,
	name text,
	alias text,
	ethnicity text,
	gender text,
	age integer,
	eyes text,
	hair text,
	build text,
	height integer,
	mods text,
	clothing text,
	comments text
)