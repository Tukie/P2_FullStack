#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = psycopg2.connect("dbname=tournament")
    cur = DB.cursor()
    cur.execute("DELETE FROM matches")
    DB.commit()
    DB.close()

def deletePlayers():
    """Remove all the player records from the database."""
    DB = psycopg2.connect("dbname=tournament")
    cur = DB.cursor()
    cur.execute("DELETE FROM players")
    DB.commit()
    DB.close()

def countPlayers():
    """Returns the number of players currently registered."""
    DB = psycopg2.connect("dbname=tournament")
    cur = DB.cursor()
    cur.execute("SELECT count(*) as num FROM players")
    result = cur.fetchone() 
    num_of_player = result[0]
    DB.commit()
    DB.close()
    return num_of_player

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = psycopg2.connect("dbname=tournament")
    cur = DB.cursor()
    cur.execute("INSERT INTO players (name) values (%s)", (name,))
    DB.commit()
    DB.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = psycopg2.connect("dbname=tournament")
    cur = DB.cursor()
    cur.execute("SELECT win_total.id, win_total.name, win_total.win_num\
                , mat_total.mat_num \
                FROM win_total, mat_total where mat_total.id = win_total.id \
                ORDER BY win_total.win_num DESC;")
    DB.commit()
    stands=[]
    for row in cur.fetchall():
        # standing format: id, name, wins, matches
        stands.append( (str(row[0]),  str(row[1]), row[2], row[3]) )
    # print "standings: "
    # print stands
    DB.close()
    return stands

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = psycopg2.connect("dbname=tournament")
    cur = DB.cursor()
    cur.execute("INSERT INTO matches (p1,p2,winnerID) \
                values (%s,%s,%s);", (winner, loser, winner,))
    DB.commit()
    DB.close()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # Get data players list and theirs win_record sorted by wins total
    DB = psycopg2.connect("dbname=tournament")
    cur = DB.cursor()
    cur.execute("DROP VIEW win_total")
    cur.execute("CREATE VIEW win_total AS \
                SELECT players.id, players.name, count(matches.winnerID) \
                as win_num \
                FROM players left join matches on matches.winnerID = players.id \
                group by players.id ORDER by win_num DESC;")
    cur.execute("SELECT * FROM win_total")
    DB.commit()
    
    rows=cur.fetchall()
    #print rows
    if (len(rows) % 2 != 0):
        raise ValueError(
            "Number of Player is not suitable for Swiss pairing.")
    pairs=[]
    for i in range(len(rows)):
        # pairing format: id, name, id, name
        if(i%2 == 0):
            pairs.append( (str(rows[i][0]),  str(rows[i][1])) )
        else:
            pairs[len(pairs)-1] = pairs[len(pairs)-1] + (str(rows[i][0]),  str(rows[i][1]))
    DB.close()
    # print pairs
    return pairs
