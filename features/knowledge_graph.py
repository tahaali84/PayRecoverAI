import networkx as nx

def build_payment_graph(transaction):
    g = nx.Graph()

    txn = str(transaction["transaction_id"])
    customer = str(transaction["customer_id"])
    method = str(transaction["payment_method"])
    reason = str(transaction["failure_reason"]) or "SUCCESS"
    status = str(transaction["status"])

    g.add_node(txn, label=txn, group="Transaction")
    g.add_node(customer, label=customer, group="Customer")
    g.add_node(method, label=method, group="Payment Method")
    g.add_node(reason, label=reason, group="Failure Reason")
    g.add_node(status, label=status, group="Status")

    g.add_edge(customer, txn, relation="made")
    g.add_edge(txn, method, relation="used")
    g.add_edge(txn, reason, relation="has_reason")
    g.add_edge(txn, status, relation="has_status")

    return g
