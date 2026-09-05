def graph_to_html(graph):
    from pyvis.network import Network

    net = Network(height="580px", width="100%", bgcolor="#ffffff", font_color="#222222")
    net.barnes_hut()

    for node, data in graph.nodes(data=True):
        net.add_node(
            node,
            label=data.get("label", node),
            title=data.get("group", ""),
        )

    for source, target, data in graph.edges(data=True):
        net.add_edge(source, target, label=data.get("relation", ""))

    return net.generate_html()
