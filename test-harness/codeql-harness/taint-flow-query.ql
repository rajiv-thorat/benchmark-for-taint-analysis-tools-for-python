/**
 * @name Empty scope
 * @kind problem
 * @problem.severity warning
 * @id python/example/empty-scope
 */
import python
import semmle.python.dataflow.new.TaintTracking
import semmle.python.ApiGraphs

class EnvironmentToFileConfiguration extends DataFlow::Configuration {
  EnvironmentToFileConfiguration() { this = "EnvironmentToFileConfiguration" }

  override predicate isSource(DataFlow::Node source) {
    source = API::moduleImport("os").getMember("getenv").getACall()
  }

  override predicate isSink(DataFlow::Node sink) {
    exists(DataFlow::CallCfgNode call |
      call = API::moduleImport("os").getMember("open").getACall() and
      sink = call.getArg(0)
    )
  }
}

from Expr environment, Expr fileOpen, EnvironmentToFileConfiguration config
where config.hasFlow(DataFlow::exprNode(environment), DataFlow::exprNode(fileOpen))
select fileOpen, "This call to 'os.open' uses data from $@.",
  environment, "call to 'os.getenv'"