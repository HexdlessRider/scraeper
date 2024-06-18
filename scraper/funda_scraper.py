import asyncio
import logging
import os
import time
import json

from db.models.apartment import ApartmentStore
from settings.config import VESTEDA_CD
from core.engine import fetch_url


async def main_koop():
    url = "https://listing-search-wonen-arc.funda.io/listings-wonen-searcher-alias-prod/_reactivesearch?preference=_local&filter_path=-responses.aggregations.results.grid.buckets.global_ids.hits.hits._source%2C-responses._shards%2C-responses.aggregations.results.doc_count%2C-responses.**._index%2C-responses.**._score%2C-responses.**.doc_count_error_upper_bound%2C-responses.**.sum_other_doc_count%2C-responses.**._source.address.identifiers"
    headers = {
        "accept": "application/json",
        "accept-language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": "Basic ZjVhMjQyZGIxZmUwOjM5ZDYxMjI3LWQ1YTgtNDIxMi04NDY4LWU1NWQ0MjhjMmM2Zg==",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://www.funda.nl",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.funda.nl/",
        "sec-ch-ua": '"Chromium";v="124", "Opera";v="110", "Not-A.Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0",
        "x-search-client": "ReactiveSearch Vue",
        "x-timestamp": "1717680481770"
    }
    payload_koop = {
        "settings": {
            "recordAnalytics": False,
            "enableQueryRules": True,
            "emptyQuery": True,
            "suggestionAnalytics": True,
            "queryParams": {
                "preference": "_local",
                "filter_path": "-responses.aggregations.results.grid.buckets.global_ids.hits.hits._source,-responses._shards,-responses.aggregations.results.doc_count,-responses.**._index,-responses.**._score,-responses.**.doc_count_error_upper_bound,-responses.**.sum_other_doc_count,-responses.**._source.address.identifiers"
            }
        },
        "query": [
            {
                "id": "object_type",
                "type": "term",
                "dataField": [
                    "object_type"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "object-type-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": []
            },
            {
                "id": "selected_area",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "customQuery": {
                    "id": "location-query-v2",
                    "params": {
                        "location": [
                            "nl"
                        ]
                    }
                }
            },
            {
                "id": "offering_type",
                "type": "term",
                "dataField": [
                    "offering_type"
                ],
                "execute": False,
                "defaultQuery": {
                    "timeout": "500ms"
                },
                "value": "buy"
            },
            {
                "id": "sort",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False
            },
            {
                "id": "price",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "react": {
                    "and": "price__internal"
                },
                "customQuery": {},
                "defaultQuery": {
                    "timeout": "500ms"
                }
            },
            {
                "id": "floor_area",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "react": {
                    "and": "floor_area__internal"
                },
                "defaultQuery": {
                    "timeout": "500ms"
                }
            },
            {
                "id": "plot_area",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "react": {
                    "and": "plot_area__internal"
                },
                "defaultQuery": {
                    "timeout": "500ms"
                }
            },
            {
                "id": "bedrooms",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "react": {
                    "and": "bedrooms__internal"
                },
                "defaultQuery": {
                    "timeout": "500ms"
                }
            },
            {
                "id": "rooms",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "react": {
                    "and": "rooms__internal"
                },
                "defaultQuery": {
                    "timeout": "500ms"
                }
            },
            {
                "id": "exterior_space_garden_size",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "react": {
                    "and": "exterior_space_garden_size__internal"
                },
                "defaultQuery": {
                    "timeout": "500ms"
                }
            },
            {
                "id": "garage_capacity",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "garage_capacity__internal"
                    ]
                },
                "defaultQuery": {
                    "timeout": "500ms"
                }
            },
            {
                "id": "publication_date",
                "type": "term",
                "dataField": [
                    "publish_date_utc"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "publication_date__internal"
                    ]
                },
                "customQuery": {
                    "id": "publish-date-query-v2",
                    "params": {
                        "date_to": None,
                        "date_from": None
                    }
                },
                "defaultQuery": {
                    "id": "publish-date-aggs-v3",
                    "params": {
                        "timeout": "500ms",
                        "date_6_key": "no_preference",
                        "date_6_from": None,
                        "date_6_to": None,
                        "date_5_key": "30",
                        "date_5_from": "now-29d/d",
                        "date_5_to": "now+1h/h",
                        "date_4_key": "10",
                        "date_4_from": "now-9d/d",
                        "date_4_to": "now+1h/h",
                        "date_3_key": "5",
                        "date_3_from": "now-4d/d",
                        "date_3_to": "now+1h/h",
                        "date_2_key": "3",
                        "date_2_from": "now-2d/d",
                        "date_2_to": "now+1h/h",
                        "date_1_key": "1",
                        "date_1_from": "now/d",
                        "date_1_to": "now+1h/h"
                    }
                },
                "value": "no_preference"
            },
            {
                "id": "availability",
                "type": "term",
                "dataField": [
                    "availability"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "availability__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "availability-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": [
                    "available",
                    "negotiations"
                ]
            },
            {
                "id": "construction_type",
                "type": "term",
                "dataField": [
                    "construction_type"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "construction_type__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "construction-type-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": []
            },
            {
                "id": "construction_period",
                "type": "term",
                "dataField": [
                    "construction_period"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "construction_period__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "construction-period-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": []
            },
            {
                "id": "surrounding",
                "type": "term",
                "dataField": [
                    "surrounding"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "surrounding__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "surrounding-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": []
            },
            {
                "id": "garage_type",
                "type": "term",
                "dataField": [
                    "garage.type"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "garage_type__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "garage-type-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": []
            },
            {
                "id": "exterior_space_type",
                "type": "term",
                "dataField": [
                    "exterior_space.type"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "exterior_space_type__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "exterior-space-type-aggs-v3",
                    "params": {
                        "value": {},
                        "timeout": "500ms"
                    }
                },
                "value": []
            },
            {
                "id": "exterior_space_garden_orientation",
                "type": "term",
                "dataField": [
                    "exterior_space.garden_orientation"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "exterior_space_garden_orientation__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "garden-orientation-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": []
            },
            {
                "id": "energy_label",
                "type": "term",
                "dataField": [
                    "energy_label"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "energy_label__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "energy-label-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": []
            },
            {
                "id": "zoning",
                "type": "term",
                "dataField": [
                    "zoning"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "zoning__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "zoning-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": [
                    "residential"
                ]
            },
            {
                "id": "amenities",
                "type": "term",
                "dataField": [
                    "amenities"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "amenities__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "amenities-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": []
            },
            {
                "id": "type",
                "type": "term",
                "dataField": [
                    "type"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "type__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "type-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": [
                    "single"
                ]
            },
            {
                "id": "nvm_open_house_day",
                "type": "term",
                "dataField": [
                    "open_house_datetime_slot.is_nvm_open_house_day"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "nvm_open_house_day__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "nvm-open-house-day-aggs-v1",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": []
            },
            {
                "id": "open_house",
                "type": "term",
                "dataField": [
                    "open_house_datetime_slot.open_house_date"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "open_house__internal"
                    ]
                },
                "customQuery": {},
                "defaultQuery": {
                    "id": "open-house-aggs-v1",
                    "params": {
                        "timeout": "500ms",
                        "date_3_key": "coming_weekend",
                        "date_3_from": "now+7d/w-2d",
                        "date_3_to": "now+7d/w",
                        "date_2_key": "today",
                        "date_2_from": "now/d",
                        "date_2_to": "now+1d/d",
                        "date_1_key": "all",
                        "date_1_from": "now/h",
                        "date_1_to": None
                    }
                },
                "value": []
            },
            {
                "id": "free_text_search",
                "type": "search",
                "dataField": [
                    "description.dutch"
                ],
                "execute": False,
                "react": {
                    "and": "free_text_search__internal"
                },
                "customQuery": {}
            },
            {
                "id": "agent_id",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "react": {
                    "and": "agent_id__internal"
                },
                "customQuery": {},
                "defaultQuery": {
                    "timeout": "500ms"
                }
            },
            {
                "id": "object_type_house_orientation",
                "type": "term",
                "dataField": [
                    "object_type_specifications.house.orientation"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house",
                        "object_type_house_orientation__internal"
                    ],
                    "or": [
                        "object_type"
                    ]
                },
                "customQuery": {},
                "defaultQuery": {
                    "id": "house-orientation-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": []
            },
            {
                "id": "object_type_house",
                "type": "term",
                "dataField": [
                    "object_type_specifications.house.type"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house__internal"
                    ],
                    "or": [
                        "object_type"
                    ]
                },
                "customQuery": {},
                "defaultQuery": {
                    "id": "house-type-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": []
            },
            {
                "id": "object_type_apartment_orientation",
                "type": "term",
                "dataField": [
                    "object_type_specifications.apartment.orientation"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_apartment",
                        "object_type_apartment_orientation__internal"
                    ],
                    "or": [
                        "object_type"
                    ]
                },
                "customQuery": {},
                "defaultQuery": {
                    "id": "apartment-orientation-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": []
            },
            {
                "id": "object_type_apartment",
                "type": "term",
                "dataField": [
                    "object_type_specifications.apartment.type"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_apartment_orientation",
                        "object_type_apartment__internal"
                    ],
                    "or": [
                        "object_type"
                    ]
                },
                "customQuery": {},
                "defaultQuery": {
                    "id": "apartment-type-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": []
            },
            {
                "id": "object_type_parking",
                "type": "term",
                "dataField": [
                    "object_type_specifications.parking.type"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_parking_capacity",
                        "object_type_parking__internal"
                    ],
                    "or": [
                        "object_type"
                    ]
                },
                "customQuery": {},
                "defaultQuery": {
                    "id": "parking-type-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": []
            },
            {
                "id": "object_type_parking_capacity",
                "type": "term",
                "dataField": [
                    "object_type_specifications.parking.capacity"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_parking",
                        "object_type_parking_capacity__internal"
                    ],
                    "or": [
                        "object_type"
                    ]
                },
                "customQuery": {},
                "defaultQuery": {
                    "id": "parking-capacity-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": []
            },
            {
                "id": "search_result",
                "type": "search",
                "dataField": [
                    "availability"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "map_results",
                        "object_type",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "search_result__internal"
                    ]
                },
                "size": 15,
                "from": 1,
                "defaultQuery": {
                    "track_total_hits": True,
                    "timeout": "1s",
                    "sort": [
                        {
                            "placement_type": "asc"
                        },
                        {
                            "relevancy_sort_order": "desc"
                        },
                        {
                            "id.number": "desc"
                        }
                    ],
                    "_source": {
                        "includes": [
                            "address",
                            "agent",
                            "available_media_types",
                            "blikvanger",
                            "construction_date_range",
                            "energy_label",
                            "floor_area",
                            "floor_area_range",
                            "handover_date_range",
                            "tiny_id",
                            "id",
                            "name",
                            "number_of_bedrooms",
                            "number_of_rooms",
                            "object_detail_page_relative_url",
                            "offering_type",
                            "open_house_datetime_slot",
                            "plot_area",
                            "plot_area_range",
                            "price",
                            "project",
                            "publish_date",
                            "sale_date_range",
                            "status",
                            "thumbnail_id",
                            "type",
                            "object_type"
                        ]
                    }
                }
            }
        ]

    }

    try:
        data = await fetch_url('POST', url, 1, payload=payload_koop, headers=headers)
        if data is None:
            logging.error("Failed to fetch data: No response")
            return  # Exit the function or handle the case where no data is returned

        json_data = json.loads(data)
        if 'search_result' not in json_data or 'hits' not in json_data['search_if_search_data'] or 'total' not in \
                json_data['total']['hits']:
            logging.error("Invalid JSON structure")
            return  # Handle the case where JSON structure is different

        count_items = json_data['search_result']['hits']['total']['value']
    except json.JSONDecodeError as e:
        logging.error(f"JSON decoding failed: {e}")
        return  # Exit the function or handle JSON decode error
    except KeyError as e:
        logging.error(f"Data parsing error - key missing: {e}")
        return  # Handle missing keys in JSON data
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return  # Handle other unexpected errors
    count_items = 10000
    pages = (count_items // 750) + 1
    result = []
    for page in range(1, pages + 1):
        items_per_page = 750
        from_param = (page - 1) * items_per_page
        if from_param > count_items - 750:
            items_per_page = count_items - (page - 1) * items_per_page
        payload = {
            "settings": {
                "recordAnalytics": False,
                "enableQueryRules": True,
                "emptyQuery": True,
                "suggestionAnalytics": True,
                "queryParams": {
                    "preference": "_local",
                    "filter_path": "-responses.aggregations.results.grid.buckets.global_ids.hits.hits._source,-responses._shards,-responses.aggregations.results.doc_count,-responses.**._index,-responses.**._score,-responses.**.doc_count_error_upper_bound,-responses.**.sum_other_doc_count,-responses.**._source.address.identifiers"
                }
            },
            "query": [
                {
                    "id": "object_type",
                    "type": "term",
                    "dataField": [
                        "object_type"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "object-type-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": []
                },
                {
                    "id": "selected_area",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "customQuery": {
                        "id": "location-query-v2",
                        "params": {
                            "location": [
                                "nl"
                            ]
                        }
                    }
                },
                {
                    "id": "offering_type",
                    "type": "term",
                    "dataField": [
                        "offering_type"
                    ],
                    "execute": False,
                    "defaultQuery": {
                        "timeout": "500ms"
                    },
                    "value": "buy"
                },
                {
                    "id": "sort",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False
                },
                {
                    "id": "price",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "react": {
                        "and": "price__internal"
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "timeout": "500ms"
                    }
                },
                {
                    "id": "floor_area",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "react": {
                        "and": "floor_area__internal"
                    },
                    "defaultQuery": {
                        "timeout": "500ms"
                    }
                },
                {
                    "id": "plot_area",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "react": {
                        "and": "plot_area__internal"
                    },
                    "defaultQuery": {
                        "timeout": "500ms"
                    }
                },
                {
                    "id": "bedrooms",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "react": {
                        "and": "bedrooms__internal"
                    },
                    "defaultQuery": {
                        "timeout": "500ms"
                    }
                },
                {
                    "id": "rooms",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "react": {
                        "and": "rooms__internal"
                    },
                    "defaultQuery": {
                        "timeout": "500ms"
                    }
                },
                {
                    "id": "exterior_space_garden_size",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "react": {
                        "and": "exterior_space_garden_size__internal"
                    },
                    "defaultQuery": {
                        "timeout": "500ms"
                    }
                },
                {
                    "id": "garage_capacity",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "garage_capacity__internal"
                        ]
                    },
                    "defaultQuery": {
                        "timeout": "500ms"
                    }
                },
                {
                    "id": "publication_date",
                    "type": "term",
                    "dataField": [
                        "publish_date_utc"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "publication_date__internal"
                        ]
                    },
                    "customQuery": {
                        "id": "publish-date-query-v2",
                        "params": {
                            "date_to": None,
                            "date_from": None
                        }
                    },
                    "defaultQuery": {
                        "id": "publish-date-aggs-v3",
                        "params": {
                            "timeout": "500ms",
                            "date_6_key": "no_preference",
                            "date_6_from": None,
                            "date_6_to": None,
                            "date_5_key": "30",
                            "date_5_from": "now-29d/d",
                            "date_5_to": "now+1h/h",
                            "date_4_key": "10",
                            "date_4_from": "now-9d/d",
                            "date_4_to": "now+1h/h",
                            "date_3_key": "5",
                            "date_3_from": "now-4d/d",
                            "date_3_to": "now+1h/h",
                            "date_2_key": "3",
                            "date_2_from": "now-2d/d",
                            "date_2_to": "now+1h/h",
                            "date_1_key": "1",
                            "date_1_from": "now/d",
                            "date_1_to": "now+1h/h"
                        }
                    },
                    "value": "no_preference"
                },
                {
                    "id": "availability",
                    "type": "term",
                    "dataField": [
                        "availability"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "availability__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "availability-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": [
                        "available",
                        "negotiations"
                    ]
                },
                {
                    "id": "construction_type",
                    "type": "term",
                    "dataField": [
                        "construction_type"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "construction_type__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "construction-type-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": []
                },
                {
                    "id": "construction_period",
                    "type": "term",
                    "dataField": [
                        "construction_period"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "construction_period__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "construction-period-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": []
                },
                {
                    "id": "surrounding",
                    "type": "term",
                    "dataField": [
                        "surrounding"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "surrounding__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "surrounding-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": []
                },
                {
                    "id": "garage_type",
                    "type": "term",
                    "dataField": [
                        "garage.type"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "garage_type__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "garage-type-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": []
                },
                {
                    "id": "exterior_space_type",
                    "type": "term",
                    "dataField": [
                        "exterior_space.type"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "exterior_space_type__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "exterior-space-type-aggs-v3",
                        "params": {
                            "value": {},
                            "timeout": "500ms"
                        }
                    },
                    "value": []
                },
                {
                    "id": "exterior_space_garden_orientation",
                    "type": "term",
                    "dataField": [
                        "exterior_space.garden_orientation"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "exterior_space_garden_orientation__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "garden-orientation-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": []
                },
                {
                    "id": "energy_label",
                    "type": "term",
                    "dataField": [
                        "energy_label"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "energy_label__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "energy-label-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": []
                },
                {
                    "id": "zoning",
                    "type": "term",
                    "dataField": [
                        "zoning"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "zoning__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "zoning-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": [
                        "residential"
                    ]
                },
                {
                    "id": "amenities",
                    "type": "term",
                    "dataField": [
                        "amenities"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "amenities__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "amenities-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": []
                },
                {
                    "id": "type",
                    "type": "term",
                    "dataField": [
                        "type"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "type__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "type-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": [
                        "single"
                    ]
                },
                {
                    "id": "nvm_open_house_day",
                    "type": "term",
                    "dataField": [
                        "open_house_datetime_slot.is_nvm_open_house_day"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "nvm_open_house_day__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "nvm-open-house-day-aggs-v1",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": []
                },
                {
                    "id": "open_house",
                    "type": "term",
                    "dataField": [
                        "open_house_datetime_slot.open_house_date"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "open_house__internal"
                        ]
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "id": "open-house-aggs-v1",
                        "params": {
                            "timeout": "500ms",
                            "date_3_key": "coming_weekend",
                            "date_3_from": "now+7d/w-2d",
                            "date_3_to": "now+7d/w",
                            "date_2_key": "today",
                            "date_2_from": "now/d",
                            "date_2_to": "now+1d/d",
                            "date_1_key": "all",
                            "date_1_from": "now/h",
                            "date_1_to": None
                        }
                    },
                    "value": []
                },
                {
                    "id": "free_text_search",
                    "type": "search",
                    "dataField": [
                        "description.dutch"
                    ],
                    "execute": False,
                    "react": {
                        "and": "free_text_search__internal"
                    },
                    "customQuery": {}
                },
                {
                    "id": "agent_id",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "react": {
                        "and": "agent_id__internal"
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "timeout": "500ms"
                    }
                },
                {
                    "id": "object_type_house_orientation",
                    "type": "term",
                    "dataField": [
                        "object_type_specifications.house.orientation"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house",
                            "object_type_house_orientation__internal"
                        ],
                        "or": [
                            "object_type"
                        ]
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "id": "house-orientation-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": []
                },
                {
                    "id": "object_type_house",
                    "type": "term",
                    "dataField": [
                        "object_type_specifications.house.type"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house__internal"
                        ],
                        "or": [
                            "object_type"
                        ]
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "id": "house-type-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": []
                },
                {
                    "id": "object_type_apartment_orientation",
                    "type": "term",
                    "dataField": [
                        "object_type_specifications.apartment.orientation"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_apartment",
                            "object_type_apartment_orientation__internal"
                        ],
                        "or": [
                            "object_type"
                        ]
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "id": "apartment-orientation-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": []
                },
                {
                    "id": "object_type_apartment",
                    "type": "term",
                    "dataField": [
                        "object_type_specifications.apartment.type"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_apartment_orientation",
                            "object_type_apartment__internal"
                        ],
                        "or": [
                            "object_type"
                        ]
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "id": "apartment-type-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": []
                },
                {
                    "id": "object_type_parking",
                    "type": "term",
                    "dataField": [
                        "object_type_specifications.parking.type"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_parking_capacity",
                            "object_type_parking__internal"
                        ],
                        "or": [
                            "object_type"
                        ]
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "id": "parking-type-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": []
                },
                {
                    "id": "object_type_parking_capacity",
                    "type": "term",
                    "dataField": [
                        "object_type_specifications.parking.capacity"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_parking",
                            "object_type_parking_capacity__internal"
                        ],
                        "or": [
                            "object_type"
                        ]
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "id": "parking-capacity-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": []
                },
                {
                    "id": "search_result",
                    "type": "search",
                    "dataField": [
                        "availability"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "map_results",
                            "object_type",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "search_result__internal"
                        ]
                    },
                    "size": items_per_page,
                    "from": from_param,
                    "defaultQuery": {
                        "track_total_hits": True,
                        "timeout": "1s",
                        "sort": [
                            {
                                "placement_type": "asc"
                            },
                            {
                                "relevancy_sort_order": "desc"
                            },
                            {
                                "id.number": "desc"
                            }
                        ],
                        "_source": {
                            "includes": [
                                "address",
                                "agent",
                                "available_media_types",
                                "blikvanger",
                                "construction_date_range",
                                "energy_label",
                                "floor_area",
                                "floor_area_range",
                                "handover_date_range",
                                "tiny_id",
                                "id",
                                "name",
                                "number_of_bedrooms",
                                "number_of_rooms",
                                "object_detail_page_relative_url",
                                "offering_type",
                                "open_house_datetime_slot",
                                "plot_area",
                                "plot_area_range",
                                "price",
                                "project",
                                "publish_date",
                                "sale_date_range",
                                "status",
                                "thumbnail_id",
                                "type",
                                "object_type"
                            ]
                        }
                    }
                }
            ]

        }

        try:
            raw_data = await fetch_url('POST', url, 1, payload=payload, headers=headers)
            if raw_data is None:
                logging.error('No data received from the server')
                return  # Exit the function if no data was fetched

            json_data = json.loads(raw_data)
            if 'search_result' not in json_data or 'hits' not in json_data['search_result'] or 'hits' not in \
                    json_data['search_result']['hits']:
                logging.error('JSON does not contain the expected data structure')
                return  # Exit the function if the JSON structure is incorrect

            data = json_data['search_result']['hits']['hits']
            if not data:
                logging.error('Data list is empty')
                return  # Exit if data is empty or not present
            data = [elm['_source'] for elm in data]
            result.extend(data)
        except json.JSONDecodeError as err:
            logging.error(f'Error decoding JSON: {err}')
        except Exception as err:
            logging.info(str(err))
            logging.error(f'Unexpected error: {err}')
    return result


async def main_huur():
    url = "https://listing-search-wonen-arc.funda.io/listings-wonen-searcher-alias-prod/_reactivesearch?preference=_local&filter_path=-responses.aggregations.results.grid.buckets.global_ids.hits.hits._source%2C-responses._shards%2C-responses.aggregations.results.doc_count%2C-responses.**._index%2C-responses.**._score%2C-responses.**.doc_count_error_upper_bound%2C-responses.**.sum_other_doc_count%2C-responses.**._source.address.identifiers"
    headers = {
        "accept": "application/json",
        "accept-language": "uk-UA,uk;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": "Basic ZjVhMjQyZGIxZmUwOjM5ZDYxMjI3LWQ1YTgtNDIxMi04NDY4LWU1NWQ0MjhjMmM2Zg==",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://www.funda.nl",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.funda.nl/",
        "sec-ch-ua": '"Chromium";v="124", "Opera";v="110", "Not-A.Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 OPR/110.0.0.0",
        "x-search-client": "ReactiveSearch Vue",
        "x-timestamp": "1717680481770"
    }
    payload_huur = {
        "settings": {
            "recordAnalytics": False,
            "enableQueryRules": True,
            "emptyQuery": True,
            "suggestionAnalytics": True,
            "queryParams": {
                "preference": "_local",
                "filter_path": "-responses.aggregations.results.grid.buckets.global_ids.hits.hits._source,-responses._shards,-responses.aggregations.results.doc_count,-responses.**._index,-responses.**._score,-responses.**.doc_count_error_upper_bound,-responses.**.sum_other_doc_count,-responses.**._source.address.identifiers"
            }
        },
        "query": [
            {
                "id": "search_result",
                "type": "search",
                "dataField": [
                    "availability"
                ],
                "execute": True,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "map_results",
                        "object_type",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "search_result__internal"
                    ]
                },
                "size": 15,
                "from": 15,
                "defaultQuery": {
                    "track_total_hits": True,
                    "timeout": "1s",
                    "sort": [
                        {
                            "placement_type": "asc"
                        },
                        {
                            "relevancy_sort_order": "desc"
                        },
                        {
                            "id.number": "desc"
                        }
                    ],
                    "_source": {
                        "includes": [
                            "address",
                            "agent",
                            "available_media_types",
                            "blikvanger",
                            "construction_date_range",
                            "energy_label",
                            "floor_area",
                            "floor_area_range",
                            "handover_date_range",
                            "tiny_id",
                            "id",
                            "name",
                            "number_of_bedrooms",
                            "number_of_rooms",
                            "object_detail_page_relative_url",
                            "offering_type",
                            "open_house_datetime_slot",
                            "plot_area",
                            "plot_area_range",
                            "price",
                            "project",
                            "publish_date",
                            "sale_date_range",
                            "status",
                            "thumbnail_id",
                            "type",
                            "object_type"
                        ]
                    }
                }
            },
            {
                "id": "selected_area",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "customQuery": {
                    "id": "location-query-v2",
                    "params": {
                        "location": [
                            "nl"
                        ]
                    }
                }
            },
            {
                "id": "offering_type",
                "type": "term",
                "dataField": [
                    "offering_type"
                ],
                "execute": False,
                "defaultQuery": {
                    "timeout": "500ms"
                },
                "value": "rent"
            },
            {
                "id": "sort",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False
            },
            {
                "id": "price",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "react": {
                    "and": "price__internal"
                },
                "customQuery": {
                    "id": "empty-query-v1"
                },
                "defaultQuery": {
                    "timeout": "500ms"
                }
            },
            {
                "id": "floor_area",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "react": {
                    "and": "floor_area__internal"
                },
                "defaultQuery": {
                    "timeout": "500ms"
                }
            },
            {
                "id": "plot_area",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "react": {
                    "and": "plot_area__internal"
                },
                "defaultQuery": {
                    "timeout": "500ms"
                }
            },
            {
                "id": "bedrooms",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "react": {
                    "and": "bedrooms__internal"
                },
                "defaultQuery": {
                    "timeout": "500ms"
                }
            },
            {
                "id": "rooms",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "react": {
                    "and": "rooms__internal"
                },
                "defaultQuery": {
                    "timeout": "500ms"
                }
            },
            {
                "id": "exterior_space_garden_size",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "react": {
                    "and": "exterior_space_garden_size__internal"
                },
                "defaultQuery": {
                    "timeout": "500ms"
                }
            },
            {
                "id": "garage_capacity",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "garage_capacity__internal"
                    ]
                },
                "defaultQuery": {
                    "timeout": "500ms"
                }
            },
            {
                "id": "publication_date",
                "type": "term",
                "dataField": [
                    "publish_date_utc"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "publication_date__internal"
                    ]
                },
                "customQuery": {
                    "id": "publish-date-query-v2",
                    "params": {
                        "date_to": None,
                        "date_from": None
                    }
                },
                "defaultQuery": {
                    "id": "publish-date-aggs-v3",
                    "params": {
                        "timeout": "500ms",
                        "date_6_key": "no_preference",
                        "date_6_from": None,
                        "date_6_to": None,
                        "date_5_key": "30",
                        "date_5_from": "now-29d/d",
                        "date_5_to": "now+1h/h",
                        "date_4_key": "10",
                        "date_4_from": "now-9d/d",
                        "date_4_to": "now+1h/h",
                        "date_3_key": "5",
                        "date_3_from": "now-4d/d",
                        "date_3_to": "now+1h/h",
                        "date_2_key": "3",
                        "date_2_from": "now-2d/d",
                        "date_2_to": "now+1h/h",
                        "date_1_key": "1",
                        "date_1_from": "now/d",
                        "date_1_to": "now+1h/h"
                    }
                },
                "value": "no_preference"
            },
            {
                "id": "object_type",
                "type": "term",
                "dataField": [
                    "object_type"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "object-type-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                }
            },
            {
                "id": "availability",
                "type": "term",
                "dataField": [
                    "availability"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "availability__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "availability-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": [
                    "available",
                    "negotiations"
                ]
            },
            {
                "id": "construction_type",
                "type": "term",
                "dataField": [
                    "construction_type"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "construction_type__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "construction-type-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                }
            },
            {
                "id": "construction_period",
                "type": "term",
                "dataField": [
                    "construction_period"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "construction_period__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "construction-period-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                }
            },
            {
                "id": "surrounding",
                "type": "term",
                "dataField": [
                    "surrounding"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "surrounding__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "surrounding-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                }
            },
            {
                "id": "garage_type",
                "type": "term",
                "dataField": [
                    "garage.type"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "garage_type__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "garage-type-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                }
            },
            {
                "id": "exterior_space_type",
                "type": "term",
                "dataField": [
                    "exterior_space.type"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "exterior_space_type__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "exterior-space-type-aggs-v3",
                    "params": {
                        "value": {},
                        "timeout": "500ms"
                    }
                }
            },
            {
                "id": "exterior_space_garden_orientation",
                "type": "term",
                "dataField": [
                    "exterior_space.garden_orientation"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "exterior_space_garden_orientation__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "garden-orientation-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                }
            },
            {
                "id": "energy_label",
                "type": "term",
                "dataField": [
                    "energy_label"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "energy_label__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "energy-label-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                }
            },
            {
                "id": "zoning",
                "type": "term",
                "dataField": [
                    "zoning"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "zoning__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "zoning-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": [
                    "residential"
                ]
            },
            {
                "id": "amenities",
                "type": "term",
                "dataField": [
                    "amenities"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "amenities__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "amenities-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                }
            },
            {
                "id": "type",
                "type": "term",
                "dataField": [
                    "type"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "type__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "type-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                },
                "value": [
                    "single"
                ]
            },
            {
                "id": "nvm_open_house_day",
                "type": "term",
                "dataField": [
                    "open_house_datetime_slot.is_nvm_open_house_day"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "nvm_open_house_day__internal"
                    ]
                },
                "defaultQuery": {
                    "id": "nvm-open-house-day-aggs-v1",
                    "params": {
                        "timeout": "500ms"
                    }
                }
            },
            {
                "id": "open_house",
                "type": "term",
                "dataField": [
                    "open_house_datetime_slot.open_house_date"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "object_type",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house",
                        "object_type_apartment_orientation",
                        "object_type_apartment",
                        "object_type_parking",
                        "object_type_parking_capacity",
                        "open_house__internal"
                    ]
                },
                "customQuery": {},
                "defaultQuery": {
                    "id": "open-house-aggs-v1",
                    "params": {
                        "timeout": "500ms",
                        "date_3_key": "coming_weekend",
                        "date_3_from": "now+7d/w-2d",
                        "date_3_to": "now+7d/w",
                        "date_2_key": "today",
                        "date_2_from": "now/d",
                        "date_2_to": "now+1d/d",
                        "date_1_key": "all",
                        "date_1_from": "now/h",
                        "date_1_to": None
                    }
                }
            },
            {
                "id": "free_text_search",
                "type": "search",
                "dataField": [
                    "description.dutch"
                ],
                "execute": False,
                "react": {
                    "and": "free_text_search__internal"
                },
                "customQuery": {}
            },
            {
                "id": "agent_id",
                "type": "term",
                "dataField": [
                    "reactive_component_field"
                ],
                "execute": False,
                "react": {
                    "and": "agent_id__internal"
                },
                "customQuery": {},
                "defaultQuery": {
                    "timeout": "500ms"
                }
            },
            {
                "id": "object_type_house_orientation",
                "type": "term",
                "dataField": [
                    "object_type_specifications.house.orientation"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house",
                        "object_type_house_orientation__internal"
                    ],
                    "or": [
                        "object_type"
                    ]
                },
                "customQuery": {},
                "defaultQuery": {
                    "id": "house-orientation-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                }
            },
            {
                "id": "object_type_house",
                "type": "term",
                "dataField": [
                    "object_type_specifications.house.type"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_house_orientation",
                        "object_type_house__internal"
                    ],
                    "or": [
                        "object_type"
                    ]
                },
                "customQuery": {},
                "defaultQuery": {
                    "id": "house-type-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                }
            },
            {
                "id": "object_type_apartment_orientation",
                "type": "term",
                "dataField": [
                    "object_type_specifications.apartment.orientation"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_apartment",
                        "object_type_apartment_orientation__internal"
                    ],
                    "or": [
                        "object_type"
                    ]
                },
                "customQuery": {},
                "defaultQuery": {
                    "id": "apartment-orientation-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                }
            },
            {
                "id": "object_type_apartment",
                "type": "term",
                "dataField": [
                    "object_type_specifications.apartment.type"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_apartment_orientation",
                        "object_type_apartment__internal"
                    ],
                    "or": [
                        "object_type"
                    ]
                },
                "customQuery": {},
                "defaultQuery": {
                    "id": "apartment-type-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                }
            },
            {
                "id": "object_type_parking",
                "type": "term",
                "dataField": [
                    "object_type_specifications.parking.type"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_parking_capacity",
                        "object_type_parking__internal"
                    ],
                    "or": [
                        "object_type"
                    ]
                },
                "customQuery": {},
                "defaultQuery": {
                    "id": "parking-type-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                }
            },
            {
                "id": "object_type_parking_capacity",
                "type": "term",
                "dataField": [
                    "object_type_specifications.parking.capacity"
                ],
                "execute": False,
                "react": {
                    "and": [
                        "selected_area",
                        "offering_type",
                        "sort",
                        "price",
                        "floor_area",
                        "plot_area",
                        "bedrooms",
                        "rooms",
                        "exterior_space_garden_size",
                        "garage_capacity",
                        "publication_date",
                        "availability",
                        "construction_type",
                        "construction_period",
                        "surrounding",
                        "garage_type",
                        "exterior_space_type",
                        "exterior_space_garden_orientation",
                        "energy_label",
                        "zoning",
                        "amenities",
                        "type",
                        "nvm_open_house_day",
                        "open_house",
                        "free_text_search",
                        "agent_id",
                        "object_type_parking",
                        "object_type_parking_capacity__internal"
                    ],
                    "or": [
                        "object_type"
                    ]
                },
                "customQuery": {},
                "defaultQuery": {
                    "id": "parking-capacity-aggs-v3",
                    "params": {
                        "timeout": "500ms"
                    }
                }
            }
        ]

    }

    data = await fetch_url('POST', url, 1, payload=payload_huur, headers=headers,
                           )
    count_items = json.loads(data)['search_result']['hits']['total']['value']
    pages = (count_items // 750) + 1
    result = []
    for page in range(1, pages + 1):
        items_per_page = 750
        from_param = (page - 1) * items_per_page
        if from_param > count_items - 750:
            items_per_page = count_items - (page - 1) * items_per_page
        payload = {
            "settings": {
                "recordAnalytics": False,
                "enableQueryRules": True,
                "emptyQuery": True,
                "suggestionAnalytics": True,
                "queryParams": {
                    "preference": "_local",
                    "filter_path": "-responses.aggregations.results.grid.buckets.global_ids.hits.hits._source,-responses._shards,-responses.aggregations.results.doc_count,-responses.**._index,-responses.**._score,-responses.**.doc_count_error_upper_bound,-responses.**.sum_other_doc_count,-responses.**._source.address.identifiers"
                }
            },
            "query": [
                {
                    "id": "search_result",
                    "type": "search",
                    "dataField": [
                        "availability"
                    ],
                    "execute": True,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "map_results",
                            "object_type",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "search_result__internal"
                        ]
                    },
                    "size": items_per_page,
                    "from": from_param,
                    "defaultQuery": {
                        "track_total_hits": True,
                        "timeout": "1s",
                        "sort": [
                            {
                                "placement_type": "asc"
                            },
                            {
                                "relevancy_sort_order": "desc"
                            },
                            {
                                "id.number": "desc"
                            }
                        ],
                        "_source": {
                            "includes": [
                                "address",
                                "agent",
                                "available_media_types",
                                "blikvanger",
                                "construction_date_range",
                                "energy_label",
                                "floor_area",
                                "floor_area_range",
                                "handover_date_range",
                                "tiny_id",
                                "id",
                                "name",
                                "number_of_bedrooms",
                                "number_of_rooms",
                                "object_detail_page_relative_url",
                                "offering_type",
                                "open_house_datetime_slot",
                                "plot_area",
                                "plot_area_range",
                                "price",
                                "project",
                                "publish_date",
                                "sale_date_range",
                                "status",
                                "thumbnail_id",
                                "type",
                                "object_type"
                            ]
                        }
                    }
                },
                {
                    "id": "selected_area",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "customQuery": {
                        "id": "location-query-v2",
                        "params": {
                            "location": [
                                "nl"
                            ]
                        }
                    }
                },
                {
                    "id": "offering_type",
                    "type": "term",
                    "dataField": [
                        "offering_type"
                    ],
                    "execute": False,
                    "defaultQuery": {
                        "timeout": "500ms"
                    },
                    "value": "rent"
                },
                {
                    "id": "sort",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False
                },
                {
                    "id": "price",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "react": {
                        "and": "price__internal"
                    },
                    "customQuery": {
                        "id": "empty-query-v1"
                    },
                    "defaultQuery": {
                        "timeout": "500ms"
                    }
                },
                {
                    "id": "floor_area",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "react": {
                        "and": "floor_area__internal"
                    },
                    "defaultQuery": {
                        "timeout": "500ms"
                    }
                },
                {
                    "id": "plot_area",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "react": {
                        "and": "plot_area__internal"
                    },
                    "defaultQuery": {
                        "timeout": "500ms"
                    }
                },
                {
                    "id": "bedrooms",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "react": {
                        "and": "bedrooms__internal"
                    },
                    "defaultQuery": {
                        "timeout": "500ms"
                    }
                },
                {
                    "id": "rooms",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "react": {
                        "and": "rooms__internal"
                    },
                    "defaultQuery": {
                        "timeout": "500ms"
                    }
                },
                {
                    "id": "exterior_space_garden_size",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "react": {
                        "and": "exterior_space_garden_size__internal"
                    },
                    "defaultQuery": {
                        "timeout": "500ms"
                    }
                },
                {
                    "id": "garage_capacity",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "garage_capacity__internal"
                        ]
                    },
                    "defaultQuery": {
                        "timeout": "500ms"
                    }
                },
                {
                    "id": "publication_date",
                    "type": "term",
                    "dataField": [
                        "publish_date_utc"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "publication_date__internal"
                        ]
                    },
                    "customQuery": {
                        "id": "publish-date-query-v2",
                        "params": {
                            "date_to": None,
                            "date_from": None
                        }
                    },
                    "defaultQuery": {
                        "id": "publish-date-aggs-v3",
                        "params": {
                            "timeout": "500ms",
                            "date_6_key": "no_preference",
                            "date_6_from": None,
                            "date_6_to": None,
                            "date_5_key": "30",
                            "date_5_from": "now-29d/d",
                            "date_5_to": "now+1h/h",
                            "date_4_key": "10",
                            "date_4_from": "now-9d/d",
                            "date_4_to": "now+1h/h",
                            "date_3_key": "5",
                            "date_3_from": "now-4d/d",
                            "date_3_to": "now+1h/h",
                            "date_2_key": "3",
                            "date_2_from": "now-2d/d",
                            "date_2_to": "now+1h/h",
                            "date_1_key": "1",
                            "date_1_from": "now/d",
                            "date_1_to": "now+1h/h"
                        }
                    },
                    "value": "no_preference"
                },
                {
                    "id": "object_type",
                    "type": "term",
                    "dataField": [
                        "object_type"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "object-type-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    }
                },
                {
                    "id": "availability",
                    "type": "term",
                    "dataField": [
                        "availability"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "availability__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "availability-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": [
                        "available",
                        "negotiations"
                    ]
                },
                {
                    "id": "construction_type",
                    "type": "term",
                    "dataField": [
                        "construction_type"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "construction_type__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "construction-type-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    }
                },
                {
                    "id": "construction_period",
                    "type": "term",
                    "dataField": [
                        "construction_period"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "construction_period__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "construction-period-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    }
                },
                {
                    "id": "surrounding",
                    "type": "term",
                    "dataField": [
                        "surrounding"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "surrounding__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "surrounding-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    }
                },
                {
                    "id": "garage_type",
                    "type": "term",
                    "dataField": [
                        "garage.type"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "garage_type__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "garage-type-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    }
                },
                {
                    "id": "exterior_space_type",
                    "type": "term",
                    "dataField": [
                        "exterior_space.type"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "exterior_space_type__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "exterior-space-type-aggs-v3",
                        "params": {
                            "value": {},
                            "timeout": "500ms"
                        }
                    }
                },
                {
                    "id": "exterior_space_garden_orientation",
                    "type": "term",
                    "dataField": [
                        "exterior_space.garden_orientation"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "exterior_space_garden_orientation__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "garden-orientation-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    }
                },
                {
                    "id": "energy_label",
                    "type": "term",
                    "dataField": [
                        "energy_label"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "energy_label__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "energy-label-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    }
                },
                {
                    "id": "zoning",
                    "type": "term",
                    "dataField": [
                        "zoning"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "zoning__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "zoning-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": [
                        "residential"
                    ]
                },
                {
                    "id": "amenities",
                    "type": "term",
                    "dataField": [
                        "amenities"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "amenities__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "amenities-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    }
                },
                {
                    "id": "type",
                    "type": "term",
                    "dataField": [
                        "type"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "type__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "type-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    },
                    "value": [
                        "single"
                    ]
                },
                {
                    "id": "nvm_open_house_day",
                    "type": "term",
                    "dataField": [
                        "open_house_datetime_slot.is_nvm_open_house_day"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "nvm_open_house_day__internal"
                        ]
                    },
                    "defaultQuery": {
                        "id": "nvm-open-house-day-aggs-v1",
                        "params": {
                            "timeout": "500ms"
                        }
                    }
                },
                {
                    "id": "open_house",
                    "type": "term",
                    "dataField": [
                        "open_house_datetime_slot.open_house_date"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "object_type",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house",
                            "object_type_apartment_orientation",
                            "object_type_apartment",
                            "object_type_parking",
                            "object_type_parking_capacity",
                            "open_house__internal"
                        ]
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "id": "open-house-aggs-v1",
                        "params": {
                            "timeout": "500ms",
                            "date_3_key": "coming_weekend",
                            "date_3_from": "now+7d/w-2d",
                            "date_3_to": "now+7d/w",
                            "date_2_key": "today",
                            "date_2_from": "now/d",
                            "date_2_to": "now+1d/d",
                            "date_1_key": "all",
                            "date_1_from": "now/h",
                            "date_1_to": None
                        }
                    }
                },
                {
                    "id": "free_text_search",
                    "type": "search",
                    "dataField": [
                        "description.dutch"
                    ],
                    "execute": False,
                    "react": {
                        "and": "free_text_search__internal"
                    },
                    "customQuery": {}
                },
                {
                    "id": "agent_id",
                    "type": "term",
                    "dataField": [
                        "reactive_component_field"
                    ],
                    "execute": False,
                    "react": {
                        "and": "agent_id__internal"
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "timeout": "500ms"
                    }
                },
                {
                    "id": "object_type_house_orientation",
                    "type": "term",
                    "dataField": [
                        "object_type_specifications.house.orientation"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house",
                            "object_type_house_orientation__internal"
                        ],
                        "or": [
                            "object_type"
                        ]
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "id": "house-orientation-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    }
                },
                {
                    "id": "object_type_house",
                    "type": "term",
                    "dataField": [
                        "object_type_specifications.house.type"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_house_orientation",
                            "object_type_house__internal"
                        ],
                        "or": [
                            "object_type"
                        ]
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "id": "house-type-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    }
                },
                {
                    "id": "object_type_apartment_orientation",
                    "type": "term",
                    "dataField": [
                        "object_type_specifications.apartment.orientation"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_apartment",
                            "object_type_apartment_orientation__internal"
                        ],
                        "or": [
                            "object_type"
                        ]
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "id": "apartment-orientation-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    }
                },
                {
                    "id": "object_type_apartment",
                    "type": "term",
                    "dataField": [
                        "object_type_specifications.apartment.type"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_apartment_orientation",
                            "object_type_apartment__internal"
                        ],
                        "or": [
                            "object_type"
                        ]
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "id": "apartment-type-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    }
                },
                {
                    "id": "object_type_parking",
                    "type": "term",
                    "dataField": [
                        "object_type_specifications.parking.type"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_parking_capacity",
                            "object_type_parking__internal"
                        ],
                        "or": [
                            "object_type"
                        ]
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "id": "parking-type-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    }
                },
                {
                    "id": "object_type_parking_capacity",
                    "type": "term",
                    "dataField": [
                        "object_type_specifications.parking.capacity"
                    ],
                    "execute": False,
                    "react": {
                        "and": [
                            "selected_area",
                            "offering_type",
                            "sort",
                            "price",
                            "floor_area",
                            "plot_area",
                            "bedrooms",
                            "rooms",
                            "exterior_space_garden_size",
                            "garage_capacity",
                            "publication_date",
                            "availability",
                            "construction_type",
                            "construction_period",
                            "surrounding",
                            "garage_type",
                            "exterior_space_type",
                            "exterior_space_garden_orientation",
                            "energy_label",
                            "zoning",
                            "amenities",
                            "type",
                            "nvm_open_house_day",
                            "open_house",
                            "free_text_search",
                            "agent_id",
                            "object_type_parking",
                            "object_type_parking_capacity__internal"
                        ],
                        "or": [
                            "object_type"
                        ]
                    },
                    "customQuery": {},
                    "defaultQuery": {
                        "id": "parking-capacity-aggs-v3",
                        "params": {
                            "timeout": "500ms"
                        }
                    }
                }
            ]

        }

        data = await fetch_url('POST', url, 1, payload=payload, headers=headers,
                               )
        try:
            data = json.loads(data)['search_result']['hits']['hits']
        except Exception as err:
            logging.error(f'Error: {err}')
            data = []
        if data is not None:  # Check if data is not None before iterating
            data = [elm['_source'] for elm in data]
            result.extend(data)
        else:
            logging.error("Received no data to process")
    return result


