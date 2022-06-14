from services.neo4j import driver
from ..owner import owner


def existence_of_saloon_by_id(saloon_id):
    with driver.session() as session:
        node = session.run("match (b:saloon{id:$saloon_id}) "
                           "where not exists (b.updated_at) and not exists(b.deleted_at) "
                           "return b",
                           saloon_id=saloon_id)
        node = node.data()
        if not node:
            return False
        else:
            return True

def existence_of_worker(phone_number):
    with driver.session() as session:
        node = session.run("match (b:worker{phone_number:$phone_number}) "
                           "where not exists (b.updated_at) and not exists(b.deleted_at) "
                           "return b",
                           phone_number=phone_number)
        node = node.data()
        if node:
            return True
        else:
            return False

def create_worker(name, phone_number, password, instagram_link):
    if owner.existence_of_owner(phone_number=phone_number) or existence_of_worker(phone_number=phone_number):
        return False
    with driver.session() as session:
        session.run("create (worker:worker {id:apoc.create.uuid(), "
                    "created_at:datetime(), "
                    "name:$name, "
                    "phone_number:$phone_number, "
                    "password:$password, "
                    "instagram_link:$instagram_link} )",
                    name=name, phone_number=phone_number, password=password, instagram_link=instagram_link)
    return True

#TODO:: create connect and dissconnet to saloon functions