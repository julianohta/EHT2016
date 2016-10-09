drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);
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