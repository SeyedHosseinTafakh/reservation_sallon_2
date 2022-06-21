from services.neo4j import driver


def existence_of_owner(phone_number):
    with driver.session() as session:
        node = session.run("match (b:owner{phone_number:$phone_number}) "
                           "where not exists (b.updated_at) and not exists(b.deleted_at) "
                           "return b",
                           phone_number=phone_number)
        node = node.data()
        if not node:
            return False
        else:
            return True


def create_owner(name, password, phone_number):
    if existence_of_owner(phone_number=phone_number):
        return False
    with driver.session() as session:
        node = session.run("create (owner:owner {id:apoc.create.uuid(), "
                           "created_at:datetime(), "
                           "name:$name, "
                           "phone_number:$phone_number}) ",
                           name=name, password=password, phone_number=phone_number)
    return True

def get_owners():
    with driver.session() as session:
        nodes = session.run("match (n:owner) return n as owners").data()
    return nodes


# def add_available_time(start,end,worker_id):
#     with driver.session() as session:
#         available_time = session.run("create (available_time:available_time {id:apoc.create.uuid(), "
#                     "created_at:datetime(), "
#                     "start_date:$start, "
#                     "end:$end}) return available_time.id as id",start=start, end=end)
#         available_time_id = available_time.data()[0]['id']
#         session.run('match (worker:worker ),(available_time:available_time ) where worker.id=$worker_id and available_time.id=$available_time_id '
#                     'create (worker)-[:rel {created_at:datetime()}]->(available_time)',worker_id=worker_id,available_time_id=available_time_id)

