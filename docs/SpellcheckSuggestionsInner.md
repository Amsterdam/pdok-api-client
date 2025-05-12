# SpellcheckSuggestionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_offset** | **int** |  | [optional] 
**num_found** | **int** |  | [optional] 
**start_offset** | **int** |  | [optional] 
**suggestion** | **List[str]** |  | [optional] 

## Example

```python
from pdok_api_client.models.spellcheck_suggestions_inner import SpellcheckSuggestionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SpellcheckSuggestionsInner from a JSON string
spellcheck_suggestions_inner_instance = SpellcheckSuggestionsInner.from_json(json)
# print the JSON string representation of the object
print(SpellcheckSuggestionsInner.to_json())

# convert the object into a dict
spellcheck_suggestions_inner_dict = spellcheck_suggestions_inner_instance.to_dict()
# create an instance of SpellcheckSuggestionsInner from a dict
spellcheck_suggestions_inner_from_dict = SpellcheckSuggestionsInner.from_dict(spellcheck_suggestions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


