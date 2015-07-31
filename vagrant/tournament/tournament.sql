-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament;

CREATE TABLE players ( id SERIAL PRIMARY KEY,
                        name TEXT);
                        
CREATE TABLE matches ( match_id SERIAL PRIMARY KEY,
                        p1 INTEGER REFERENCES players(id),
                        p2 INTEGER REFERENCES players(id),
                        winnerID INTEGER);

CREATE VIEW mat_total AS
SELECT players.id, count (matches.winnerID) as mat_num FROM players left join matches on matches.p1 = players.id 
or matches.p2 = players.id group by players.id order by mat_num DESC;                        
                        
CREATE VIEW win_total AS
SELECT players.id, players.name, count(matches.winnerID) as win_num 
FROM players left join matches on matches.winnerID = players.id group by players.id ORDER by win_num DESC;