# pdok_api_client.LocatieserverApi

All URIs are relative to *https://api.pdok.nl/bzk/locatieserver/search/v3_1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**free**](LocatieserverApi.md#free) | **GET** /free | De Free API biedt de mogelijkheid om vrij te zoeken (klassiek geocoderen), waar zonder tussenkomst van suggesties de API direct resultaten teruggeeft op basis van de zoekopdracht. 
[**lookup**](LocatieserverApi.md#lookup) | **GET** /lookup | Zodra er op basis van suggesties van de Suggest API een keuze is gemaakt, wordt de Lookup API aangeroepen, welke o.a. een (versimpelde) geometrie van de zoekopdracht teruggeeft. 
[**reverse_geocoder**](LocatieserverApi.md#reverse_geocoder) | **GET** /reverse | De Reverse API biedt de mogelijkheid om een locatie (punt geometrie) op te geven om vervolgens verschillende gegevens in een range rondom deze locatie te ontvangen. 
[**suggest**](LocatieserverApi.md#suggest) | **GET** /suggest | De Suggest API biedt de mogelijkheid om een (gedeelte van een) zoekopdracht op te voeren, waarnaar er suggesties teruggegeven worden. 


# **free**
> Free200Response free(q=q, lat=lat, lon=lon, fl=fl, fq=fq, df=df, qf=qf, bq=bq, start=start, rows=rows, sort=sort, wt=wt)

De Free API biedt de mogelijkheid om vrij te zoeken (klassiek geocoderen), waar zonder tussenkomst van suggesties de API direct resultaten teruggeeft op basis van de zoekopdracht. 

### Example


```python
import pdok_api_client
from pdok_api_client.models.free200_response import Free200Response
from pdok_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pdok.nl/bzk/locatieserver/search/v3_1
# See configuration.py for a list of all supported configuration parameters.
configuration = pdok_api_client.Configuration(
    host = "https://api.pdok.nl/bzk/locatieserver/search/v3_1"
)


# Enter a context with an instance of the API client
async with pdok_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdok_api_client.LocatieserverApi(api_client)
    q = 'q_example' # str | Hiermee worden de zoektermen opgegeven. De Solr-syntax voor zoektermen kan hier worden toegepast, bijv. combineren met \"and\", en het gebruik van dubbele quotes voor opeenvolgende zoektermen. Zoektermen mogen incompleet zijn. Ook wordt er gebruik gemaakt van synoniemen.  Voorbeelden: `q=Utrecht`: geeft resultaten terug met de zoekterm Utrecht, bijv. adressen in de stad Utrecht, woonplaatsen en gemeenten in de provincie Utrecht.  `q=\"De Bilt\"`: geeft resultaten terug met de zoekterm De Bilt, bijv. de woonplaats en gemeente De Bilt, of adressen in deze woonplaats. Let op dat bij het daadwerkelijk verzenden van het request onder water de URL-encodingregels toegepast worden, dus een spatie wordt verzonden als een plusteken.  `q=\"Sint Jacob\" Utre`: geeft o.a. adressen terug waarvan er delen achtereenvolgens beginnen met \"Sint\" en \"Jacob\", of met \"St\" (synoniem) en \"Jacob\", en waar ook een deel met \"Utre\" begint. Een voorbeeld is het adres St.-Jacobsstraat 200 (officiële schrijfwijze) in Utrecht.  (optional)
    lat = 3.4 # float | Hiermee kan een coördinaat (in lat/lon, ofwel WGS84) worden opgegeven. Met behulp van deze parameters worden de gevonden zoekresultaten gesorteerd op afstand van het meegegeven punt. Wanneer de locatie van de gebruiker bekend is, kan op deze manier effectiever worden gezocht.  Het meegeven van een coördinaat is met name nuttig voor de suggest- en vrije geocoder-services. Hier worden meestal meerdere resultaten teruggegeven. Als decimaal scheidingsteken moet een punt worden opgegeven i.p.v. een komma.  (optional)
    lon = 3.4 # float | Hiermee kan een coördinaat (in lat/lon, ofwel WGS84) worden opgegeven. Met behulp van deze parameters worden de gevonden zoekresultaten gesorteerd op afstand van het meegegeven punt. Wanneer de locatie van de gebruiker bekend is, kan op deze manier effectiever worden gezocht.  Het meegeven van een coördinaat is met name nuttig voor de suggest- en vrije geocoder-services. Hier worden meestal meerdere resultaten teruggegeven. Als decimaal scheidingsteken moet een punt worden opgegeven i.p.v. een komma.  Voorbeeld: `lat=52.09&lon=5.12`  De resultaten worden gesorteerd op afstand van een bepaald punt in het centrum van Utrecht.  (optional)
    fl = 'id identificatie weergavenaam bron type openbareruimte_id nwb_id openbareruimtetype straatnaam straatnaam_verkort adresseerbaarobject_id nummeraanduiding_id huisnummer huisletter huisnummertoevoeging huis_nlt postcode buurtnaam buurtcode wijknaam wijkcode woonplaatscode woonplaatsnaam gemeentecode gemeentenaam provinciecode provincienaam provincieafkorting kadastrale_gemeentecode kadastrale_gemeentenaam kadastrale_sectie perceelnummer kadastrale_grootte gekoppeld_perceel kadastrale_aanduiding volgnummer gekoppeld_appartement wegnummer hectometernummer zijde hectometerletter waterschapsnaam waterschapscode rdf_seealso centroide_ll centroide_rd score' # str | Hiermee worden de velden opgegeven die teruggegeven dienen te worden. (optional) (default to 'id identificatie weergavenaam bron type openbareruimte_id nwb_id openbareruimtetype straatnaam straatnaam_verkort adresseerbaarobject_id nummeraanduiding_id huisnummer huisletter huisnummertoevoeging huis_nlt postcode buurtnaam buurtcode wijknaam wijkcode woonplaatscode woonplaatsnaam gemeentecode gemeentenaam provinciecode provincienaam provincieafkorting kadastrale_gemeentecode kadastrale_gemeentenaam kadastrale_sectie perceelnummer kadastrale_grootte gekoppeld_perceel kadastrale_aanduiding volgnummer gekoppeld_appartement wegnummer hectometernummer zijde hectometerletter waterschapsnaam waterschapscode rdf_seealso centroide_ll centroide_rd score')
    fq = ["type:(gemeente OR woonplaats OR weg OR postcode OR adres)"] # List[str] | Hiermee kan een filter query worden opgegeven, bijv. `fq=bron:BAG`. (optional) (default to ["type:(gemeente OR woonplaats OR weg OR postcode OR adres)"])
    df = 'tekst' # str | Hiermee wordt het default zoekveld opgegeven. Dit is het veld waar standaard in gezocht wordt, wanneer de veldnaam niet wordt meegegeven.  (optional) (default to 'tekst')
    qf = 'qf_example' # str | Met behulp van deze parameter kan aan bepaalde _velden_ een extra boost worden meegegeven. Hiermee kan de scoreberekening worden aangepast.  (optional)
    bq = ["type:provincie^1.5","type:gemeente^1.5","type:woonplaats^1.5","type:weg^1.5","type:postcode^0.5","type:adres^1"] # List[str] | Met behulp van deze parameter kan aan bepaalde _veldwaarden_ een extra boost worden meegegeven. Ook hiermee kan de scoreberekening worden aangepast.  Voor elke boost query moet een aparte `bq=<boost>` worden gebruikt. Bijvoorbeeld: `bq=type:gemeente^1.5&bq=type:woonplaats^1.5`.  (optional) (default to ["type:provincie^1.5","type:gemeente^1.5","type:woonplaats^1.5","type:weg^1.5","type:postcode^0.5","type:adres^1"])
    start = 0 # int | Hiermee wordt opgegeven wat de index is van het eerste resultaat dat teruggegeven wordt. Dit is zero-based. In combinatie met de rows-parameter kunnen deze services gepagineerd worden bevraagd. Het maximum is \"10.000\".  (optional) (default to 0)
    rows = 10 # int | Hiermee wordt opgegeven wat het maximale aantal rijen (ofwel resultaten) is dat teruggegeven moet worden op deze bevraging. Het maximum is \"100\".  (optional) (default to 10)
    sort = 'score desc,sortering asc,weergavenaam asc' # str | Hiermee kan worden opgegeven hoe de sortering plaatsvindt. (optional) (default to 'score desc,sortering asc,weergavenaam asc')
    wt = json # str | Hiermee wordt opgegeven wat het outputformaat is van de bevraging. (optional) (default to json)

    try:
        # De Free API biedt de mogelijkheid om vrij te zoeken (klassiek geocoderen), waar zonder tussenkomst van suggesties de API direct resultaten teruggeeft op basis van de zoekopdracht. 
        api_response = await api_instance.free(q=q, lat=lat, lon=lon, fl=fl, fq=fq, df=df, qf=qf, bq=bq, start=start, rows=rows, sort=sort, wt=wt)
        print("The response of LocatieserverApi->free:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocatieserverApi->free: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Hiermee worden de zoektermen opgegeven. De Solr-syntax voor zoektermen kan hier worden toegepast, bijv. combineren met \&quot;and\&quot;, en het gebruik van dubbele quotes voor opeenvolgende zoektermen. Zoektermen mogen incompleet zijn. Ook wordt er gebruik gemaakt van synoniemen.  Voorbeelden: &#x60;q&#x3D;Utrecht&#x60;: geeft resultaten terug met de zoekterm Utrecht, bijv. adressen in de stad Utrecht, woonplaatsen en gemeenten in de provincie Utrecht.  &#x60;q&#x3D;\&quot;De Bilt\&quot;&#x60;: geeft resultaten terug met de zoekterm De Bilt, bijv. de woonplaats en gemeente De Bilt, of adressen in deze woonplaats. Let op dat bij het daadwerkelijk verzenden van het request onder water de URL-encodingregels toegepast worden, dus een spatie wordt verzonden als een plusteken.  &#x60;q&#x3D;\&quot;Sint Jacob\&quot; Utre&#x60;: geeft o.a. adressen terug waarvan er delen achtereenvolgens beginnen met \&quot;Sint\&quot; en \&quot;Jacob\&quot;, of met \&quot;St\&quot; (synoniem) en \&quot;Jacob\&quot;, en waar ook een deel met \&quot;Utre\&quot; begint. Een voorbeeld is het adres St.-Jacobsstraat 200 (officiële schrijfwijze) in Utrecht.  | [optional] 
 **lat** | **float**| Hiermee kan een coördinaat (in lat/lon, ofwel WGS84) worden opgegeven. Met behulp van deze parameters worden de gevonden zoekresultaten gesorteerd op afstand van het meegegeven punt. Wanneer de locatie van de gebruiker bekend is, kan op deze manier effectiever worden gezocht.  Het meegeven van een coördinaat is met name nuttig voor de suggest- en vrije geocoder-services. Hier worden meestal meerdere resultaten teruggegeven. Als decimaal scheidingsteken moet een punt worden opgegeven i.p.v. een komma.  | [optional] 
 **lon** | **float**| Hiermee kan een coördinaat (in lat/lon, ofwel WGS84) worden opgegeven. Met behulp van deze parameters worden de gevonden zoekresultaten gesorteerd op afstand van het meegegeven punt. Wanneer de locatie van de gebruiker bekend is, kan op deze manier effectiever worden gezocht.  Het meegeven van een coördinaat is met name nuttig voor de suggest- en vrije geocoder-services. Hier worden meestal meerdere resultaten teruggegeven. Als decimaal scheidingsteken moet een punt worden opgegeven i.p.v. een komma.  Voorbeeld: &#x60;lat&#x3D;52.09&amp;lon&#x3D;5.12&#x60;  De resultaten worden gesorteerd op afstand van een bepaald punt in het centrum van Utrecht.  | [optional] 
 **fl** | **str**| Hiermee worden de velden opgegeven die teruggegeven dienen te worden. | [optional] [default to &#39;id identificatie weergavenaam bron type openbareruimte_id nwb_id openbareruimtetype straatnaam straatnaam_verkort adresseerbaarobject_id nummeraanduiding_id huisnummer huisletter huisnummertoevoeging huis_nlt postcode buurtnaam buurtcode wijknaam wijkcode woonplaatscode woonplaatsnaam gemeentecode gemeentenaam provinciecode provincienaam provincieafkorting kadastrale_gemeentecode kadastrale_gemeentenaam kadastrale_sectie perceelnummer kadastrale_grootte gekoppeld_perceel kadastrale_aanduiding volgnummer gekoppeld_appartement wegnummer hectometernummer zijde hectometerletter waterschapsnaam waterschapscode rdf_seealso centroide_ll centroide_rd score&#39;]
 **fq** | [**List[str]**](str.md)| Hiermee kan een filter query worden opgegeven, bijv. &#x60;fq&#x3D;bron:BAG&#x60;. | [optional] [default to [&quot;type:(gemeente OR woonplaats OR weg OR postcode OR adres)&quot;]]
 **df** | **str**| Hiermee wordt het default zoekveld opgegeven. Dit is het veld waar standaard in gezocht wordt, wanneer de veldnaam niet wordt meegegeven.  | [optional] [default to &#39;tekst&#39;]
 **qf** | **str**| Met behulp van deze parameter kan aan bepaalde _velden_ een extra boost worden meegegeven. Hiermee kan de scoreberekening worden aangepast.  | [optional] 
 **bq** | [**List[str]**](str.md)| Met behulp van deze parameter kan aan bepaalde _veldwaarden_ een extra boost worden meegegeven. Ook hiermee kan de scoreberekening worden aangepast.  Voor elke boost query moet een aparte &#x60;bq&#x3D;&lt;boost&gt;&#x60; worden gebruikt. Bijvoorbeeld: &#x60;bq&#x3D;type:gemeente^1.5&amp;bq&#x3D;type:woonplaats^1.5&#x60;.  | [optional] [default to [&quot;type:provincie^1.5&quot;,&quot;type:gemeente^1.5&quot;,&quot;type:woonplaats^1.5&quot;,&quot;type:weg^1.5&quot;,&quot;type:postcode^0.5&quot;,&quot;type:adres^1&quot;]]
 **start** | **int**| Hiermee wordt opgegeven wat de index is van het eerste resultaat dat teruggegeven wordt. Dit is zero-based. In combinatie met de rows-parameter kunnen deze services gepagineerd worden bevraagd. Het maximum is \&quot;10.000\&quot;.  | [optional] [default to 0]
 **rows** | **int**| Hiermee wordt opgegeven wat het maximale aantal rijen (ofwel resultaten) is dat teruggegeven moet worden op deze bevraging. Het maximum is \&quot;100\&quot;.  | [optional] [default to 10]
 **sort** | **str**| Hiermee kan worden opgegeven hoe de sortering plaatsvindt. | [optional] [default to &#39;score desc,sortering asc,weergavenaam asc&#39;]
 **wt** | **str**| Hiermee wordt opgegeven wat het outputformaat is van de bevraging. | [optional] [default to json]

### Return type

[**Free200Response**](Free200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookup**
> Free200Response lookup(id, fl=fl, fq=fq, wt=wt)

Zodra er op basis van suggesties van de Suggest API een keuze is gemaakt, wordt de Lookup API aangeroepen, welke o.a. een (versimpelde) geometrie van de zoekopdracht teruggeeft. 

### Example


```python
import pdok_api_client
from pdok_api_client.models.free200_response import Free200Response
from pdok_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pdok.nl/bzk/locatieserver/search/v3_1
# See configuration.py for a list of all supported configuration parameters.
configuration = pdok_api_client.Configuration(
    host = "https://api.pdok.nl/bzk/locatieserver/search/v3_1"
)


# Enter a context with an instance of the API client
async with pdok_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdok_api_client.LocatieserverApi(api_client)
    id = 'id_example' # str | Hiermee wordt het object-ID opgegeven.
    fl = 'id identificatie weergavenaam bron type openbareruimte_id nwb_id openbareruimtetype straatnaam straatnaam_verkort adresseerbaarobject_id nummeraanduiding_id huisnummer huisletter huisnummertoevoeging huis_nlt postcode buurtnaam buurtcode wijknaam wijkcode woonplaatscode woonplaatsnaam gemeentecode gemeentenaam provinciecode provincienaam provincieafkorting kadastrale_gemeentecode kadastrale_gemeentenaam kadastrale_sectie perceelnummer kadastrale_grootte gekoppeld_perceel volgnummer gekoppeld_appartement kadastrale_aanduiding wegnummer hectometernummer zijde hectometerletter waterschapsnaam waterschapscode rdf_seealso centroide_ll centroide_rd' # str | Hiermee worden de velden opgegeven die teruggegeven dienen te worden. (optional) (default to 'id identificatie weergavenaam bron type openbareruimte_id nwb_id openbareruimtetype straatnaam straatnaam_verkort adresseerbaarobject_id nummeraanduiding_id huisnummer huisletter huisnummertoevoeging huis_nlt postcode buurtnaam buurtcode wijknaam wijkcode woonplaatscode woonplaatsnaam gemeentecode gemeentenaam provinciecode provincienaam provincieafkorting kadastrale_gemeentecode kadastrale_gemeentenaam kadastrale_sectie perceelnummer kadastrale_grootte gekoppeld_perceel volgnummer gekoppeld_appartement kadastrale_aanduiding wegnummer hectometernummer zijde hectometerletter waterschapsnaam waterschapscode rdf_seealso centroide_ll centroide_rd')
    fq = ['fq_example'] # List[str] | Hiermee kan een filter query worden opgegeven, bijv. `fq=bron:BAG`. (optional)
    wt = json # str | Hiermee wordt opgegeven wat het outputformaat is van de bevraging. (optional) (default to json)

    try:
        # Zodra er op basis van suggesties van de Suggest API een keuze is gemaakt, wordt de Lookup API aangeroepen, welke o.a. een (versimpelde) geometrie van de zoekopdracht teruggeeft. 
        api_response = await api_instance.lookup(id, fl=fl, fq=fq, wt=wt)
        print("The response of LocatieserverApi->lookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocatieserverApi->lookup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Hiermee wordt het object-ID opgegeven. | 
 **fl** | **str**| Hiermee worden de velden opgegeven die teruggegeven dienen te worden. | [optional] [default to &#39;id identificatie weergavenaam bron type openbareruimte_id nwb_id openbareruimtetype straatnaam straatnaam_verkort adresseerbaarobject_id nummeraanduiding_id huisnummer huisletter huisnummertoevoeging huis_nlt postcode buurtnaam buurtcode wijknaam wijkcode woonplaatscode woonplaatsnaam gemeentecode gemeentenaam provinciecode provincienaam provincieafkorting kadastrale_gemeentecode kadastrale_gemeentenaam kadastrale_sectie perceelnummer kadastrale_grootte gekoppeld_perceel volgnummer gekoppeld_appartement kadastrale_aanduiding wegnummer hectometernummer zijde hectometerletter waterschapsnaam waterschapscode rdf_seealso centroide_ll centroide_rd&#39;]
 **fq** | [**List[str]**](str.md)| Hiermee kan een filter query worden opgegeven, bijv. &#x60;fq&#x3D;bron:BAG&#x60;. | [optional] 
 **wt** | **str**| Hiermee wordt opgegeven wat het outputformaat is van de bevraging. | [optional] [default to json]

### Return type

[**Free200Response**](Free200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reverse_geocoder**
> Free200Response reverse_geocoder(x=x, y=y, lat=lat, lon=lon, type=type, distance=distance, fl=fl, fq=fq, start=start, rows=rows, wt=wt)

De Reverse API biedt de mogelijkheid om een locatie (punt geometrie) op te geven om vervolgens verschillende gegevens in een range rondom deze locatie te ontvangen. 

### Example


```python
import pdok_api_client
from pdok_api_client.models.free200_response import Free200Response
from pdok_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pdok.nl/bzk/locatieserver/search/v3_1
# See configuration.py for a list of all supported configuration parameters.
configuration = pdok_api_client.Configuration(
    host = "https://api.pdok.nl/bzk/locatieserver/search/v3_1"
)


# Enter a context with an instance of the API client
async with pdok_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdok_api_client.LocatieserverApi(api_client)
    x = 194195.304 # float | Hiermee wordt het coördinaat in X/Y (RD), of in lat/lon (WGS84) opgegeven. Vanaf dit coördinaat gaat de reverse geocoder zoeken.  (optional)
    y = 465885.902 # float | Hiermee wordt het coördinaat in X/Y (RD), of in lat/lon (WGS84) opgegeven. Vanaf dit coördinaat gaat de reverse geocoder zoeken.  (optional)
    lat = 3.4 # float | Hiermee wordt het coördinaat in X/Y (RD), of in lat/lon (WGS84) opgegeven. Vanaf dit coördinaat gaat de reverse geocoder zoeken.  (optional)
    lon = 3.4 # float | Hiermee wordt het coördinaat in X/Y (RD), of in lat/lon (WGS84) opgegeven. Vanaf dit coördinaat gaat de reverse geocoder zoeken.  (optional)
    type = 'adres' # str | Hiermee kan worden opgegeven welke resultaat types je terug krijgt in het resultaat. Voor elke type dat je wilt terugkrijgen moet je een aparte type parameter toevoegen, bijv. `type=adres&type=gemeente&type=perceel`. Met `type=*` krijg je alle types terug. Deze wordt voor het bepalen van de resultaten gebruikt en heeft dus geen invloed op aantal resultaten dat wordt teruggegeven.  (optional) (default to 'adres')
    distance = 56 # int | Hiermee kan een maximale zoekstraal in meters worden opgegeven. Er zullen dan geen resultaten worden teruggegeven die verder liggen dan deze waarden.  (optional)
    fl = 'id type weergavenaam score afstand' # str | Hiermee worden de velden opgegeven die teruggegeven dienen te worden. (optional) (default to 'id type weergavenaam score afstand')
    fq = '' # str | Hiermee kan een filter query worden opgegeven, bijv. `fq=bron:BAG`. Deze wordt uitgevoerd nadat de dichtsbijzijnde resultaten zijn gevonden, dus resultaten die hier niet aan voldoen worden weggefilterd waardoor je minder resultaten dan het aantal rows kan terugkrijgen.  (optional)
    start = 0 # int | Hiermee wordt opgegeven wat de index is van het eerste resultaat dat teruggegeven wordt. Dit is zero-based. In combinatie met de rows-parameter kunnen deze services gepagineerd worden bevraagd. Het maximum is \"10.000\".  (optional) (default to 0)
    rows = 10 # int | Hiermee wordt opgegeven wat het maximale aantal rijen (ofwel resultaten) is dat teruggegeven moet worden op deze bevraging. Het maximum is \"100\".  (optional) (default to 10)
    wt = json # str | Hiermee wordt opgegeven wat het outputformaat is van de bevraging. (optional) (default to json)

    try:
        # De Reverse API biedt de mogelijkheid om een locatie (punt geometrie) op te geven om vervolgens verschillende gegevens in een range rondom deze locatie te ontvangen. 
        api_response = await api_instance.reverse_geocoder(x=x, y=y, lat=lat, lon=lon, type=type, distance=distance, fl=fl, fq=fq, start=start, rows=rows, wt=wt)
        print("The response of LocatieserverApi->reverse_geocoder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocatieserverApi->reverse_geocoder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x** | **float**| Hiermee wordt het coördinaat in X/Y (RD), of in lat/lon (WGS84) opgegeven. Vanaf dit coördinaat gaat de reverse geocoder zoeken.  | [optional] 
 **y** | **float**| Hiermee wordt het coördinaat in X/Y (RD), of in lat/lon (WGS84) opgegeven. Vanaf dit coördinaat gaat de reverse geocoder zoeken.  | [optional] 
 **lat** | **float**| Hiermee wordt het coördinaat in X/Y (RD), of in lat/lon (WGS84) opgegeven. Vanaf dit coördinaat gaat de reverse geocoder zoeken.  | [optional] 
 **lon** | **float**| Hiermee wordt het coördinaat in X/Y (RD), of in lat/lon (WGS84) opgegeven. Vanaf dit coördinaat gaat de reverse geocoder zoeken.  | [optional] 
 **type** | **str**| Hiermee kan worden opgegeven welke resultaat types je terug krijgt in het resultaat. Voor elke type dat je wilt terugkrijgen moet je een aparte type parameter toevoegen, bijv. &#x60;type&#x3D;adres&amp;type&#x3D;gemeente&amp;type&#x3D;perceel&#x60;. Met &#x60;type&#x3D;*&#x60; krijg je alle types terug. Deze wordt voor het bepalen van de resultaten gebruikt en heeft dus geen invloed op aantal resultaten dat wordt teruggegeven.  | [optional] [default to &#39;adres&#39;]
 **distance** | **int**| Hiermee kan een maximale zoekstraal in meters worden opgegeven. Er zullen dan geen resultaten worden teruggegeven die verder liggen dan deze waarden.  | [optional] 
 **fl** | **str**| Hiermee worden de velden opgegeven die teruggegeven dienen te worden. | [optional] [default to &#39;id type weergavenaam score afstand&#39;]
 **fq** | **str**| Hiermee kan een filter query worden opgegeven, bijv. &#x60;fq&#x3D;bron:BAG&#x60;. Deze wordt uitgevoerd nadat de dichtsbijzijnde resultaten zijn gevonden, dus resultaten die hier niet aan voldoen worden weggefilterd waardoor je minder resultaten dan het aantal rows kan terugkrijgen.  | [optional] 
 **start** | **int**| Hiermee wordt opgegeven wat de index is van het eerste resultaat dat teruggegeven wordt. Dit is zero-based. In combinatie met de rows-parameter kunnen deze services gepagineerd worden bevraagd. Het maximum is \&quot;10.000\&quot;.  | [optional] [default to 0]
 **rows** | **int**| Hiermee wordt opgegeven wat het maximale aantal rijen (ofwel resultaten) is dat teruggegeven moet worden op deze bevraging. Het maximum is \&quot;100\&quot;.  | [optional] [default to 10]
 **wt** | **str**| Hiermee wordt opgegeven wat het outputformaat is van de bevraging. | [optional] [default to json]

### Return type

[**Free200Response**](Free200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suggest**
> Suggest200Response suggest(q, lat=lat, lon=lon, fl=fl, fq=fq, qf=qf, bq=bq, start=start, rows=rows, sort=sort, wt=wt)

De Suggest API biedt de mogelijkheid om een (gedeelte van een) zoekopdracht op te voeren, waarnaar er suggesties teruggegeven worden. 

### Example


```python
import pdok_api_client
from pdok_api_client.models.suggest200_response import Suggest200Response
from pdok_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pdok.nl/bzk/locatieserver/search/v3_1
# See configuration.py for a list of all supported configuration parameters.
configuration = pdok_api_client.Configuration(
    host = "https://api.pdok.nl/bzk/locatieserver/search/v3_1"
)


# Enter a context with an instance of the API client
async with pdok_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pdok_api_client.LocatieserverApi(api_client)
    q = 'q_example' # str | Hiermee worden de zoektermen opgegeven. De Solr-syntax voor zoektermen kan hier worden toegepast, bijv. combineren met \"and\", en het gebruik van dubbele quotes voor opeenvolgende zoektermen. Zoektermen mogen incompleet zijn. Ook wordt er gebruik gemaakt van synoniemen.  Voorbeelden: `q=Utrecht`: geeft resultaten terug met de zoekterm Utrecht, bijv. adressen in de stad Utrecht, woonplaatsen en gemeenten in de provincie Utrecht.  `q=\"De Bilt\"`: geeft resultaten terug met de zoekterm De Bilt, bijv. de woonplaats en gemeente De Bilt, of adressen in deze woonplaats. Let op dat bij het daadwerkelijk verzenden van het request onder water de URL-encodingregels toegepast worden, dus een spatie wordt verzonden als een plusteken.  `q=\"Sint Jacob\" Utre`: geeft o.a. adressen terug waarvan er delen achtereenvolgens beginnen met \"Sint\" en \"Jacob\", of met \"St\" (synoniem) en \"Jacob\", en waar ook een deel met \"Utre\" begint. Een voorbeeld is het adres St.-Jacobsstraat 200 (officiële schrijfwijze) in Utrecht. 
    lat = 3.4 # float | Hiermee kan een coördinaat (in lat/lon, ofwel WGS84) worden opgegeven. Met behulp van deze parameters worden de gevonden zoekresultaten gesorteerd op afstand van het meegegeven punt. Wanneer de locatie van de gebruiker bekend is, kan op deze manier effectiever worden gezocht.  Het meegeven van een coördinaat is met name nuttig voor de suggest- en vrije geocoder-services. Hier worden meestal meerdere resultaten teruggegeven. Als decimaal scheidingsteken moet een punt worden opgegeven i.p.v. een komma.  Voorbeeld: `lat=52.09&lon=5.12`  De resultaten worden gesorteerd op afstand van een bepaald punt in het centrum van Utrecht.  (optional)
    lon = 3.4 # float | Hiermee kan een coördinaat (in lat/lon, ofwel WGS84) worden opgegeven. Met behulp van deze parameters worden de gevonden zoekresultaten gesorteerd op afstand van het meegegeven punt. Wanneer de locatie van de gebruiker bekend is, kan op deze manier effectiever worden gezocht.  Het meegeven van een coördinaat is met name nuttig voor de suggest- en vrije geocoder-services. Hier worden meestal meerdere resultaten teruggegeven. Als decimaal scheidingsteken moet een punt worden opgegeven i.p.v. een komma.  Voorbeeld: `lat=52.09&lon=5.12`  De resultaten worden gesorteerd op afstand van een bepaald punt in het centrum van Utrecht.  (optional)
    fl = 'id weergavenaam type score adrestype' # str | Hiermee worden de velden opgegeven die teruggegeven dienen te worden. (optional) (default to 'id weergavenaam type score adrestype')
    fq = ["type:(gemeente OR woonplaats OR weg OR postcode OR adres)"] # List[str] | Hiermee kan een filter query worden opgegeven, bijv. `fq=bron:BAG`. (optional) (default to ["type:(gemeente OR woonplaats OR weg OR postcode OR adres)"])
    qf = 'exacte_match^1 suggest^0.5 huisnummer^0.5 huisletter^0.5 huisnummertoevoeging^0.5' # str | Met behulp van deze parameter kan aan bepaalde _velden_ een extra boost worden meegegeven. Hiermee kan de scoreberekening worden aangepast.  (optional) (default to 'exacte_match^1 suggest^0.5 huisnummer^0.5 huisletter^0.5 huisnummertoevoeging^0.5')
    bq = ["type:provincie^1.5","type:gemeente^1.5","type:woonplaats^1.5","type:weg^1.5","type:postcode^0.6","type:adres^1"] # List[str] | Met behulp van deze parameter kan aan bepaalde _veldwaarden_ een extra boost worden meegegeven. Ook hiermee kan de scoreberekening worden aangepast.  Voor elke boost query moet een aparte `bq=<boost>` worden gebruikt. Bijvoorbeeld: `bq=type:gemeente^1.5&bq=type:woonplaats^1.5`.  (optional) (default to ["type:provincie^1.5","type:gemeente^1.5","type:woonplaats^1.5","type:weg^1.5","type:postcode^0.6","type:adres^1"])
    start = 0 # int | Hiermee wordt opgegeven wat de index is van het eerste resultaat dat teruggegeven wordt. Dit is zero-based. In combinatie met de rows-parameter kunnen deze services gepagineerd worden bevraagd. Hhet maximum is \"10.000\".  (optional) (default to 0)
    rows = 10 # int | Hiermee wordt opgegeven wat het maximale aantal rijen (ofwel resultaten) is dat teruggegeven moet worden op deze bevraging. Het maximum is \"100\".  (optional) (default to 10)
    sort = 'score desc,sortering asc,weergavenaam asc' # str | Hiermee kan worden opgegeven hoe de sortering plaatsvindt. (optional) (default to 'score desc,sortering asc,weergavenaam asc')
    wt = json # str | Hiermee wordt opgegeven wat het outputformaat is van de bevraging. (optional) (default to json)

    try:
        # De Suggest API biedt de mogelijkheid om een (gedeelte van een) zoekopdracht op te voeren, waarnaar er suggesties teruggegeven worden. 
        api_response = await api_instance.suggest(q, lat=lat, lon=lon, fl=fl, fq=fq, qf=qf, bq=bq, start=start, rows=rows, sort=sort, wt=wt)
        print("The response of LocatieserverApi->suggest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocatieserverApi->suggest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Hiermee worden de zoektermen opgegeven. De Solr-syntax voor zoektermen kan hier worden toegepast, bijv. combineren met \&quot;and\&quot;, en het gebruik van dubbele quotes voor opeenvolgende zoektermen. Zoektermen mogen incompleet zijn. Ook wordt er gebruik gemaakt van synoniemen.  Voorbeelden: &#x60;q&#x3D;Utrecht&#x60;: geeft resultaten terug met de zoekterm Utrecht, bijv. adressen in de stad Utrecht, woonplaatsen en gemeenten in de provincie Utrecht.  &#x60;q&#x3D;\&quot;De Bilt\&quot;&#x60;: geeft resultaten terug met de zoekterm De Bilt, bijv. de woonplaats en gemeente De Bilt, of adressen in deze woonplaats. Let op dat bij het daadwerkelijk verzenden van het request onder water de URL-encodingregels toegepast worden, dus een spatie wordt verzonden als een plusteken.  &#x60;q&#x3D;\&quot;Sint Jacob\&quot; Utre&#x60;: geeft o.a. adressen terug waarvan er delen achtereenvolgens beginnen met \&quot;Sint\&quot; en \&quot;Jacob\&quot;, of met \&quot;St\&quot; (synoniem) en \&quot;Jacob\&quot;, en waar ook een deel met \&quot;Utre\&quot; begint. Een voorbeeld is het adres St.-Jacobsstraat 200 (officiële schrijfwijze) in Utrecht.  | 
 **lat** | **float**| Hiermee kan een coördinaat (in lat/lon, ofwel WGS84) worden opgegeven. Met behulp van deze parameters worden de gevonden zoekresultaten gesorteerd op afstand van het meegegeven punt. Wanneer de locatie van de gebruiker bekend is, kan op deze manier effectiever worden gezocht.  Het meegeven van een coördinaat is met name nuttig voor de suggest- en vrije geocoder-services. Hier worden meestal meerdere resultaten teruggegeven. Als decimaal scheidingsteken moet een punt worden opgegeven i.p.v. een komma.  Voorbeeld: &#x60;lat&#x3D;52.09&amp;lon&#x3D;5.12&#x60;  De resultaten worden gesorteerd op afstand van een bepaald punt in het centrum van Utrecht.  | [optional] 
 **lon** | **float**| Hiermee kan een coördinaat (in lat/lon, ofwel WGS84) worden opgegeven. Met behulp van deze parameters worden de gevonden zoekresultaten gesorteerd op afstand van het meegegeven punt. Wanneer de locatie van de gebruiker bekend is, kan op deze manier effectiever worden gezocht.  Het meegeven van een coördinaat is met name nuttig voor de suggest- en vrije geocoder-services. Hier worden meestal meerdere resultaten teruggegeven. Als decimaal scheidingsteken moet een punt worden opgegeven i.p.v. een komma.  Voorbeeld: &#x60;lat&#x3D;52.09&amp;lon&#x3D;5.12&#x60;  De resultaten worden gesorteerd op afstand van een bepaald punt in het centrum van Utrecht.  | [optional] 
 **fl** | **str**| Hiermee worden de velden opgegeven die teruggegeven dienen te worden. | [optional] [default to &#39;id weergavenaam type score adrestype&#39;]
 **fq** | [**List[str]**](str.md)| Hiermee kan een filter query worden opgegeven, bijv. &#x60;fq&#x3D;bron:BAG&#x60;. | [optional] [default to [&quot;type:(gemeente OR woonplaats OR weg OR postcode OR adres)&quot;]]
 **qf** | **str**| Met behulp van deze parameter kan aan bepaalde _velden_ een extra boost worden meegegeven. Hiermee kan de scoreberekening worden aangepast.  | [optional] [default to &#39;exacte_match^1 suggest^0.5 huisnummer^0.5 huisletter^0.5 huisnummertoevoeging^0.5&#39;]
 **bq** | [**List[str]**](str.md)| Met behulp van deze parameter kan aan bepaalde _veldwaarden_ een extra boost worden meegegeven. Ook hiermee kan de scoreberekening worden aangepast.  Voor elke boost query moet een aparte &#x60;bq&#x3D;&lt;boost&gt;&#x60; worden gebruikt. Bijvoorbeeld: &#x60;bq&#x3D;type:gemeente^1.5&amp;bq&#x3D;type:woonplaats^1.5&#x60;.  | [optional] [default to [&quot;type:provincie^1.5&quot;,&quot;type:gemeente^1.5&quot;,&quot;type:woonplaats^1.5&quot;,&quot;type:weg^1.5&quot;,&quot;type:postcode^0.6&quot;,&quot;type:adres^1&quot;]]
 **start** | **int**| Hiermee wordt opgegeven wat de index is van het eerste resultaat dat teruggegeven wordt. Dit is zero-based. In combinatie met de rows-parameter kunnen deze services gepagineerd worden bevraagd. Hhet maximum is \&quot;10.000\&quot;.  | [optional] [default to 0]
 **rows** | **int**| Hiermee wordt opgegeven wat het maximale aantal rijen (ofwel resultaten) is dat teruggegeven moet worden op deze bevraging. Het maximum is \&quot;100\&quot;.  | [optional] [default to 10]
 **sort** | **str**| Hiermee kan worden opgegeven hoe de sortering plaatsvindt. | [optional] [default to &#39;score desc,sortering asc,weergavenaam asc&#39;]
 **wt** | **str**| Hiermee wordt opgegeven wat het outputformaat is van de bevraging. | [optional] [default to json]

### Return type

[**Suggest200Response**](Suggest200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 OK |  -  |
**400** | 400 Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

