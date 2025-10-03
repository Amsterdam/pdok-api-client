import pdok_api_client
from pdok_api_client.rest import ApiException
from pprint import pprint
import asyncio

# Defining the host is optional and defaults to https://api.pdok.nl/bzk/locatieserver/search/v3_1
# See configuration.py for a list of all supported configuration parameters.
configuration = pdok_api_client.Configuration(
    host = "https://api.pdok.nl/bzk/locatieserver/search/v3_1"
)


async def main():

    print('Testing..')

    # Enter a context with an instance of the API client
    async with pdok_api_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = pdok_api_client.LocatieserverApi(api_client)
        q = 'Utrecht' # str | Hiermee worden de zoektermen opgegeven. De Solr-syntax voor zoektermen kan hier worden toegepast, bijv. combineren met \"and\", en het gebruik van dubbele quotes voor opeenvolgende zoektermen. Zoektermen mogen incompleet zijn. Ook wordt er gebruik gemaakt van synoniemen.  Voorbeelden: `q=Utrecht`: geeft resultaten terug met de zoekterm Utrecht, bijv. adressen in de stad Utrecht, woonplaatsen en gemeenten in de provincie Utrecht.  `q=\"De Bilt\"`: geeft resultaten terug met de zoekterm De Bilt, bijv. de woonplaats en gemeente De Bilt, of adressen in deze woonplaats. Let op dat bij het daadwerkelijk verzenden van het request onder water de URL-encodingregels toegepast worden, dus een spatie wordt verzonden als een plusteken.  `q=\"Sint Jacob\" Utre`: geeft o.a. adressen terug waarvan er delen achtereenvolgens beginnen met \"Sint\" en \"Jacob\", of met \"St\" (synoniem) en \"Jacob\", en waar ook een deel met \"Utre\" begint. Een voorbeeld is het adres St.-Jacobsstraat 200 (officiële schrijfwijze) in Utrecht.  (optional)
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
        wt = 'json' # str | Hiermee wordt opgegeven wat het outputformaat is van de bevraging. (optional) (default to json)

        async def do_request():

            try:
                # De Free API biedt de mogelijkheid om vrij te zoeken (klassiek geocoderen), waar zonder tussenkomst van suggesties de API direct resultaten teruggeeft op basis van de zoekopdracht.
                api_response = await api_instance.free(q=q, lat=lat, lon=lon, fl=fl, fq=fq, df=df, bq=bq,
                                                       start=start, rows=rows, sort=sort, wt=wt)
                print("The response of LocatieserverApi->free:\n")
                pprint(api_response)
            except ApiException as e:
                print("Exception when calling LocatieserverApi->free: %s\n" % e)

        await do_request()

if __name__ == '__main__':
    asyncio.run(main())
