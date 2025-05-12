# SpellcheckSuggestionsInnerOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_offset** | **int** |  | [optional] 
**num_found** | **int** |  | [optional] 
**start_offset** | **int** |  | [optional] 
**suggestion** | **List[str]** |  | [optional] 

## Example

```python
from pdok_api_client.models.spellcheck_suggestions_inner_one_of import SpellcheckSuggestionsInnerOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of SpellcheckSuggestionsInnerOneOf from a JSON string
spellcheck_suggestions_inner_one_of_instance = SpellcheckSuggestionsInnerOneOf.from_json(json)
# print the JSON string representation of the object
print(SpellcheckSuggestionsInnerOneOf.to_json())

# convert the object into a dict
spellcheck_suggestions_inner_one_of_dict = spellcheck_suggestions_inner_one_of_instance.to_dict()
# create an instance of SpellcheckSuggestionsInnerOneOf from a dict
spellcheck_suggestions_inner_one_of_from_dict = SpellcheckSuggestionsInnerOneOf.from_dict(spellcheck_suggestions_inner_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


