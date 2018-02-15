from temboo.Library.Utilities.JSON import GetValuesFromJSON
from temboo.core.session import TembooSession

# Create a session with your Temboo account details
session = TembooSession("accountName", "myFirstApp", "abc123xxxxxxxxxxxxxx")

# Instantiate the Choreo
getValuesFromJSONChoreo = GetValuesFromJSON(session)

# Get an InputSet object for the Choreo
getValuesFromJSONInputs = getValuesFromJSONChoreo.new_input_set()

# Execute the Choreo
getValuesFromJSONResults = getValuesFromJSONChoreo.execute_with_results(getValuesFromJSONInputs)

# Print the Choreo outputs
print("Response: " + getValuesFromJSONResults.get_Response())