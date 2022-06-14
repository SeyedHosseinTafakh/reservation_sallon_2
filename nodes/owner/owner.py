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
                           name=name, password=password, phone_number=phone_number )
    return True