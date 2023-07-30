'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
#given  sample data
social_graph = {
    "@bongolpoc": {
        "first_name": "Joselito",
        "last_name": "Olpoc",
        "following": []
    },
    "@joaquin": {
        "first_name": "Joaquin",
        "last_name": "Gonzales",
        "following": ["@chums", "@jobenilagan"]
    },
    "@chums": {
        "first_name": "Matthew",
        "last_name": "Uy",
        "following": ["@bongolpoc", "@miketan", "@rudyang", "@joeilagan"]
    },
    "@jobenilagan": {
        "first_name": "Joben",
        "last_name": "Ilagan",
        "following": ["@eeebeee", "@joeilagan", "@chums", "@joaquin"]
    },
    "@joeilagan": {
        "first_name": "Joe",
        "last_name": "Ilagan",
        "following": ["@eeebeee", "@jobenilagan", "@chums"]
    },
    "@eeebeee": {
        "first_name": "Elizabeth",
        "last_name": "Ilagan",
        "following": ["@jobenilagan", "@joeilagan"]
    },
}

def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph.get(from_member, {}).get("following", []):
        if from_member in social_graph.get(to_member, {}).get("following", []):
            return "friends"
        else:
            return "follower"
    elif from_member in social_graph.get(to_member, {}).get("following", []):
        return "followed by"
    else:
        return "no relationship"

print(relationship_status("@bongolpoc", "@chums", social_graph))
print(relationship_status("@chums", "@joeilagan", social_graph))
print(relationship_status("@joeilagan", "@chums", social_graph))
print(relationship_status("@joeilagan", "@bongolpoc", social_graph))
print(relationship_status("@joaquin", "@jobenilagan", social_graph))


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def tic_tac_toe(board):
    def check_line(line):
        return all(cell == line[0] for cell in line) and line[0] != ''

    for row in board:
        if check_line(row):
            return row[0]

    for col in range(len(board)):
        if check_line([board[row][col] for row in range(len(board))]):
            return board[0][col]

    if check_line([board[i][i] for i in range(len(board))]) or check_line([board[i][len(board) - 1 - i] for i in range(len(board))]):
        return board[len(board) // 2][len(board) // 2]

    return "NO WINNER"

#given sample data
board1 = [
    ['X', 'X', 'O'],
    ['O', 'X', 'O'],
    ['O', '', 'X'],
]

board2 = [
    ['X', 'X', 'O'],
    ['O', 'X', 'O'],
    ['', 'O', 'X'],
]

board3 = [
    ['O', 'X', 'O'],
    ['', 'O', 'X'],
    ['X', 'X', 'O'],
]

board4 = [
    ['X', 'X', 'X'],
    ['O', 'X', 'O'],
    ['O', '', 'O'],
]

board5 = [
    ['X', 'X', 'O'],
    ['O', 'X', 'O'],
    ['X', '', 'O'],
]

board6 = [
    ['X', 'X', 'O'],
    ['O', 'X', 'O'],
    ['X', '', ''],
]

board7 = [
    ['X', 'X', 'O', ''],
    ['O', 'X', 'O', 'O'],
    ['X', '', '', 'O'],
    ['O', 'X', '', '']
]

print(tic_tac_toe(board1))
print(tic_tac_toe(board2))  
print(tic_tac_toe(board3))
print(tic_tac_toe(board4))  
print(tic_tac_toe(board5)) 
print(tic_tac_toe(board6))  
print(tic_tac_toe(board7))  


def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
def eta(first_stop, second_stop, route_map):
    def get_travel_time(from_stop, to_stop):
        leg = route_map.get((from_stop, to_stop))
        if leg:
            return leg['travel_time_mins']
        return None

    def find_route_time(start, end, stops, total_time):
        if start == end:
            return total_time
        for next_stop in stops:
            travel_time = get_travel_time(start, next_stop)
            if travel_time is not None:
                remaining_stops = [stop for stop in stops if stop != start]
                result = find_route_time(next_stop, end, remaining_stops, total_time + travel_time)
                if result is not None:
                    return result

    stops = {stop for leg in route_map.keys() for stop in leg}
    return find_route_time(first_stop, second_stop, stops, 0)

#given sample data
legs = {
    ("upd", "admu"): {
        "travel_time_mins": 10
    },
    ("admu", "dlsu"): {
        "travel_time_mins": 35
    },
    ("dlsu", "upd"): {
        "travel_time_mins": 55
    }
}

#test
print(eta("upd", "admu", legs))  
print(eta("admu", "dlsu", legs))  
print(eta("dlsu", "upd", legs))  


legs_2 = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}

print(eta('a1', 'a2', legs_2))  
print(eta('a1', 'b1', legs_2))  
