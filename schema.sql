drop table if exists users;
drop table if exists reports;
drop table if exists persons;
create table users (
  id integer primary key autoincrement,
  tax_id integer check(tax_id not null and length(tax_id) == 9),
  precinct text not null,
  sector text not null,
  password text not null,
  first_name text not null,
  last_name text not null,
  account_sid text check(account_sid not null and length(account_sid) == 34),
  auth_token text check(auth_token not null and length(auth_token) == 32)
);
create table reports (
	id integer primary key autoincrement,
	description text not null,
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
