# SpellcheckCollationsInnerOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collation_query** | **str** |  | [optional] 
**hits** | **int** |  | [optional] 
**misspellings_and_corrections** | **List[str]** |  | [optional] 

## Example

```python
from pdok_api_client.models.spellcheck_collations_inner_one_of import SpellcheckCollationsInnerOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of SpellcheckCollationsInnerOneOf from a JSON string
spellcheck_collations_inner_one_of_instance = SpellcheckCollationsInnerOneOf.from_json(json)
# print the JSON string representation of the object
print(SpellcheckCollationsInnerOneOf.to_json())

# convert the object into a dict
spellcheck_collations_inner_one_of_dict = spellcheck_collations_inner_one_of_instance.to_dict()
# create an instance of SpellcheckCollationsInnerOneOf from a dict
spellcheck_collations_inner_one_of_from_dict = SpellcheckCollationsInnerOneOf.from_dict(spellcheck_collations_inner_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


