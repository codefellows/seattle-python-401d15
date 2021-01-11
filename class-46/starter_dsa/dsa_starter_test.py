def test_breadth_first():

  g = Graph()

  pandora = g.add_node("Pandora")

  arendelle = g.add_node("Arendelle")

  metroville = g.add_node("Metroville")

  monstropolis = g.add_node("Monstropolis")

  narnia = g.add_node("Narnia")

  naboo = g.add_node("Naboo")

  g.add_edge(pandora, arendelle)
  g.add_edge(arendelle, pandora)

  g.add_edge(arendelle, metroville)
  g.add_edge(metroville, arendelle)

  g.add_edge(arendelle, monstropolis)
  g.add_edge(monstropolis, arendelle)

  g.add_edge(metroville, monstropolis)
  g.add_edge(monstropolis, metroville)

  g.add_edge(metroville, narnia)
  g.add_edge(narnia, metroville)

  g.add_edge(metroville, naboo)
  g.add_edge(naboo, metroville)

  g.add_edge(narnia, naboo)
  g.add_edge(naboo, narnia)

  # stretch make more flexible vs. always returning list of vertices

  vertices = g.breadth_first(pandora)

  # this code assumes list of vertices/nodes is returned
  # you can alternately return list of values instead
  # In that case tweak code as needed

  # convert vertices into values for easier testing
  values = [vertex.value for vertex in vertices]

  assert values == ["Pandora", "Arendelle", "Metroville", "Monstropolis", "Narnia", "Naboo"]
