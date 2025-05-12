# SpellcheckCollationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collation_query** | **str** |  | [optional] 
**hits** | **int** |  | [optional] 
**misspellings_and_corrections** | **List[str]** |  | [optional] 

## Example

```python
from pdok_api_client.models.spellcheck_collations_inner import SpellcheckCollationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SpellcheckCollationsInner from a JSON string
spellcheck_collations_inner_instance = SpellcheckCollationsInner.from_json(json)
# print the JSON string representation of the object
print(SpellcheckCollationsInner.to_json())

# convert the object into a dict
spellcheck_collations_inner_dict = spellcheck_collations_inner_instance.to_dict()
# create an instance of SpellcheckCollationsInner from a dict
spellcheck_collations_inner_from_dict = SpellcheckCollationsInner.from_dict(spellcheck_collations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


