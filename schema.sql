drop table if exists users;
drop table if exists reports;
drop table if exists reports;
create table users (
  id integer primary key autoincrement,
  username text unique not null,
  password text not null,
  account_ssid text check(account_ssid not null and length(account_ssid) == 19),
  auth_token text check(auth_token not null and length(auth_token) == 18)
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
