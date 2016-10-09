drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);
create table users (
  id integer primary key autoincrement,
  username text unique not null,
  password text not null,
  account_ssid text check(account_ssid not null and length(account_ssid) == 19),
  auth_token text check(auth_token not null and length(auth_token) == 18)
);