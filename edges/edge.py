from services.neo4j import driver


def connect_nodes(first_node_id,second_node_id):
    with driver.session() as session:
        session.run("match(first_node {id:$first_node_id}), "
                    "(second_node {id:$second_node_id})  "
                    "create (first_node)-[r:rel  {created_at:datetime(),id:apoc.create.uuid()}]->(second_node) ",
                    first_node_id=first_node_id,second_node_id=second_node_id
                    )
    return True


def delete_connection(first_node_id,second_node_id):
    with driver.session() as session:
        session.run("match (first_node{id:$first_node_id})-[r]->(second_node{id:$second_node_id}) "
                    "delete r ",
                    first_node_id=first_node_id,second_node_id=second_node_id)
    return True


def check_connection(first_node_id,second_node_id):
    with driver.session() as session:
        connection = session.run("match (first_node{id:$first_node_id})-[r]->(second_node{id:$second_node_id}) "
                                 "return r ",
                    first_node_id=first_node_id,second_node_id=second_node_id)
        connection = connection.graph().relationships
        con_list=[]
        for i in connection:
            x = list(i.values())
            x.append(i.type)
            con_list.append(x)
        print(con_list)
    if connection:
        return True, con_list
    return False, None


