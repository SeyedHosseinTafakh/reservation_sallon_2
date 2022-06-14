from services.neo4j import driver


def existence_of_owner_by_id(owner_id):
    with driver.session() as session:
        node = session.run("match (b:owner{id:$owner_id}) "
                           "where not exists (b.updated_at) and not exists(b.deleted_at) "
                           "return b",
                           owner_id=owner_id)
        node = node.data()
        if not node:
            return False
        else:
            return True


def create_saloon(name, phone_number, address, location, owner_id):
    if not existence_of_owner_by_id(owner_id=owner_id):
        return False
    with driver.session() as session:
        node = session.run("match (owner:owner {id:$owner_id})"
                           "create (saloon:saloon {id:apoc.create.uuid(), "
                           "created_at:datetime(), "
                           "name:$name, "
                           "phone_number:$phone_number, "
                           "address:$address, "
                           "location:$location}), "
                           "(owner) - [:Created_at{Created_at:datetime()}] -> (saloon)",
                           name=name, phone_number=phone_number, address=address, location=location,owner_id=owner_id )
    return True