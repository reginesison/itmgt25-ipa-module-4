'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
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
    fromFollowingArray = social_graph[from_member]["following"]
    toFollowingArray = social_graph[to_member]["following"]

    if to_member in fromFollowingArray and from_member in toFollowingArray: return("friends")
    elif to_member in fromFollowingArray: return("follower")
    elif from_member in toFollowingArray: return("followed by")
    else:
        return("no relationship")

# relationship_status("@joeilagan", "@chums", social_graph)

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
    
    # determine how many elements are in array
    # how many x and how many o

    # diagonals
    if len(set([board[element][element] for element in range(len(board))])) == 1:
        return board[0][0]
    elif len(set([board[element][len(board)-element-1] for element in range(len(board))])) == 1:
        return board[0][len(board)-1]
    
    # rows
    for element in range(len(board)-1):
        if (board[element][element] != None) and (board[element][0] == board[element][1]) and (board[element][1] == board[element][2]):
            return board[element][element]
        else: continue

    # columns

    for element in range(len(board)):
        if (board[0][element] != None) and (board[0][element] == board[1][element]) and (board[1][element] == board[2][element]):
            return board[0][element]
        else: continue 
            
# print(tic_tac_toe(board7))

legs = {
    ("upd","admu"):{
        "travel_time_mins":10
    },
    ("admu","dlsu"):{
        "travel_time_mins":35
    },
    ("dlsu","upd"):{
        "travel_time_mins":55
    }
}

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

    if first_stop != second_stop:
        if (first_stop,second_stop) in route_map:
            time = route_map[first_stop,second_stop]['travel_time_mins']
            # print((first_stop,second_stop), time)

            return time
        else:            
            newList = list(route_map.keys())
            sourceList = []
            destinationList = []
            for i in newList:
                sourceList.append(i[0])
                destinationList.append(i[1])
                
            time = route_map[newList[sourceList.index(first_stop)]]['travel_time_mins'] + route_map[newList[destinationList.index(second_stop)]]['travel_time_mins']

            # print((first_stop,second_stop), time)

            return time
    
    else:
        # print((first_stop,second_stop), 0)

        return 0

eta("admu","upd", legs)