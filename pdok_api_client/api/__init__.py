# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from pdok_api_client.api.locatieserver_api import LocatieserverApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from pdok_api_client.api.locatieserver_api import LocatieserverApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
