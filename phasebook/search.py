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

    userList = []

    if len(args) == 0:
        # By default, return all users when there is no criteria given
        userList = USERS.copy()
    
    if "id" in args:
        # Return the matching user(s) by id, using List Comprehension
        # ONLY IF the user(s) are not yet added to the list
        [userList.append(user) for user in USERS if int(user["id"]) == int(args["id"]) if user not in userList]

    if "name" in args:
        # Return the matching user(s) by name (either partial or full), using List Comprehension
        # ONLY IF the user(s) are not yet added to the list
        [userList.append(user) for user in USERS if user["name"].casefold().find(args["name"].casefold()) > -1 if user not in userList]

    if "age" in args:
        # Return the matching user(s) by age such that (age-1 <= age <= age+1), using List Comprehension
        # ONLY IF the user(s) are not yet added to the list
        [userList.append(user) for user in USERS if (int(args["age"]) - 1 <= user["age"] <= int(args["age"]) + 1) if user not in userList]

    if "occupation" in args:
        # Return the matching user(s) by occupation (either partial or full), using List Comprehension
        # ONLY IF the user(s) are not yet added to the list
        [userList.append(user) for user in USERS if user["occupation"].casefold().find(args["occupation"].casefold()) > -1 if user not in userList]

    # -------------------------------------------------------------------
    # If the following statement is Commented, the results are sorted
    # according to the given matching priority: id, name, age, occupation
    #
    # Otherwise, the results are sorted by id
    # -------------------------------------------------------------------
    
    # userList = sorted(userList, key = lambda x: x["id"])

    return userList
