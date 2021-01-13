from graph_dfs import Graph

def test_dfs():

    graph = Graph()

    a = graph.add_node("a")
    b = graph.add_node("b")
    c = graph.add_node("c")
    d = graph.add_node("d")
    e = graph.add_node("e")
    f = graph.add_node("f")
    g = graph.add_node("g")
    h = graph.add_node("h")

    graph.add_edge(a, b)
    graph.add_edge(b, c)
    graph.add_edge(c, g)
    graph.add_edge(a, d)

    graph.add_edge(d, e)
    graph.add_edge(d, h)
    graph.add_edge(d, f)

    graph.add_edge(h, f)

    actual = graph.depth_first_search(a)

    expected = ["a", "b", "c", "g", "d", "e", "h", "f"]

    assert actual == expected
