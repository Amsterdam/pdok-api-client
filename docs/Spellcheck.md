# Spellcheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collations** | [**List[SpellcheckCollationsInner]**](SpellcheckCollationsInner.md) |  | [optional] 
**suggestions** | [**List[SpellcheckSuggestionsInner]**](SpellcheckSuggestionsInner.md) |  | [optional] 

## Example

```python
from pdok_api_client.models.spellcheck import Spellcheck

# TODO update the JSON string below
json = "{}"
# create an instance of Spellcheck from a JSON string
spellcheck_instance = Spellcheck.from_json(json)
# print the JSON string representation of the object
print(Spellcheck.to_json())

# convert the object into a dict
spellcheck_dict = spellcheck_instance.to_dict()
# create an instance of Spellcheck from a dict
spellcheck_from_dict = Spellcheck.from_dict(spellcheck_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


