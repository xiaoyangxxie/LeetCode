<%  
 import java.text.DateFormat  
 import java.text.SimpleDateFormat  
 %>  
 <!-- Robot Framework Results -->  
 <%  
 def robotResults = false  
 def actions = build.actions // List<hudson.model.Action>  
 actions.each() { action ->  
  if( action.class.simpleName.equals("RobotBuildAction") ) { // hudson.plugins.robot.RobotBuildAction  
   robotResults = true %>  
 <p><h4>Robot Framework Results</h4></p>  
 <p><a href="${rooturl}${build.url}robot/report/final-report.html">Detailed Report</a></p>  
 <p>Pass Percentage: <%= action.overallPassPercentage %>%</p>  
 <table cellspacing="0" cellpadding="4" border="1" align="left">  
 <thead>  
 <tr bgcolor="#F3F3F3">  
  <td><b>Test Name</b></td>  
  <td><b>Status</b></td>  
  <td><b>Execution Datetime</b></td>  
 </tr>  
 </thead>  
 <tbody>  
 <% def suites = action.result.allSuites  
   suites.each() { suite ->   
    def currSuite = suite  
    def suiteName = currSuite.displayName  
    // ignore top 2 elements in the structure as they are placeholders  
    while (currSuite.parent != null && currSuite.parent.parent != null) {  
     currSuite = currSuite.parent  
     suiteName = currSuite.displayName + "." + suiteName  
    } %>  
 <tr><td colspan="3"><b><%= suiteName %></b></td></tr>  
 <%  DateFormat format = new SimpleDateFormat("yyyyMMdd HH:mm:ss.SS")
    def execDateTcPairs = []
    suite.caseResults.each() { tc ->  
      Date execDate = format.parse(tc.starttime)
      execDateTcPairs << [execDate, tc]
    }
    // primary sort execDate, secondary displayName
    execDateTcPairs = execDateTcPairs.sort{ a,b -> a[1].displayName <=> b[1].displayName }
    execDateTcPairs = execDateTcPairs.sort{ a,b -> a[0] <=> b[0] }
    execDateTcPairs.each() {
      def execDate = it[0]
      def tc = it[1]  %>
 <tr>  
  <td><%= tc.displayName %></td>  
  <td style="color: <%= tc.isPassed() ? "#66CC00" : "#FF3333" %>"><%= tc.isPassed() ? "PASS" : "FAIL" %></td>  
  <td><%= execDate %></td>  
 </tr>  
 <%  } // tests  
   } // suites %>  
 </tbody></table><%  
  } // robot results  
 }  
 if (!robotResults) { %>  
 <p>No Robot Framework test results found.</p>  
 <%  
 } %>  