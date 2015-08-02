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

-- Database view sorted number of matches
CREATE VIEW mat_total AS
SELECT players.id, count (matches.winnerID) AS mat_num FROM players 
left join matches on matches.p1 = players.id or matches.p2 = players.id
GROUP BY players.id ORDER BY mat_num DESC;                        

-- Database view sorted number of winners
CREATE VIEW win_total AS
SELECT players.id, players.name, count(matches.winnerID) AS win_num 
FROM players left join matches on matches.winnerID = players.id
GROUP BY players.id ORDER by win_num DESC;

-- Database view for player standings tournament based on the sorted winners 
CREATE VIEW players_stands AS 
SELECT win_total.id, win_total.name, win_total.win_num, mat_total.mat_num
FROM win_total, mat_total WHERE mat_total.id = win_total.id
ORDER BY win_total.win_num DESC;