async def scrape_data(file_name: str):
    data_koop = await main_koop()
    data_huur = await main_huur()
    data = []
    if data_koop:
        data.extend(data_koop)
    if data_huur:
        data.extend(data_huur)
    result = [{
        'url': 'https://www.funda.nl' + elm['object_detail_page_relative_url'],
        'selling_price': int(elm['price']['selling_price'][0]) if isinstance(elm['price'].get('selling_price'),
                                                                             list) and
                                                                  elm['price'].get('selling_price') else None,
        'rent_price': int(elm['price']['rent_price'][0]) if isinstance(elm['price'].get('rent_price'), list) and
                                                            elm['price'].get('rent_price') else None,
        'square_meters': elm['floor_area'][0],
        'bedrooms': elm['number_of_bedrooms'],
        'location': f"{elm['address']['city']}, {elm['address']['street_name']} {elm['address'].get('house_number', '')}",
    } for elm in data]
    if result:
        await ApartmentStore.create_or_update_apartment(result, file_name)
        # await check uniq result (service class in db)
        # await store uniq result (service class in db )
        # wait next function call
        pass


async def main():
    script_path = os.path.abspath(__file__)
    script_name = (os.path.basename(script_path)).split('.')[0]
    while True:
        await scrape_data(file_name=script_name)
        time.sleep(VESTEDA_CD)


if __name__ == "__main__":
    asyncio.run(main())
