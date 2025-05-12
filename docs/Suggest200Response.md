# Suggest200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**highlighting** | [**Dict[str, HighlightingValue]**](HighlightingValue.md) |  | [optional] 
**response** | [**Response**](Response.md) |  | [optional] 
**spellcheck** | [**Spellcheck**](Spellcheck.md) |  | [optional] 

## Example

```python
from pdok_api_client.models.suggest200_response import Suggest200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Suggest200Response from a JSON string
suggest200_response_instance = Suggest200Response.from_json(json)
# print the JSON string representation of the object
print(Suggest200Response.to_json())

# convert the object into a dict
suggest200_response_dict = suggest200_response_instance.to_dict()
# create an instance of Suggest200Response from a dict
suggest200_response_from_dict = Suggest200Response.from_dict(suggest200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


