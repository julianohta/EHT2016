drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);
create table users (
  id integer primary key autoincrement,
  username text unique not null,
  password test not null
);