from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    # Implement search here!


    userQueries = request.args
    validQueryParams = {"id": "id", "name": "name", "age": "age", "occupation": "occupation"}
    userValidQueries = []
    
    # Get and store valid user queries(keys only, no values) to "userValidQueries"
    def getValidQueries():
        for validQuery in validQueryParams:
            if validQuery in userQueries:
                userValidQueries.append(validQuery)

    # Filter users
    def filterUsers():
        getValidQueries()
        users = []

        # All of the search parameters are optional.
        if(len(userValidQueries)==0):
            return USERS

        # Loop through USERS data
        for user in USERS:
            # Loop through user queries and satisfy
                #The id is unique. If the id is included in the search parameters,
                    # then immediately include the user with the passed id.
                # The name can be partially matched and is case insensitive.
                # The occupation parameter can be partially matched and is case insensitive.
                    # This means that if we pass "er" to the occupation parameter,
                # The age parameter should include users that are in the range of age - 1 to age + 1.
                    # we should include all users with an occupation that contains "er" in the results.
                # Do not include a user in the results more than once.
            if "id" in userValidQueries:
                if userQueries["id"] == user["id"]:
                    if user not in users:
                            users.append(user)

            if "name" in userValidQueries :
                if userQueries["name"].lower() in user["name"].lower() :
                    if user not in users:
                        users.append(user)

            if "occupation" in userValidQueries:
                if userQueries["occupation"].lower() in user["occupation"].lower():
                    if user not in users:
                        users.append(user)

            if "age" in userValidQueries:
                if int(userQueries["age"]) <= int(user["age"])+1 and int(userQueries["age"]) >= int(user["age"]-1):
                    if user not in users:
                            users.append(user)

        return users   

    

    return filterUsers()
