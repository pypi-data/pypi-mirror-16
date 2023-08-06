'''
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
'''
from .traversal import RawExpression
from .traversal import Traversal
from .traversal import Bytecode
from gremlin_python import statics

class GraphTraversalSource(object):
  def __init__(self, graph, traversal_strategies, graph_traversal=None, bytecode=Bytecode()):
    self.graph = graph
    self.traversal_strategies = traversal_strategies
    if graph_traversal is None:
        graph_traversal = GraphTraversal
    self.graph_traversal = graph_traversal
    self.bytecode = bytecode
  def __repr__(self):
    return "graphtraversalsource[" + str(self.graph) + "]"
  def E(self, *args):
    traversal = self.graph_traversal(self.graph, self.traversal_strategies, Bytecode(self.bytecode))
    traversal.bytecode.add_step("E", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return traversal
  def V(self, *args):
    traversal = self.graph_traversal(self.graph, self.traversal_strategies, Bytecode(self.bytecode))
    traversal.bytecode.add_step("V", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return traversal
  def addV(self, *args):
    traversal = self.graph_traversal(self.graph, self.traversal_strategies, Bytecode(self.bytecode))
    traversal.bytecode.add_step("addV", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return traversal
  def inject(self, *args):
    traversal = self.graph_traversal(self.graph, self.traversal_strategies, Bytecode(self.bytecode))
    traversal.bytecode.add_step("inject", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return traversal
  def withBulk(self, *args):
    source = GraphTraversalSource(self.graph, self.traversal_strategies, Bytecode(self.bytecode))
    source.bytecode.add_source("withBulk", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return source
  def withComputer(self, *args):
    source = GraphTraversalSource(self.graph, self.traversal_strategies, Bytecode(self.bytecode))
    source.bytecode.add_source("withComputer", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return source
  def withPath(self, *args):
    source = GraphTraversalSource(self.graph, self.traversal_strategies, Bytecode(self.bytecode))
    source.bytecode.add_source("withPath", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return source
  def withSack(self, *args):
    source = GraphTraversalSource(self.graph, self.traversal_strategies, Bytecode(self.bytecode))
    source.bytecode.add_source("withSack", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return source
  def withSideEffect(self, *args):
    source = GraphTraversalSource(self.graph, self.traversal_strategies, Bytecode(self.bytecode))
    source.bytecode.add_source("withSideEffect", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return source
  def withStrategies(self, *args):
    source = GraphTraversalSource(self.graph, self.traversal_strategies, Bytecode(self.bytecode))
    source.bytecode.add_source("withStrategies", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return source
  def withTranslator(self, *args):
    source = GraphTraversalSource(self.graph, self.traversal_strategies, Bytecode(self.bytecode))
    source.bytecode.add_source("withTranslator", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return source
  def withoutStrategies(self, *args):
    source = GraphTraversalSource(self.graph, self.traversal_strategies, Bytecode(self.bytecode))
    source.bytecode.add_source("withoutStrategies", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return source


class GraphTraversal(Traversal):
  def __init__(self, graph, traversal_strategies, bytecode):
    Traversal.__init__(self, graph, traversal_strategies, bytecode)
  def V(self, *args):
    self.bytecode.add_step("V", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def _and(self, *args):
    self.bytecode.add_step("_and", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def _as(self, *args):
    self.bytecode.add_step("_as", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def _from(self, *args):
    self.bytecode.add_step("_from", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def _in(self, *args):
    self.bytecode.add_step("_in", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def _is(self, *args):
    self.bytecode.add_step("_is", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def _not(self, *args):
    self.bytecode.add_step("_not", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def _or(self, *args):
    self.bytecode.add_step("_or", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def addE(self, *args):
    self.bytecode.add_step("addE", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def addInE(self, *args):
    self.bytecode.add_step("addInE", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def addOutE(self, *args):
    self.bytecode.add_step("addOutE", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def addV(self, *args):
    self.bytecode.add_step("addV", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def aggregate(self, *args):
    self.bytecode.add_step("aggregate", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def asAdmin(self, *args):
    self.bytecode.add_step("asAdmin", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def barrier(self, *args):
    self.bytecode.add_step("barrier", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def both(self, *args):
    self.bytecode.add_step("both", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def bothE(self, *args):
    self.bytecode.add_step("bothE", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def bothV(self, *args):
    self.bytecode.add_step("bothV", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def branch(self, *args):
    self.bytecode.add_step("branch", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def by(self, *args):
    self.bytecode.add_step("by", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def cap(self, *args):
    self.bytecode.add_step("cap", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def choose(self, *args):
    self.bytecode.add_step("choose", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def coalesce(self, *args):
    self.bytecode.add_step("coalesce", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def coin(self, *args):
    self.bytecode.add_step("coin", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def constant(self, *args):
    self.bytecode.add_step("constant", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def count(self, *args):
    self.bytecode.add_step("count", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def cyclicPath(self, *args):
    self.bytecode.add_step("cyclicPath", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def dedup(self, *args):
    self.bytecode.add_step("dedup", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def drop(self, *args):
    self.bytecode.add_step("drop", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def emit(self, *args):
    self.bytecode.add_step("emit", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def filter(self, *args):
    self.bytecode.add_step("filter", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def flatMap(self, *args):
    self.bytecode.add_step("flatMap", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def fold(self, *args):
    self.bytecode.add_step("fold", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def group(self, *args):
    self.bytecode.add_step("group", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def groupCount(self, *args):
    self.bytecode.add_step("groupCount", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def groupV3d0(self, *args):
    self.bytecode.add_step("groupV3d0", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def has(self, *args):
    self.bytecode.add_step("has", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def hasId(self, *args):
    self.bytecode.add_step("hasId", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def hasKey(self, *args):
    self.bytecode.add_step("hasKey", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def hasLabel(self, *args):
    self.bytecode.add_step("hasLabel", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def hasNot(self, *args):
    self.bytecode.add_step("hasNot", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def hasValue(self, *args):
    self.bytecode.add_step("hasValue", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def id(self, *args):
    self.bytecode.add_step("id", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def identity(self, *args):
    self.bytecode.add_step("identity", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def inE(self, *args):
    self.bytecode.add_step("inE", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def inV(self, *args):
    self.bytecode.add_step("inV", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def inject(self, *args):
    self.bytecode.add_step("inject", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def iterate(self, *args):
    self.bytecode.add_step("iterate", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def key(self, *args):
    self.bytecode.add_step("key", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def label(self, *args):
    self.bytecode.add_step("label", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def limit(self, *args):
    self.bytecode.add_step("limit", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def local(self, *args):
    self.bytecode.add_step("local", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def loops(self, *args):
    self.bytecode.add_step("loops", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def map(self, *args):
    self.bytecode.add_step("map", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def mapKeys(self, *args):
    self.bytecode.add_step("mapKeys", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def mapValues(self, *args):
    self.bytecode.add_step("mapValues", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def match(self, *args):
    self.bytecode.add_step("match", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def max(self, *args):
    self.bytecode.add_step("max", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def mean(self, *args):
    self.bytecode.add_step("mean", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def min(self, *args):
    self.bytecode.add_step("min", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def option(self, *args):
    self.bytecode.add_step("option", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def optional(self, *args):
    self.bytecode.add_step("optional", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def order(self, *args):
    self.bytecode.add_step("order", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def otherV(self, *args):
    self.bytecode.add_step("otherV", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def out(self, *args):
    self.bytecode.add_step("out", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def outE(self, *args):
    self.bytecode.add_step("outE", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def outV(self, *args):
    self.bytecode.add_step("outV", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def pageRank(self, *args):
    self.bytecode.add_step("pageRank", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def path(self, *args):
    self.bytecode.add_step("path", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def peerPressure(self, *args):
    self.bytecode.add_step("peerPressure", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def profile(self, *args):
    self.bytecode.add_step("profile", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def program(self, *args):
    self.bytecode.add_step("program", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def project(self, *args):
    self.bytecode.add_step("project", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def properties(self, *args):
    self.bytecode.add_step("properties", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def property(self, *args):
    self.bytecode.add_step("property", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def propertyMap(self, *args):
    self.bytecode.add_step("propertyMap", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def range(self, *args):
    self.bytecode.add_step("range", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def repeat(self, *args):
    self.bytecode.add_step("repeat", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def sack(self, *args):
    self.bytecode.add_step("sack", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def sample(self, *args):
    self.bytecode.add_step("sample", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def select(self, *args):
    self.bytecode.add_step("select", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def sideEffect(self, *args):
    self.bytecode.add_step("sideEffect", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def simplePath(self, *args):
    self.bytecode.add_step("simplePath", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def store(self, *args):
    self.bytecode.add_step("store", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def subgraph(self, *args):
    self.bytecode.add_step("subgraph", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def sum(self, *args):
    self.bytecode.add_step("sum", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def tail(self, *args):
    self.bytecode.add_step("tail", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def timeLimit(self, *args):
    self.bytecode.add_step("timeLimit", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def times(self, *args):
    self.bytecode.add_step("times", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def to(self, *args):
    self.bytecode.add_step("to", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def toE(self, *args):
    self.bytecode.add_step("toE", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def toV(self, *args):
    self.bytecode.add_step("toV", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def tree(self, *args):
    self.bytecode.add_step("tree", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def unfold(self, *args):
    self.bytecode.add_step("unfold", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def union(self, *args):
    self.bytecode.add_step("union", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def until(self, *args):
    self.bytecode.add_step("until", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def value(self, *args):
    self.bytecode.add_step("value", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def valueMap(self, *args):
    self.bytecode.add_step("valueMap", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def values(self, *args):
    self.bytecode.add_step("values", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self
  def where(self, *args):
    self.bytecode.add_step("where", *args)
    for arg in args:
      if isinstance(arg, tuple) and 2 == len(arg) and isinstance(arg[0], str):
        self.bindings[arg[0]] = arg[1]
      elif isinstance(arg, RawExpression):
        self.bindings.update(arg.bindings)
    return self


class __(object):
  @staticmethod
  def V(*args):
    return GraphTraversal(None, None, Bytecode()).V(*args)
  @staticmethod
  def __(*args):
    return GraphTraversal(None, None, Bytecode()).__(*args)
  @staticmethod
  def _and(*args):
    return GraphTraversal(None, None, Bytecode())._and(*args)
  @staticmethod
  def _as(*args):
    return GraphTraversal(None, None, Bytecode())._as(*args)
  @staticmethod
  def _in(*args):
    return GraphTraversal(None, None, Bytecode())._in(*args)
  @staticmethod
  def _is(*args):
    return GraphTraversal(None, None, Bytecode())._is(*args)
  @staticmethod
  def _not(*args):
    return GraphTraversal(None, None, Bytecode())._not(*args)
  @staticmethod
  def _or(*args):
    return GraphTraversal(None, None, Bytecode())._or(*args)
  @staticmethod
  def addE(*args):
    return GraphTraversal(None, None, Bytecode()).addE(*args)
  @staticmethod
  def addInE(*args):
    return GraphTraversal(None, None, Bytecode()).addInE(*args)
  @staticmethod
  def addOutE(*args):
    return GraphTraversal(None, None, Bytecode()).addOutE(*args)
  @staticmethod
  def addV(*args):
    return GraphTraversal(None, None, Bytecode()).addV(*args)
  @staticmethod
  def aggregate(*args):
    return GraphTraversal(None, None, Bytecode()).aggregate(*args)
  @staticmethod
  def barrier(*args):
    return GraphTraversal(None, None, Bytecode()).barrier(*args)
  @staticmethod
  def both(*args):
    return GraphTraversal(None, None, Bytecode()).both(*args)
  @staticmethod
  def bothE(*args):
    return GraphTraversal(None, None, Bytecode()).bothE(*args)
  @staticmethod
  def bothV(*args):
    return GraphTraversal(None, None, Bytecode()).bothV(*args)
  @staticmethod
  def branch(*args):
    return GraphTraversal(None, None, Bytecode()).branch(*args)
  @staticmethod
  def cap(*args):
    return GraphTraversal(None, None, Bytecode()).cap(*args)
  @staticmethod
  def choose(*args):
    return GraphTraversal(None, None, Bytecode()).choose(*args)
  @staticmethod
  def coalesce(*args):
    return GraphTraversal(None, None, Bytecode()).coalesce(*args)
  @staticmethod
  def coin(*args):
    return GraphTraversal(None, None, Bytecode()).coin(*args)
  @staticmethod
  def constant(*args):
    return GraphTraversal(None, None, Bytecode()).constant(*args)
  @staticmethod
  def count(*args):
    return GraphTraversal(None, None, Bytecode()).count(*args)
  @staticmethod
  def cyclicPath(*args):
    return GraphTraversal(None, None, Bytecode()).cyclicPath(*args)
  @staticmethod
  def dedup(*args):
    return GraphTraversal(None, None, Bytecode()).dedup(*args)
  @staticmethod
  def drop(*args):
    return GraphTraversal(None, None, Bytecode()).drop(*args)
  @staticmethod
  def emit(*args):
    return GraphTraversal(None, None, Bytecode()).emit(*args)
  @staticmethod
  def filter(*args):
    return GraphTraversal(None, None, Bytecode()).filter(*args)
  @staticmethod
  def flatMap(*args):
    return GraphTraversal(None, None, Bytecode()).flatMap(*args)
  @staticmethod
  def fold(*args):
    return GraphTraversal(None, None, Bytecode()).fold(*args)
  @staticmethod
  def group(*args):
    return GraphTraversal(None, None, Bytecode()).group(*args)
  @staticmethod
  def groupCount(*args):
    return GraphTraversal(None, None, Bytecode()).groupCount(*args)
  @staticmethod
  def groupV3d0(*args):
    return GraphTraversal(None, None, Bytecode()).groupV3d0(*args)
  @staticmethod
  def has(*args):
    return GraphTraversal(None, None, Bytecode()).has(*args)
  @staticmethod
  def hasId(*args):
    return GraphTraversal(None, None, Bytecode()).hasId(*args)
  @staticmethod
  def hasKey(*args):
    return GraphTraversal(None, None, Bytecode()).hasKey(*args)
  @staticmethod
  def hasLabel(*args):
    return GraphTraversal(None, None, Bytecode()).hasLabel(*args)
  @staticmethod
  def hasNot(*args):
    return GraphTraversal(None, None, Bytecode()).hasNot(*args)
  @staticmethod
  def hasValue(*args):
    return GraphTraversal(None, None, Bytecode()).hasValue(*args)
  @staticmethod
  def id(*args):
    return GraphTraversal(None, None, Bytecode()).id(*args)
  @staticmethod
  def identity(*args):
    return GraphTraversal(None, None, Bytecode()).identity(*args)
  @staticmethod
  def inE(*args):
    return GraphTraversal(None, None, Bytecode()).inE(*args)
  @staticmethod
  def inV(*args):
    return GraphTraversal(None, None, Bytecode()).inV(*args)
  @staticmethod
  def inject(*args):
    return GraphTraversal(None, None, Bytecode()).inject(*args)
  @staticmethod
  def key(*args):
    return GraphTraversal(None, None, Bytecode()).key(*args)
  @staticmethod
  def label(*args):
    return GraphTraversal(None, None, Bytecode()).label(*args)
  @staticmethod
  def limit(*args):
    return GraphTraversal(None, None, Bytecode()).limit(*args)
  @staticmethod
  def local(*args):
    return GraphTraversal(None, None, Bytecode()).local(*args)
  @staticmethod
  def loops(*args):
    return GraphTraversal(None, None, Bytecode()).loops(*args)
  @staticmethod
  def map(*args):
    return GraphTraversal(None, None, Bytecode()).map(*args)
  @staticmethod
  def mapKeys(*args):
    return GraphTraversal(None, None, Bytecode()).mapKeys(*args)
  @staticmethod
  def mapValues(*args):
    return GraphTraversal(None, None, Bytecode()).mapValues(*args)
  @staticmethod
  def match(*args):
    return GraphTraversal(None, None, Bytecode()).match(*args)
  @staticmethod
  def max(*args):
    return GraphTraversal(None, None, Bytecode()).max(*args)
  @staticmethod
  def mean(*args):
    return GraphTraversal(None, None, Bytecode()).mean(*args)
  @staticmethod
  def min(*args):
    return GraphTraversal(None, None, Bytecode()).min(*args)
  @staticmethod
  def optional(*args):
    return GraphTraversal(None, None, Bytecode()).optional(*args)
  @staticmethod
  def order(*args):
    return GraphTraversal(None, None, Bytecode()).order(*args)
  @staticmethod
  def otherV(*args):
    return GraphTraversal(None, None, Bytecode()).otherV(*args)
  @staticmethod
  def out(*args):
    return GraphTraversal(None, None, Bytecode()).out(*args)
  @staticmethod
  def outE(*args):
    return GraphTraversal(None, None, Bytecode()).outE(*args)
  @staticmethod
  def outV(*args):
    return GraphTraversal(None, None, Bytecode()).outV(*args)
  @staticmethod
  def path(*args):
    return GraphTraversal(None, None, Bytecode()).path(*args)
  @staticmethod
  def project(*args):
    return GraphTraversal(None, None, Bytecode()).project(*args)
  @staticmethod
  def properties(*args):
    return GraphTraversal(None, None, Bytecode()).properties(*args)
  @staticmethod
  def property(*args):
    return GraphTraversal(None, None, Bytecode()).property(*args)
  @staticmethod
  def propertyMap(*args):
    return GraphTraversal(None, None, Bytecode()).propertyMap(*args)
  @staticmethod
  def range(*args):
    return GraphTraversal(None, None, Bytecode()).range(*args)
  @staticmethod
  def repeat(*args):
    return GraphTraversal(None, None, Bytecode()).repeat(*args)
  @staticmethod
  def sack(*args):
    return GraphTraversal(None, None, Bytecode()).sack(*args)
  @staticmethod
  def sample(*args):
    return GraphTraversal(None, None, Bytecode()).sample(*args)
  @staticmethod
  def select(*args):
    return GraphTraversal(None, None, Bytecode()).select(*args)
  @staticmethod
  def sideEffect(*args):
    return GraphTraversal(None, None, Bytecode()).sideEffect(*args)
  @staticmethod
  def simplePath(*args):
    return GraphTraversal(None, None, Bytecode()).simplePath(*args)
  @staticmethod
  def start(*args):
    return GraphTraversal(None, None, Bytecode()).start(*args)
  @staticmethod
  def store(*args):
    return GraphTraversal(None, None, Bytecode()).store(*args)
  @staticmethod
  def subgraph(*args):
    return GraphTraversal(None, None, Bytecode()).subgraph(*args)
  @staticmethod
  def sum(*args):
    return GraphTraversal(None, None, Bytecode()).sum(*args)
  @staticmethod
  def tail(*args):
    return GraphTraversal(None, None, Bytecode()).tail(*args)
  @staticmethod
  def timeLimit(*args):
    return GraphTraversal(None, None, Bytecode()).timeLimit(*args)
  @staticmethod
  def times(*args):
    return GraphTraversal(None, None, Bytecode()).times(*args)
  @staticmethod
  def to(*args):
    return GraphTraversal(None, None, Bytecode()).to(*args)
  @staticmethod
  def toE(*args):
    return GraphTraversal(None, None, Bytecode()).toE(*args)
  @staticmethod
  def toV(*args):
    return GraphTraversal(None, None, Bytecode()).toV(*args)
  @staticmethod
  def tree(*args):
    return GraphTraversal(None, None, Bytecode()).tree(*args)
  @staticmethod
  def unfold(*args):
    return GraphTraversal(None, None, Bytecode()).unfold(*args)
  @staticmethod
  def union(*args):
    return GraphTraversal(None, None, Bytecode()).union(*args)
  @staticmethod
  def until(*args):
    return GraphTraversal(None, None, Bytecode()).until(*args)
  @staticmethod
  def value(*args):
    return GraphTraversal(None, None, Bytecode()).value(*args)
  @staticmethod
  def valueMap(*args):
    return GraphTraversal(None, None, Bytecode()).valueMap(*args)
  @staticmethod
  def values(*args):
    return GraphTraversal(None, None, Bytecode()).values(*args)
  @staticmethod
  def where(*args):
    return GraphTraversal(None, None, Bytecode()).where(*args)


def V(*args):
      return __.V(*args)

statics.add_static('V', V)

def _and(*args):
      return __._and(*args)

statics.add_static('_and', _and)

def _as(*args):
      return __._as(*args)

statics.add_static('_as', _as)

def _in(*args):
      return __._in(*args)

statics.add_static('_in', _in)

def _is(*args):
      return __._is(*args)

statics.add_static('_is', _is)

def _not(*args):
      return __._not(*args)

statics.add_static('_not', _not)

def _or(*args):
      return __._or(*args)

statics.add_static('_or', _or)

def addE(*args):
      return __.addE(*args)

statics.add_static('addE', addE)

def addInE(*args):
      return __.addInE(*args)

statics.add_static('addInE', addInE)

def addOutE(*args):
      return __.addOutE(*args)

statics.add_static('addOutE', addOutE)

def addV(*args):
      return __.addV(*args)

statics.add_static('addV', addV)

def aggregate(*args):
      return __.aggregate(*args)

statics.add_static('aggregate', aggregate)

def barrier(*args):
      return __.barrier(*args)

statics.add_static('barrier', barrier)

def both(*args):
      return __.both(*args)

statics.add_static('both', both)

def bothE(*args):
      return __.bothE(*args)

statics.add_static('bothE', bothE)

def bothV(*args):
      return __.bothV(*args)

statics.add_static('bothV', bothV)

def branch(*args):
      return __.branch(*args)

statics.add_static('branch', branch)

def cap(*args):
      return __.cap(*args)

statics.add_static('cap', cap)

def choose(*args):
      return __.choose(*args)

statics.add_static('choose', choose)

def coalesce(*args):
      return __.coalesce(*args)

statics.add_static('coalesce', coalesce)

def coin(*args):
      return __.coin(*args)

statics.add_static('coin', coin)

def constant(*args):
      return __.constant(*args)

statics.add_static('constant', constant)

def count(*args):
      return __.count(*args)

statics.add_static('count', count)

def cyclicPath(*args):
      return __.cyclicPath(*args)

statics.add_static('cyclicPath', cyclicPath)

def dedup(*args):
      return __.dedup(*args)

statics.add_static('dedup', dedup)

def drop(*args):
      return __.drop(*args)

statics.add_static('drop', drop)

def emit(*args):
      return __.emit(*args)

statics.add_static('emit', emit)

def filter(*args):
      return __.filter(*args)

statics.add_static('filter', filter)

def flatMap(*args):
      return __.flatMap(*args)

statics.add_static('flatMap', flatMap)

def fold(*args):
      return __.fold(*args)

statics.add_static('fold', fold)

def group(*args):
      return __.group(*args)

statics.add_static('group', group)

def groupCount(*args):
      return __.groupCount(*args)

statics.add_static('groupCount', groupCount)

def groupV3d0(*args):
      return __.groupV3d0(*args)

statics.add_static('groupV3d0', groupV3d0)

def has(*args):
      return __.has(*args)

statics.add_static('has', has)

def hasId(*args):
      return __.hasId(*args)

statics.add_static('hasId', hasId)

def hasKey(*args):
      return __.hasKey(*args)

statics.add_static('hasKey', hasKey)

def hasLabel(*args):
      return __.hasLabel(*args)

statics.add_static('hasLabel', hasLabel)

def hasNot(*args):
      return __.hasNot(*args)

statics.add_static('hasNot', hasNot)

def hasValue(*args):
      return __.hasValue(*args)

statics.add_static('hasValue', hasValue)

def id(*args):
      return __.id(*args)

statics.add_static('id', id)

def identity(*args):
      return __.identity(*args)

statics.add_static('identity', identity)

def inE(*args):
      return __.inE(*args)

statics.add_static('inE', inE)

def inV(*args):
      return __.inV(*args)

statics.add_static('inV', inV)

def inject(*args):
      return __.inject(*args)

statics.add_static('inject', inject)

def key(*args):
      return __.key(*args)

statics.add_static('key', key)

def label(*args):
      return __.label(*args)

statics.add_static('label', label)

def limit(*args):
      return __.limit(*args)

statics.add_static('limit', limit)

def local(*args):
      return __.local(*args)

statics.add_static('local', local)

def loops(*args):
      return __.loops(*args)

statics.add_static('loops', loops)

def map(*args):
      return __.map(*args)

statics.add_static('map', map)

def mapKeys(*args):
      return __.mapKeys(*args)

statics.add_static('mapKeys', mapKeys)

def mapValues(*args):
      return __.mapValues(*args)

statics.add_static('mapValues', mapValues)

def match(*args):
      return __.match(*args)

statics.add_static('match', match)

def max(*args):
      return __.max(*args)

statics.add_static('max', max)

def mean(*args):
      return __.mean(*args)

statics.add_static('mean', mean)

def min(*args):
      return __.min(*args)

statics.add_static('min', min)

def optional(*args):
      return __.optional(*args)

statics.add_static('optional', optional)

def order(*args):
      return __.order(*args)

statics.add_static('order', order)

def otherV(*args):
      return __.otherV(*args)

statics.add_static('otherV', otherV)

def out(*args):
      return __.out(*args)

statics.add_static('out', out)

def outE(*args):
      return __.outE(*args)

statics.add_static('outE', outE)

def outV(*args):
      return __.outV(*args)

statics.add_static('outV', outV)

def path(*args):
      return __.path(*args)

statics.add_static('path', path)

def project(*args):
      return __.project(*args)

statics.add_static('project', project)

def properties(*args):
      return __.properties(*args)

statics.add_static('properties', properties)

def property(*args):
      return __.property(*args)

statics.add_static('property', property)

def propertyMap(*args):
      return __.propertyMap(*args)

statics.add_static('propertyMap', propertyMap)

def range(*args):
      return __.range(*args)

statics.add_static('range', range)

def repeat(*args):
      return __.repeat(*args)

statics.add_static('repeat', repeat)

def sack(*args):
      return __.sack(*args)

statics.add_static('sack', sack)

def sample(*args):
      return __.sample(*args)

statics.add_static('sample', sample)

def select(*args):
      return __.select(*args)

statics.add_static('select', select)

def sideEffect(*args):
      return __.sideEffect(*args)

statics.add_static('sideEffect', sideEffect)

def simplePath(*args):
      return __.simplePath(*args)

statics.add_static('simplePath', simplePath)

def start(*args):
      return __.start(*args)

statics.add_static('start', start)

def store(*args):
      return __.store(*args)

statics.add_static('store', store)

def subgraph(*args):
      return __.subgraph(*args)

statics.add_static('subgraph', subgraph)

def sum(*args):
      return __.sum(*args)

statics.add_static('sum', sum)

def tail(*args):
      return __.tail(*args)

statics.add_static('tail', tail)

def timeLimit(*args):
      return __.timeLimit(*args)

statics.add_static('timeLimit', timeLimit)

def times(*args):
      return __.times(*args)

statics.add_static('times', times)

def to(*args):
      return __.to(*args)

statics.add_static('to', to)

def toE(*args):
      return __.toE(*args)

statics.add_static('toE', toE)

def toV(*args):
      return __.toV(*args)

statics.add_static('toV', toV)

def tree(*args):
      return __.tree(*args)

statics.add_static('tree', tree)

def unfold(*args):
      return __.unfold(*args)

statics.add_static('unfold', unfold)

def union(*args):
      return __.union(*args)

statics.add_static('union', union)

def until(*args):
      return __.until(*args)

statics.add_static('until', until)

def value(*args):
      return __.value(*args)

statics.add_static('value', value)

def valueMap(*args):
      return __.valueMap(*args)

statics.add_static('valueMap', valueMap)

def values(*args):
      return __.values(*args)

statics.add_static('values', values)

def where(*args):
      return __.where(*args)

statics.add_static('where', where)
